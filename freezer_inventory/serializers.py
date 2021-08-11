from rest_framework import serializers
from .models import Freezer, FreezerRack, FreezerBox, FreezerInventory, FreezerCheckout
from users.enumerations import YesNo, MeasureUnits, VolUnits, InvStatus, InvTypes, \
    CheckoutActions
from rest_framework_gis.serializers import GeoFeatureModelSerializer
# would have to add another serializer that uses GeoFeatureModelSerializer class
# and a separate button for downloading GeoJSON format along with CSV


# Django REST Framework to allow the automatic downloading of data!
class FreezerSerializer(serializers.ModelSerializer):
    freezer_datetime = serializers.DateTimeField()
    freezer_label = serializers.CharField()
    freezer_depth = serializers.DecimalField()
    freezer_length = serializers.DecimalField()
    freezer_width = serializers.DecimalField()
    freezer_dimension_units = serializers.ChoiceField(choices=MeasureUnits.choices)
    # maximum number of columns, rows, and depth based on the number of boxes that can fit in each
    freezer_max_columns = serializers.IntegerField(min_value=1)
    freezer_max_rows = serializers.IntegerField(min_value=1)
    freezer_max_depth = serializers.IntegerField(min_value=1)
    created_datetime = serializers.DateTimeField()

    class Meta:
        model = Freezer
        fields = ['freezer_datetime', 'freezer_label',
                  'freezer_depth', 'freezer_length', 'freezer_width', 'freezer_dimension_units',
                  'freezer_max_columns', 'freezer_max_rows', 'freezer_max_depth',
                  'created_by', 'created_datetime', ]
    # Since created_by references a different table and we
    # want to show 'label' rather than some unintelligible field (like pk 1), have to add
    # slug to tell it to print the desired field from the other table
    created_by = serializers.SlugRelatedField(many=False, read_only=True,
                                              slug_field='email')


class FreezerRackSerializer(serializers.ModelSerializer):
    freezer_rack_datetime = serializers.DateTimeField()
    freezer_rack_label = serializers.CharField()
    # location of rack in freezer
    freezer_rack_column_start = serializers.IntegerField(min_value=1)
    freezer_rack_column_end = serializers.IntegerField(min_value=1)
    freezer_rack_row_start = serializers.IntegerField(min_value=1)
    freezer_rack_row_end = serializers.IntegerField(min_value=1)
    freezer_rack_depth_start = serializers.IntegerField(min_value=1)
    freezer_rack_depth_end = serializers.IntegerField(min_value=1)
    created_datetime = serializers.DateTimeField()

    class Meta:
        model = FreezerRack
        fields = ['freezer', 'freezer_rack_datetime', 'freezer_rack_label',
                  'freezer_rack_column_start', 'freezer_rack_column_end',
                  'freezer_rack_row_start', 'freezer_rack_row_end',
                  'freezer_rack_depth_start', 'freezer_rack_depth_end',
                  'created_by', 'created_datetime', ]
    # Since freezer and created_by reference different tables and we
    # want to show 'label' rather than some unintelligible field (like pk 1), have to add
    # slug to tell it to print the desired field from the other table
    created_by = serializers.SlugRelatedField(many=False, read_only=True,
                                              slug_field='email')
    freezer = serializers.SlugRelatedField(many=False, read_only=True,
                                           slug_field='freezer_label')


class FreezerBoxSerializer(serializers.ModelSerializer):
    freezer_box_datetime = serializers.DateTimeField()
    freezer_box_label = serializers.CharField()
    # location of box in freezer rack
    freezer_box_column = serializers.IntegerField(min_value=1)
    freezer_box_row = serializers.IntegerField(min_value=1)
    freezer_box_depth = serializers.IntegerField(min_value=1)
    created_datetime = serializers.DateTimeField()

    class Meta:
        model = FreezerBox
        fields = ['freezer_rack', 'freezer_box_datetime', 'freezer_box_label',
                  'freezer_box_column', 'freezer_box_row', 'freezer_box_depth',
                  'created_by', 'created_datetime', ]
    # Since freezer_rack and created_by reference different tables and we
    # want to show 'label' rather than some unintelligible field (like pk 1), have to add
    # slug to tell it to print the desired field from the other table
    created_by = serializers.SlugRelatedField(many=False, read_only=True,
                                              slug_field='email')
    freezer_rack = serializers.SlugRelatedField(many=False, read_only=True,
                                                slug_field='freezer_rack_label')


class FreezerInventorySerializer(serializers.ModelSerializer):
    barcode_slug = serializers.SlugField(max_length=27, allow_blank=True)
    freezer_inventory_type = serializers.ChoiceField(choices=InvTypes.choices)
    freezer_inventory_status = serializers.ChoiceField(choices=InvStatus.choices)
    # location of inventory in freezer box
    freezer_inventory_column = serializers.IntegerField(min_value=1)
    freezer_inventory_row = serializers.IntegerField(min_value=1)
    created_datetime = serializers.DateTimeField()

    class Meta:
        model = FreezerInventory
        fields = ['freezer_box', 'field_sample', 'extraction',
                  'barcode_slug', 'freezer_inventory_datetime',
                  'freezer_inventory_type', 'freezer_inventory_status',
                  'freezer_inventory_column', 'freezer_inventory_row',
                  'created_by', 'created_datetime', ]
    # Since freezer_box, field_sample, extraction, and created_by reference different tables and we
    # want to show 'label' rather than some unintelligible field (like pk 1), have to add
    # slug to tell it to print the desired field from the other table
    created_by = serializers.SlugRelatedField(many=False, read_only=True,
                                              slug_field='email')
    freezer_box = serializers.SlugRelatedField(many=False, read_only=True,
                                               slug_field='freezer_box_label')
    field_sample = serializers.SlugRelatedField(many=False, read_only=True,
                                                slug_field='field_sample_barcode')
    extraction = serializers.SlugRelatedField(many=False, read_only=True,
                                              slug_field='field_sample__field_sample_barcode')


class FreezerCheckoutSerializer(serializers.ModelSerializer):
    freezer_checkout_action = serializers.ChoiceField(choices=CheckoutActions.choices)
    freezer_checkout_datetime = serializers.DateTimeField()
    freezer_return_datetime = serializers.DateTimeField()
    freezer_return_vol_taken = serializers.DecimalField()
    freezer_return_vol_units = serializers.ChoiceField(choices=VolUnits.choices)
    freezer_return_notes = serializers.CharField()
    freezer_perm_removal_datetime = serializers.DateTimeField()
    created_datetime = serializers.DateTimeField()

    class Meta:
        model = FreezerCheckout
        fields = ['freezer_box', 'field_sample', 'extraction', 'freezer_inventory_datetime',
                  'freezer_inventory_type', 'freezer_inventory_status',
                  'freezer_inventory_column', 'freezer_inventory_row',
                  'created_by', 'created_datetime', ]
    # Since freezer_inventory and created_by reference different tables and we
    # want to show 'label' rather than some unintelligible field (like pk 1), have to add
    # slug to tell it to print the desired field from the other table
    created_by = serializers.SlugRelatedField(many=False, read_only=True,
                                              slug_field='email')
    freezer_inventory = serializers.SlugRelatedField(many=False, read_only=True,
                                                     slug_field='barcode_slug')
