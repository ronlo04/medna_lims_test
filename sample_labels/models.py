# Create your models here.
import datetime
#from django.db import models
# swapping to GeoDjango
from django.contrib.gis.db import models
from field_sites.models import FieldSite
from users.models import DateTimeUserMixin
from django.core.validators import MinValueValidator
import numpy as np

def current_year():
    return datetime.date.today().year

class SampleType(DateTimeUserMixin):
    sample_type_code = models.CharField("System Code", max_length=1, unique=True)
    sample_type_label = models.CharField("System Label", max_length=200)

    def __str__(self):
        return '{code}: {label}'.format(code=self.sample_type_code, label=self.sample_type_label)

class SampleLabelRequest(DateTimeUserMixin):
    # With RESTRICT, if project is deleted but system and region still exists, it will not cascade delete
    # unless all 3 related fields are gone.
    site_id = models.ForeignKey(FieldSite, on_delete=models.RESTRICT)
    sample_type = models.ForeignKey(SampleType, on_delete=models.RESTRICT)
    sample_year = models.PositiveIntegerField("Sample Year", default=current_year(), validators=[MinValueValidator(2018)])
    purpose = models.CharField("Sample Label Purpose", max_length=200)
    sample_label_prefix = models.CharField("Sample Label Prefix", max_length=11)
    req_sample_label_num = models.IntegerField("Number Requested", default=1)
    min_sample_label_num = models.IntegerField(default=1)
    max_sample_label_num = models.IntegerField(default=1)
    min_sample_label_id = models.CharField("Min Sample Label ID", max_length=16)
    max_sample_label_id = models.CharField("Max Sample Label ID", max_length=16)

    def __str__(self):
        return self.max_sample_label_id

    def insert_update_sample_id_req(self, min_sample_label_id, max_sample_label_id, min_sample_label_num,
                                    max_sample_label_num, sample_label_prefix, site_id, sample_type, sample_year,
                                    purpose):
        if min_sample_label_id == max_sample_label_id:
            # only one label request, so min and max label id will be the same; only need to enter
            # one new label into SampleLabel
            sample_label_id = min_sample_label_id
            SampleLabel.objects.update_or_create(
                sample_label_id=sample_label_id,
                site_id=site_id,
                sample_type=sample_type,
                sample_year=sample_year,
                purpose=purpose
            )
        else:
            # more than one label requested, so need to interate to insert into SampleLabel
            # arange does not include max value, hence max+1
            for num in np.arange(min_sample_label_num, max_sample_label_num + 1, 1):
                # add leading zeros to site_num, e.g., 1 to 01
                num_leading_zeros = str(num).zfill(4)

                # format site_id, e.g., "eAL_L01"
                sample_label_id = '{labelprefix}_{sitenum}'.format(labelprefix=sample_label_prefix,
                                                                   sitenum=num_leading_zeros)
                # enter each new label into SampleLabel - request only has a single row with the requested
                # number and min/max; this table is necessary for joining proceeding tables
                SampleLabel.objects.update_or_create(
                    sample_label_id=sample_label_id,
                    site_id=site_id,
                    sample_type=sample_type,
                    sample_year=sample_year,
                    purpose=purpose
                )
    def save(self, *args, **kwargs):
        # if it already exists we don't want to change the site_id; we only want to update the associated fields.
        if self.pk is None:
            last_twosigits_year = str(self.sample_year)[-2:]
            # concatenate project, region, and system to create sample_label_prefix, e.g., "eAL_L"
            self.sample_label_prefix = '{site}_{twosigits_year}{sample_type}'.format(site=self.site_id.site_id,
                                                                                     twosigits_year=last_twosigits_year,
                                                                                     sample_type=self.sample_type.sample_type_code)
            # Retrieve a list of `Site` instances, group them by the sample_label_prefix and sort them by
            # the `site_num` field and get the largest entry - Returns the next default value for the `site_num` field
            largest = SampleLabelRequest.objects.only('sample_label_prefix', 'max_sample_label_num').filter(sample_label_prefix=self.sample_label_prefix).order_by('max_sample_label_num').last()
            if not largest:
                # largest is `None` if `Site` has no instances
                # in which case we return the start value of 1
                self.min_sample_label_num = 1
                self.max_sample_label_num = self.req_sample_label_num
            else:
                # If an instance of `Site` is returned, we get it's
                # `site_num` attribute and increment it by 1
                self.min_sample_label_num = largest.max_sample_label_num + 1
                self.max_sample_label_num = largest.max_sample_label_num + self.req_sample_label_num
            # add leading zeros to site_num, e.g., 1 to 01
            min_num_leading_zeros = str(self.min_sample_label_num).zfill(4)
            max_num_leading_zeros = str(self.max_sample_label_num).zfill(4)
            # format site_id, e.g., "eAL_L01"
            self.min_sample_label_id = '{labelprefix}_{sitenum}'.format(labelprefix=self.sample_label_prefix, sitenum=min_num_leading_zeros)
            self.max_sample_label_id = '{labelprefix}_{sitenum}'.format(labelprefix=self.sample_label_prefix, sitenum=max_num_leading_zeros)
            self.insert_update_sample_id_req(self.min_sample_label_id, self.max_sample_label_id,
                                             self.min_sample_label_num, self.max_sample_label_num,
                                             self.sample_label_prefix, self.site_id,
                                             self.sample_type, self.sample_year, self.purpose)
        # all done, time to save changes to the db
        super(SampleLabelRequest, self).save(*args, **kwargs)

class SampleLabel(DateTimeUserMixin):
    sample_label_id = models.CharField("Sample Label ID", max_length=16, unique=True)
    # With RESTRICT, if project is deleted but system and region still exists, it will not cascade delete
    # unless all 3 related fields are gone.
    site_id = models.ForeignKey(FieldSite, on_delete=models.RESTRICT)
    sample_type = models.ForeignKey(SampleType, on_delete=models.RESTRICT)
    sample_year = models.PositiveIntegerField("Sample Year", default=current_year(), validators=[MinValueValidator(2018)])
    purpose = models.CharField("Sample Label Purpose", max_length=200)

    def __str__(self):
        return self.sample_label_id