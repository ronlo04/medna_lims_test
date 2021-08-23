from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import ReferenceDatabase, TaxonDomain, TaxonKingdom, TaxonPhylum, \
    TaxonClass, TaxonOrder, TaxonFamily, TaxonGenus, TaxonSpecies, AnnotationMethod, \
    AnnotationMetadata, TaxonomicAnnotation
from utility.models import ProcessLocation
from bioinfo_denoising.models import AmpliconSequenceVariant
from users.models import CustomUser


class ReferenceDatabaseAdminResource(resources.ModelResource):
    class Meta:
        model = ReferenceDatabase
        import_id_fields = ('refdb_name', 'refdb_version', 'refdb_datetime',
                            'redfb_coverage_score', )
        # exclude = ('site_prefix', 'site_num')
        fields = ('id', 'refdb_name', 'refdb_version', 'refdb_slug', 'refdb_datetime', 'redfb_coverage_score',
                  'refdb_repo_url', 'created_by', 'created_datetime',)
        export_order = ('id', 'refdb_name', 'refdb_version', 'refdb_slug', 'refdb_datetime', 'redfb_coverage_score',
                        'refdb_repo_url', 'created_by', 'created_datetime',)

    created_by = fields.Field(
        column_name='created_by',
        attribute='created_by',
        widget=ForeignKeyWidget(CustomUser, 'email'))

    def before_import_row(self, row, **kwargs):
        row['created_by'] = kwargs['user'].id


class TaxonDomainAdminResource(resources.ModelResource):
    class Meta:
        model = TaxonDomain
        import_id_fields = ('taxon_domain', )
        # exclude = ('site_prefix', 'site_num')
        fields = ('id', 'taxon_domain',
                  'created_by', 'created_datetime', )
        export_order = ('id', 'taxon_domain',
                        'created_by', 'created_datetime', )

    created_by = fields.Field(
        column_name='created_by',
        attribute='created_by',
        widget=ForeignKeyWidget(CustomUser, 'email'))

    def before_import_row(self, row, **kwargs):
        row['created_by'] = kwargs['user'].id


class TaxonKingdomAdminResource(resources.ModelResource):
    class Meta:
        model = TaxonKingdom
        import_id_fields = ('taxon_domain', 'taxon_kingdom', )
        # exclude = ('site_prefix', 'site_num')
        fields = ('id', 'taxon_domain', 'taxon_kingdom',
                  'created_by', 'created_datetime', )
        export_order = ('id', 'taxon_domain', 'taxon_kingdom',
                        'created_by', 'created_datetime', )

    taxon_domain_slug = fields.Field(
        column_name='taxon_domain_slug',
        attribute='taxon_domain_slug',
        widget=ForeignKeyWidget(TaxonDomain, 'taxon_domain'))

    created_by = fields.Field(
        column_name='created_by',
        attribute='created_by',
        widget=ForeignKeyWidget(CustomUser, 'email'))

    def before_import_row(self, row, **kwargs):
        row['created_by'] = kwargs['user'].id


class TaxonPhylumAdminResource(resources.ModelResource):
    class Meta:
        model = TaxonPhylum
        import_id_fields = ('taxon_domain', 'taxon_kingdom', 'taxon_phylum', )
        # exclude = ('site_prefix', 'site_num')
        fields = ('id', 'taxon_domain', 'taxon_kingdom', 'taxon_phylum',
                  'created_by', 'created_datetime', )
        export_order = ('id', 'taxon_domain', 'taxon_kingdom', 'taxon_phylum',
                        'created_by', 'created_datetime',)

    taxon_kingdom_slug = fields.Field(
        column_name='taxon_kingdom_slug',
        attribute='taxon_kingdom_slug',
        widget=ForeignKeyWidget(TaxonKingdom, 'taxon_kingdom'))

    created_by = fields.Field(
        column_name='created_by',
        attribute='created_by',
        widget=ForeignKeyWidget(CustomUser, 'email'))

    def before_import_row(self, row, **kwargs):
        row['created_by'] = kwargs['user'].id


class TaxonClassAdminResource(resources.ModelResource):
    class Meta:
        model = TaxonClass
        import_id_fields = ('taxon_domain', 'taxon_kingdom', 'taxon_phylum', 'taxon_class', )
        # exclude = ('site_prefix', 'site_num')
        fields = ('id', 'taxon_domain', 'taxon_kingdom', 'taxon_phylum', 'taxon_class',
                  'created_by', 'created_datetime',)
        export_order = ('id', 'taxon_domain', 'taxon_kingdom', 'taxon_phylum', 'taxon_class',
                        'created_by', 'created_datetime',)

    taxon_phylum_slug = fields.Field(
        column_name='taxon_phylum_slug',
        attribute='taxon_phylum_slug',
        widget=ForeignKeyWidget(TaxonPhylum, 'taxon_phylum'))

    created_by = fields.Field(
        column_name='created_by',
        attribute='created_by',
        widget=ForeignKeyWidget(CustomUser, 'email'))

    def before_import_row(self, row, **kwargs):
        row['created_by'] = kwargs['user'].id


class TaxonOrderAdminResource(resources.ModelResource):
    class Meta:
        model = TaxonOrder
        import_id_fields = ('taxon_domain', 'taxon_kingdom', 'taxon_phylum', 'taxon_class',
                            'taxon_order', )
        # exclude = ('site_prefix', 'site_num')
        fields = ('id', 'taxon_domain', 'taxon_kingdom', 'taxon_phylum', 'taxon_class', 'taxon_order',
                  'created_by', 'created_datetime',)
        export_order = ('id', 'taxon_domain', 'taxon_kingdom', 'taxon_phylum', 'taxon_class', 'taxon_order',
                        'created_by', 'created_datetime',)

    taxon_class_slug = fields.Field(
        column_name='taxon_class_slug',
        attribute='taxon_class_slug',
        widget=ForeignKeyWidget(TaxonClass, 'taxon_class'))

    created_by = fields.Field(
        column_name='created_by',
        attribute='created_by',
        widget=ForeignKeyWidget(CustomUser, 'email'))

    def before_import_row(self, row, **kwargs):
        row['created_by'] = kwargs['user'].id


class TaxonFamilyAdminResource(resources.ModelResource):
    class Meta:
        model = TaxonFamily
        import_id_fields = ('taxon_domain', 'taxon_kingdom', 'taxon_phylum', 'taxon_class',
                            'taxon_order', 'taxon_family',)
        # exclude = ('site_prefix', 'site_num')
        fields = ('id', 'taxon_domain', 'taxon_kingdom', 'taxon_phylum',
                  'taxon_class', 'taxon_order', 'taxon_family',
                  'created_by', 'created_datetime',)
        export_order = ('id', 'taxon_domain', 'taxon_kingdom', 'taxon_phylum',
                        'taxon_class', 'taxon_order', 'taxon_family',
                        'created_by', 'created_datetime',)

    taxon_order_slug = fields.Field(
        column_name='taxon_order_slug',
        attribute='taxon_order_slug',
        widget=ForeignKeyWidget(TaxonOrder, 'taxon_order'))

    created_by = fields.Field(
        column_name='created_by',
        attribute='created_by',
        widget=ForeignKeyWidget(CustomUser, 'email'))

    def before_import_row(self, row, **kwargs):
        row['created_by'] = kwargs['user'].id


class TaxonGenusAdminResource(resources.ModelResource):
    class Meta:
        model = TaxonGenus
        import_id_fields = ('taxon_domain', 'taxon_kingdom', 'taxon_phylum', 'taxon_class',
                            'taxon_order', 'taxon_family', 'taxon_genus', )
        # exclude = ('site_prefix', 'site_num')
        fields = ('id', 'taxon_domain', 'taxon_kingdom', 'taxon_phylum', 'taxon_class',
                  'taxon_order', 'taxon_family', 'taxon_genus',
                  'created_by', 'created_datetime',)
        export_order = ('id', 'taxon_domain', 'taxon_kingdom', 'taxon_phylum', 'taxon_class',
                        'taxon_order', 'taxon_family', 'taxon_genus',
                        'created_by', 'created_datetime',)

    taxon_family_slug = fields.Field(
        column_name='taxon_family_slug',
        attribute='taxon_family_slug',
        widget=ForeignKeyWidget(TaxonFamily, 'taxon_family'))

    created_by = fields.Field(
        column_name='created_by',
        attribute='created_by',
        widget=ForeignKeyWidget(CustomUser, 'email'))

    def before_import_row(self, row, **kwargs):
        row['created_by'] = kwargs['user'].id


class TaxonSpeciesAdminResource(resources.ModelResource):
    class Meta:
        model = TaxonSpecies
        import_id_fields = ('taxon_domain', 'taxon_kingdom', 'taxon_phylum', 'taxon_class',
                            'taxon_order', 'taxon_family', 'taxon_genus', 'taxon_species',)
        # exclude = ('site_prefix', 'site_num')
        fields = ('id', 'taxon_domain', 'taxon_kingdom', 'taxon_phylum', 'taxon_class',
                  'taxon_order', 'taxon_family', 'taxon_genus', 'taxon_species',
                  'taxon_common_name', 'is_endemic',
                  'created_by', 'created_datetime',)
        export_order = ('id', 'taxon_domain', 'taxon_kingdom', 'taxon_phylum', 'taxon_class',
                        'taxon_order', 'taxon_family', 'taxon_genus', 'taxon_species',
                        'taxon_common_name', 'is_endemic',
                        'created_by', 'created_datetime',)

    taxon_genus_slug = fields.Field(
        column_name='taxon_genus_slug',
        attribute='taxon_genus_slug',
        widget=ForeignKeyWidget(TaxonGenus, 'taxon_genus'))

    created_by = fields.Field(
        column_name='created_by',
        attribute='created_by',
        widget=ForeignKeyWidget(CustomUser, 'email'))

    def before_import_row(self, row, **kwargs):
        row['created_by'] = kwargs['user'].id


class TaxonAdminResource(resources.ModelResource):
    class Meta:
        model = TaxonSpecies
        import_id_fields = ('taxon_domain', 'taxon_kingdom', 'taxon_phylum', 'taxon_class',
                            'taxon_order', 'taxon_family', 'taxon_genus', 'taxon_species', )
        # exclude = ('site_prefix', 'site_num')
        fields = ('id', 'taxon_domain', 'taxon_kingdom', 'taxon_phylum', 'taxon_class',
                  'taxon_order', 'taxon_family', 'taxon_genus', 'taxon_species',
                  'taxon_common_name', 'is_endemic', )
        export_order = ('id', 'taxon_domain', 'taxon_kingdom', 'taxon_phylum', 'taxon_class',
                        'taxon_order', 'taxon_family', 'taxon_genus', 'taxon_species',
                        'taxon_common_name', 'is_endemic', )

    taxon_domain = fields.Field(
        column_name='taxon_domain',
        attribute='taxon_domain',
        widget=ForeignKeyWidget(TaxonDomain, 'taxon_domain'))

    taxon_kingdom = fields.Field(
        column_name='taxon_kingdom',
        attribute='taxon_kingdom',
        widget=ForeignKeyWidget(TaxonKingdom, 'taxon_kingdom'))

    taxon_phylum = fields.Field(
        column_name='taxon_phylum',
        attribute='taxon_phylum',
        widget=ForeignKeyWidget(TaxonPhylum, 'taxon_phylum'))

    taxon_class = fields.Field(
        column_name='taxon_class',
        attribute='taxon_class',
        widget=ForeignKeyWidget(TaxonClass, 'taxon_class'))

    taxon_order = fields.Field(
        column_name='taxon_order',
        attribute='taxon_order',
        widget=ForeignKeyWidget(TaxonOrder, 'taxon_order'))

    taxon_family = fields.Field(
        column_name='taxon_family',
        attribute='taxon_family',
        widget=ForeignKeyWidget(TaxonFamily, 'taxon_family'))

    taxon_genus = fields.Field(
        column_name='taxon_genus',
        attribute='taxon_genus',
        widget=ForeignKeyWidget(TaxonGenus, 'taxon_genus'))


class AnnotationMethodAdminResource(resources.ModelResource):
    class Meta:
        model = AnnotationMethod
        import_id_fields = ('annotation_method_name', )
        # exclude = ('site_prefix', 'site_num')
        fields = ('id', 'annotation_method_name',
                  'created_by', 'created_datetime', )
        export_order = ('id', 'annotation_method_name',
                        'created_by', 'created_datetime', )

    created_by = fields.Field(
        column_name='created_by',
        attribute='created_by',
        widget=ForeignKeyWidget(CustomUser, 'email'))

    def before_import_row(self, row, **kwargs):
        row['created_by'] = kwargs['user'].id


class AnnotationMetadataAdminResource(resources.ModelResource):
    class Meta:
        model = AnnotationMetadata
        import_id_fields = ('analysis_datetime', 'annotation_method',
                            'analyst_first_name', 'analyst_last_name', )
        # exclude = ('site_prefix', 'site_num')
        fields = ('id', 'process_location', 'analysis_datetime', 'annotation_method',
                  'analyst_first_name', 'analyst_last_name',
                  'analysis_sop_url', 'analysis_script_repo_url',
                  'created_by', 'created_datetime', )
        export_order = ('id', 'process_location', 'analysis_datetime', 'annotation_method',
                        'analyst_first_name', 'analyst_last_name',
                        'analysis_sop_url', 'analysis_script_repo_url',
                        'created_by', 'created_datetime', )

    process_location = fields.Field(
        column_name='process_location',
        attribute='process_location',
        widget=ForeignKeyWidget(ProcessLocation, 'process_location_name'))

    annotation_method = fields.Field(
        column_name='annotation_method',
        attribute='annotation_method',
        widget=ForeignKeyWidget(AnnotationMethod, 'annotation_method_name'))

    created_by = fields.Field(
        column_name='created_by',
        attribute='created_by',
        widget=ForeignKeyWidget(CustomUser, 'email'))

    def before_import_row(self, row, **kwargs):
        row['created_by'] = kwargs['user'].id


class TaxonomicAnnotationAdminResource(resources.ModelResource):
    class Meta:
        model = TaxonomicAnnotation
        import_id_fields = ('asv', 'annotation_metadata', 'reference_database', )
        # exclude = ('site_prefix', 'site_num')
        fields = ('id', 'asv', 'annotation_metadata',
                  'reference_database', 'confidence',
                  'ta_taxon', 'ta_domain', 'ta_kingdom',
                  'ta_phylum', 'ta_class', 'ta_order',
                  'ta_family', 'ta_genus', 'ta_species',
                  'ta_common_name', 'manual_domain',
                  'manual_kingdom', 'manual_phylum',
                  'manual_class', 'manual_order',
                  'manual_family', 'manual_genus',
                  'manual_species',
                  'created_by', 'created_datetime', )
        export_order = ('id', 'asv', 'annotation_metadata',
                        'reference_database', 'confidence',
                        'ta_taxon', 'ta_domain', 'ta_kingdom',
                        'ta_phylum', 'ta_class', 'ta_order',
                        'ta_family', 'ta_genus', 'ta_species',
                        'ta_common_name', 'manual_domain',
                        'manual_kingdom', 'manual_phylum',
                        'manual_class', 'manual_order',
                        'manual_family', 'manual_genus',
                        'manual_species',
                        'created_by', 'created_datetime', )

    asv = fields.Field(
        column_name='asv',
        attribute='asv',
        widget=ForeignKeyWidget(AmpliconSequenceVariant, 'asv_id'))

    annotation_metadata = fields.Field(
        column_name='annotation_metadata',
        attribute='annotation_metadata',
        widget=ForeignKeyWidget(AnnotationMethod, 'annotation_slug'))

    reference_database = fields.Field(
        column_name='reference_database',
        attribute='reference_database',
        widget=ForeignKeyWidget(ReferenceDatabase, 'refdb_slug'))

    manual_domain = fields.Field(
        column_name='manual_domain',
        attribute='manual_domain',
        widget=ForeignKeyWidget(TaxonDomain, 'taxon_domain'))

    manual_kingdom = fields.Field(
        column_name='manual_kingdom',
        attribute='manual_kingdom',
        widget=ForeignKeyWidget(TaxonKingdom, 'taxon_kingdom'))

    manual_phylum = fields.Field(
        column_name='manual_phylum',
        attribute='manual_phylum',
        widget=ForeignKeyWidget(TaxonPhylum, 'taxon_phylum'))

    manual_class = fields.Field(
        column_name='manual_class',
        attribute='manual_class',
        widget=ForeignKeyWidget(TaxonClass, 'taxon_class'))

    manual_order = fields.Field(
        column_name='manual_order',
        attribute='manual_order',
        widget=ForeignKeyWidget(TaxonOrder, 'taxon_order'))

    manual_family = fields.Field(
        column_name='manual_family',
        attribute='manual_family',
        widget=ForeignKeyWidget(TaxonFamily, 'taxon_family'))

    manual_genus = fields.Field(
        column_name='manual_genus',
        attribute='manual_genus',
        widget=ForeignKeyWidget(TaxonGenus, 'taxon_genus'))

    manual_species = fields.Field(
        column_name='manual_species',
        attribute='manual_species',
        widget=ForeignKeyWidget(TaxonSpecies, 'taxon_species'))

    created_by = fields.Field(
        column_name='created_by',
        attribute='created_by',
        widget=ForeignKeyWidget(CustomUser, 'email'))

    def before_import_row(self, row, **kwargs):
        row['created_by'] = kwargs['user'].id
