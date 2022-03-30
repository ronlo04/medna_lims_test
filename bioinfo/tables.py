import django_tables2 as tables
from .models import QualityMetadata, DenoiseClusterMethod, DenoiseClusterMetadata, FeatureOutput, FeatureRead, \
    ReferenceDatabase, TaxonDomain, TaxonKingdom, TaxonSupergroup, TaxonPhylumDivision, TaxonClass,  TaxonOrder, \
    TaxonFamily, TaxonGenus, TaxonSpecies, AnnotationMethod, AnnotationMetadata, TaxonomicAnnotation
from django_tables2.utils import A


class QualityMetadataTable(tables.Table):
    edit = tables.LinkColumn("update_qualitymetadata", text='Update', args=[A("pk")], orderable=False)
    # formatting for date column
    created_datetime = tables.DateTimeColumn(format="M d, Y h:i a")
    modified_datetime = tables.DateTimeColumn(format="M d, Y h:i a")
    created_by = tables.Column(accessor='created_by.email')
    _selected_action = tables.CheckBoxColumn(accessor="pk",
                                             attrs={"td": {"class": "action-checkbox"},
                                                    "input": {"class": "action-select"},
                                                    "th__input": {"id": "action-toggle"},
                                                    "th": {"class": "action-checkbox-column"}},
                                             orderable=False)

    class Meta:
        model = QualityMetadata
        fields = ('_selected_action', 'id', 'analysis_label', 'process_location', 'analysis_datetime',
                  'run_result',
                  'analyst_first_name', 'analyst_last_name',
                  'seq_quality_check', 'chimera_check', 'trim_length_forward', 'trim_length_reverse',
                  'min_read_length', 'max_read_length',
                  'analysis_sop_url', 'analysis_script_repo_url', 'quality_slug',
                  'created_by', 'created_datetime', 'modified_datetime', )


class DenoiseClusterMetadataTable(tables.Table):
    edit = tables.LinkColumn("update_denoiseclustermetadata", text='Update', args=[A("pk")], orderable=False)
    # formatting for date column
    created_datetime = tables.DateTimeColumn(format="M d, Y h:i a")
    modified_datetime = tables.DateTimeColumn(format="M d, Y h:i a")
    created_by = tables.Column(accessor='created_by.email')
    _selected_action = tables.CheckBoxColumn(accessor="pk",
                                             attrs={"td": {"class": "action-checkbox"},
                                                    "input": {"class": "action-select"},
                                                    "th__input": {"id": "action-toggle"},
                                                    "th": {"class": "action-checkbox-column"}},
                                             orderable=False)

    class Meta:
        model = DenoiseClusterMetadata
        fields = ('_selected_action', 'id', 'analysis_label', 'process_location', 'analysis_datetime',
                  'quality_metadata', 'denoise_cluster_method',
                  'analyst_first_name', 'analyst_last_name',
                  'analysis_sop_url', 'analysis_script_repo_url', 'denoise_cluster_slug',
                  'created_by', 'created_datetime', 'modified_datetime', )


class FeatureOutputTable(tables.Table):
    edit = tables.LinkColumn("update_featureoutput", text='Update', args=[A("pk")], orderable=False)
    # formatting for date column
    created_datetime = tables.DateTimeColumn(format="M d, Y h:i a")
    modified_datetime = tables.DateTimeColumn(format="M d, Y h:i a")
    created_by = tables.Column(accessor='created_by.email')
    _selected_action = tables.CheckBoxColumn(accessor="pk",
                                             attrs={"td": {"class": "action-checkbox"},
                                                    "input": {"class": "action-select"},
                                                    "th__input": {"id": "action-toggle"},
                                                    "th": {"class": "action-checkbox-column"}},
                                             orderable=False)

    class Meta:
        model = FeatureOutput
        fields = ('_selected_action', 'id', 'feature_id', 'feature_slug', 'feature_sequence',
                  'denoise_cluster_metadata',
                  'created_by', 'created_datetime', 'modified_datetime', )


class FeatureReadTable(tables.Table):
    edit = tables.LinkColumn("update_featureread", text='Update', args=[A("pk")], orderable=False)
    # formatting for date column
    created_datetime = tables.DateTimeColumn(format="M d, Y h:i a")
    modified_datetime = tables.DateTimeColumn(format="M d, Y h:i a")
    created_by = tables.Column(accessor='created_by.email')
    _selected_action = tables.CheckBoxColumn(accessor="pk",
                                             attrs={"td": {"class": "action-checkbox"},
                                                    "input": {"class": "action-select"},
                                                    "th__input": {"id": "action-toggle"},
                                                    "th": {"class": "action-checkbox-column"}},
                                             orderable=False)

    class Meta:
        model = FeatureRead
        fields = ('_selected_action', 'id', 'read_slug', 'feature', 'extraction', 'number_reads',
                  'created_by', 'created_datetime', 'modified_datetime', )


class AnnotationMetadataTable(tables.Table):
    edit = tables.LinkColumn("update_annotationmetadata", text='Update', args=[A("pk")], orderable=False)
    # formatting for date column
    created_datetime = tables.DateTimeColumn(format="M d, Y h:i a")
    modified_datetime = tables.DateTimeColumn(format="M d, Y h:i a")
    created_by = tables.Column(accessor='created_by.email')
    _selected_action = tables.CheckBoxColumn(accessor="pk",
                                             attrs={"td": {"class": "action-checkbox"},
                                                    "input": {"class": "action-select"},
                                                    "th__input": {"id": "action-toggle"},
                                                    "th": {"class": "action-checkbox-column"}},
                                             orderable=False)

    class Meta:
        model = AnnotationMetadata
        fields = ('_selected_action', 'id', 'analysis_label', 'process_location', 'denoise_cluster_metadata', 'analysis_datetime', 'annotation_method',
                  'analyst_first_name', 'analyst_last_name',
                  'analysis_sop_url', 'analysis_script_repo_url', 'annotation_slug',
                  'created_by', 'created_datetime', 'modified_datetime', )


class TaxonomicAnnotationTable(tables.Table):
    edit = tables.LinkColumn("update_annotationmetadata", text='Update', args=[A("pk")], orderable=False)
    # formatting for date column
    created_datetime = tables.DateTimeColumn(format="M d, Y h:i a")
    modified_datetime = tables.DateTimeColumn(format="M d, Y h:i a")
    created_by = tables.Column(accessor='created_by.email')
    _selected_action = tables.CheckBoxColumn(accessor="pk",
                                             attrs={"td": {"class": "action-checkbox"},
                                                    "input": {"class": "action-select"},
                                                    "th__input": {"id": "action-toggle"},
                                                    "th": {"class": "action-checkbox-column"}},
                                             orderable=False)

    class Meta:
        model = TaxonomicAnnotation
        fields = ('_selected_action', 'id', 'feature', 'annotation_metadata',
                  'reference_database', 'confidence',
                  'ta_taxon', 'ta_domain', 'ta_kingdom', 'ta_supergroup',
                  'ta_phylum_division', 'ta_class', 'ta_order',
                  'ta_family', 'ta_genus', 'ta_species',
                  'ta_common_name', 'manual_domain',
                  'manual_kingdom', 'manual_supergroup', 'manual_phylum_division',
                  'manual_class', 'manual_order',
                  'manual_family', 'manual_genus',
                  'manual_species', 'manual_notes',
                  'annotation_slug',
                  'created_by', 'created_datetime', 'modified_datetime', )
