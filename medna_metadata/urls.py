"""medna_metadata URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from allauth.account.views import confirm_email, signup
from dj_rest_auth.registration.views import VerifyEmailView
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from users import views as users_views
from field_sites.views import EnvoBiomeFirstViewSet, EnvoBiomeSecondViewSet, EnvoBiomeThirdViewSet, \
    EnvoBiomeFourthViewSet, EnvoBiomeFifthViewSet, \
    EnvoFeatureFirstViewSet, EnvoFeatureSecondViewSet, EnvoFeatureThirdViewSet, EnvoFeatureFourthViewSet, \
    EnvoFeatureFifthViewSet, EnvoFeatureSixthViewSet, EnvoFeatureSeventhViewSet, \
    SystemViewSet, GeoWatershedViewSet, GeoFieldSitesViewSet
from sample_labels.views import SampleTypeViewSet, SampleMaterialViewSet, SampleLabelRequestViewSet, SampleBarcodeViewSet
from field_survey.views import GeoFieldSurveyViewSet, FieldCrewViewSet, EnvMeasurementViewSet, FieldCollectionViewSet, \
    WaterCollectionViewSet, SedimentCollectionViewSet, FieldSampleViewSet, FilterSampleViewSet, SubCoreSampleViewSet, \
    GeoFieldSurveyETLViewSet, FieldCrewETLViewSet, EnvMeasurementETLViewSet, \
    FieldCollectionETLViewSet, SampleFilterETLViewSet, FieldSurveyFiltersNestedViewSet, FieldSurveySubCoresNestedViewSet
from wet_lab.views import PrimerPairViewSet, IndexPairViewSet, IndexRemovalMethodViewSet, SizeSelectionMethodViewSet, \
    QuantificationMethodViewSet, ExtractionMethodViewSet, ExtractionViewSet, PcrReplicateViewSet, PcrViewSet, \
    LibraryPrepViewSet, PooledLibraryViewSet, RunPrepViewSet, RunResultViewSet, \
    FastqFileViewSet, AmplificationMethodViewSet
from freezer_inventory.views import ReturnActionViewSet, FreezerViewSet, FreezerRackViewSet, FreezerBoxViewSet, \
    FreezerInventoryViewSet, FreezerInventoryLogViewSet, FreezerInventoryReturnMetadataViewSet, \
    FreezerInventoryLocNestedViewSet, FreezerInventoryLogsNestedViewSet, FreezerInventoryReturnsNestedViewSet
from bioinfo_denoclust.views import DenoiseClusterMethodViewSet, DenoiseClusterMetadataViewSet, \
    FeatureOutputViewSet, FeatureReadViewSet, QualityMetadataViewSet
from bioinfo_taxon.views import ReferenceDatabaseViewSet, \
    TaxonDomainViewSet, TaxonKingdomViewSet, TaxonPhylumViewSet, \
    TaxonClassViewSet, TaxonOrderViewSet, TaxonFamilyViewSet, \
    TaxonGenusViewSet, TaxonSpeciesViewSet, \
    AnnotationMethodViewSet, AnnotationMetadataViewSet, TaxonomicAnnotationViewSet
from utility.views import GrantViewSet, ProjectViewSet, ProcessLocationViewSet, YesNoChoicesViewSet, InvLocStatusChoicesViewSet, \
    TempUnitsChoicesViewSet, MeasureUnitsChoicesViewSet, VolUnitsChoicesViewSet, ConcentrationUnitsChoicesViewSet, \
    PhiXConcentrationUnitsChoicesViewSet, PcrUnitsChoicesViewSet, \
    WindSpeedsChoicesViewSet, CloudCoversChoicesViewSet, PrecipTypesChoicesViewSet, \
    TurbidTypesChoicesViewSet, EnvoMaterialsChoicesViewSet, MeasureModesChoicesViewSet, \
    EnvInstrumentsChoicesViewSet, YsiModelsChoicesViewSet, EnvMeasurementsChoicesViewSet, \
    BottomSubstratesChoicesViewSet, WaterCollectionModesChoicesViewSet, CollectionTypesChoicesViewSet, \
    FilterLocationsChoicesViewSet, ControlTypesChoicesViewSet, FilterMethodsChoicesViewSet, \
    FilterTypesChoicesViewSet, CoreMethodsChoicesViewSet, SubCoreMethodsChoicesViewSet, \
    TargetGenesChoicesViewSet, SubFragmentsChoicesViewSet, PcrTypesChoicesViewSet, \
    LibPrepTypesChoicesViewSet, LibPrepKitsChoicesViewSet, \
    InvStatusChoicesViewSet, InvTypesChoicesViewSet, CheckoutActionsChoicesViewSet, \
    CustomUserCssViewSet, DefaultSiteCssViewSet, SeqMethodsChoicesViewSet, InvestigationTypesChoicesViewSet, \
    LibLayoutsChoicesViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Maine-eDNA Metadata API",
        default_version='v1',
        description="a data management system for tracking environmental DNA samples",
        terms_of_service="https://github.com/Maine-eDNA/medna-metadata/blob/main/TOS.rst",
        contact=openapi.Contact(email="melissa.kimble@maine.edu"),
        license=openapi.License(name="GPL-3.0 License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
# users
router.register(r'users/user', users_views.CustomUserViewSet, 'users')
# utility
router.register(r'utility/grant', GrantViewSet, 'grant')
router.register(r'utility/project', ProjectViewSet, 'project')
router.register(r'utility/process_location', ProcessLocationViewSet, 'process_location')
router.register(r'utility/default_site_css', DefaultSiteCssViewSet, 'default_site_css')
router.register(r'utility/custom_user_css', CustomUserCssViewSet, 'custom_user_css')
# utility:enums
router.register(r'utility/choices_yes_no', YesNoChoicesViewSet, 'choices_yes_no')
router.register(r'utility/choices_temp_units', TempUnitsChoicesViewSet, 'choices_temp_units')
router.register(r'utility/choices_measure_units', MeasureUnitsChoicesViewSet, 'choices_measure_units')
router.register(r'utility/choices_vol_units', VolUnitsChoicesViewSet, 'choices_vol_units')
router.register(r'utility/choices_concentration_units', ConcentrationUnitsChoicesViewSet, 'choices_concentration_units')
router.register(r'utility/choices_phix_concentration_units', PhiXConcentrationUnitsChoicesViewSet, 'choices_phix_concentration_units')
router.register(r'utility/choices_pcr_units', PcrUnitsChoicesViewSet, 'choices_pcr_units')
router.register(r'utility/choices_wind_speeds', WindSpeedsChoicesViewSet, 'choices_wind_speeds')
router.register(r'utility/choices_cloud_covers', CloudCoversChoicesViewSet, 'choices_cloud_covers')
router.register(r'utility/choices_precip_types', PrecipTypesChoicesViewSet, 'choices_precip_types')
router.register(r'utility/choices_turbid_types', TurbidTypesChoicesViewSet, 'choices_turbid_types')
router.register(r'utility/choices_envo_materials', EnvoMaterialsChoicesViewSet, 'choices_envo_materials')
router.register(r'utility/choices_measure_modes', MeasureModesChoicesViewSet, 'choices_measure_modes')
router.register(r'utility/choices_env_instruments', EnvInstrumentsChoicesViewSet, 'choices_env_instruments')
router.register(r'utility/choices_ysi_models', YsiModelsChoicesViewSet, 'choices_ysi_models')
router.register(r'utility/choices_env_measurements', EnvMeasurementsChoicesViewSet, 'choices_env_measurements')
router.register(r'utility/choices_bottom_substrates', BottomSubstratesChoicesViewSet, 'choices_bottom_substrates')
router.register(r'utility/choices_water_collection_modes', WaterCollectionModesChoicesViewSet, 'choices_water_collection_modes')
router.register(r'utility/choices_collection_types', CollectionTypesChoicesViewSet, 'choices_collection_types')
router.register(r'utility/choices_filter_locations', FilterLocationsChoicesViewSet, 'choices_filter_locations')
router.register(r'utility/choices_control_types', ControlTypesChoicesViewSet, 'choices_control_types')
router.register(r'utility/choices_filter_methods', FilterMethodsChoicesViewSet, 'choices_filter_methods')
router.register(r'utility/choices_filter_types', FilterTypesChoicesViewSet, 'choices_filter_types')
router.register(r'utility/choices_core_methods', CoreMethodsChoicesViewSet, 'choices_core_methods')
router.register(r'utility/choices_subcore_methods', SubCoreMethodsChoicesViewSet, 'choices_subcore_methods')
router.register(r'utility/choices_target_genes', TargetGenesChoicesViewSet, 'choices_target_genes')
router.register(r'utility/choices_subfragment', SubFragmentsChoicesViewSet, 'choices_subfragment')
router.register(r'utility/choices_pcr_types', PcrTypesChoicesViewSet, 'choices_pcr_types')
router.register(r'utility/choices_lib_layouts', LibLayoutsChoicesViewSet, 'choices_lib_layouts')
router.register(r'utility/choices_lib_prep_types', LibPrepTypesChoicesViewSet, 'choices_lib_prep_types')
router.register(r'utility/choices_lib_prep_kits', LibPrepKitsChoicesViewSet, 'choices_lib_prep_kits')
router.register(r'utility/choices_seq_methods', SeqMethodsChoicesViewSet, 'choices_seq_methods')
router.register(r'utility/choices_investigation_types', InvestigationTypesChoicesViewSet, 'choices_investigation_types')
router.register(r'utility/choices_inv_status', InvStatusChoicesViewSet, 'choices_inv_status')
router.register(r'utility/choices_inv_loc_status', InvLocStatusChoicesViewSet, 'choices_inv_loc_status')
router.register(r'utility/choices_inv_types', InvTypesChoicesViewSet, 'choices_inv_types')
router.register(r'utility/choices_checkout_actions', CheckoutActionsChoicesViewSet, 'choices_checkout_actions')
# field_sites
router.register(r'field_sites/envo_biome_first', EnvoBiomeFirstViewSet, 'envo_biome_first')
router.register(r'field_sites/envo_biome_second', EnvoBiomeSecondViewSet, 'envo_biome_second')
router.register(r'field_sites/envo_biome_third', EnvoBiomeThirdViewSet, 'envo_biome_third')
router.register(r'field_sites/envo_biome_fourth', EnvoBiomeFourthViewSet, 'envo_biome_fourth')
router.register(r'field_sites/envo_biome_fifth', EnvoBiomeFifthViewSet, 'envo_biome_fifth')
router.register(r'field_sites/envo_feature_first', EnvoFeatureFirstViewSet, 'envo_feature_first')
router.register(r'field_sites/envo_feature_second', EnvoFeatureSecondViewSet, 'envo_feature_second')
router.register(r'field_sites/envo_feature_third', EnvoFeatureThirdViewSet, 'envo_feature_third')
router.register(r'field_sites/envo_feature_fourth', EnvoFeatureFourthViewSet, 'envo_feature_fourth')
router.register(r'field_sites/envo_feature_fifth', EnvoFeatureFifthViewSet, 'envo_feature_fifth')
router.register(r'field_sites/envo_feature_sixth', EnvoFeatureSixthViewSet, 'envo_feature_sixth')
router.register(r'field_sites/envo_feature_seventh', EnvoFeatureSeventhViewSet, 'envo_feature_seventh')
router.register(r'field_sites/system', SystemViewSet, 'system')
router.register(r'field_sites/watershed', GeoWatershedViewSet, 'watershed')
router.register(r'field_sites/field_site', GeoFieldSitesViewSet, 'field_site')
# sample_labels
router.register(r'sample_labels/sample_type', SampleTypeViewSet, 'sample_type')
router.register(r'sample_labels/sample_material', SampleMaterialViewSet, 'sample_material')
router.register(r'sample_labels/sample_label_req', SampleLabelRequestViewSet, 'sample_label_req')
router.register(r'sample_labels/sample_barcode', SampleBarcodeViewSet, 'sample_barcode')
# field_survey:post-transform
router.register(r'field_survey/field_survey', GeoFieldSurveyViewSet, 'field_survey')
router.register(r'field_survey/field_crew', FieldCrewViewSet, 'field_crew')
router.register(r'field_survey/env_measurement', EnvMeasurementViewSet, 'env_measurement')
router.register(r'field_survey/field_collection', FieldCollectionViewSet, 'field_collection')
router.register(r'field_survey/water_collection', WaterCollectionViewSet, 'water_collection')
router.register(r'field_survey/sediment_collection', SedimentCollectionViewSet, 'sediment_collection')
router.register(r'field_survey/field_sample', FieldSampleViewSet, 'field_sample')
router.register(r'field_survey/filter_sample', FilterSampleViewSet, 'filter_sample')
router.register(r'field_survey/subcore_sample', SubCoreSampleViewSet, 'subcore_sample')
router.register(r'field_survey/survey_filters', FieldSurveyFiltersNestedViewSet, 'survey_filters')
router.register(r'field_survey/survey_subcores', FieldSurveySubCoresNestedViewSet, 'survey_subcores')
# field_survey:pre-transform
router.register(r'field_survey/field_survey_etl', GeoFieldSurveyETLViewSet, 'field_survey_etl')
router.register(r'field_survey/field_crew_etl', FieldCrewETLViewSet, 'field_crew_etl')
router.register(r'field_survey/env_measurement_etl', EnvMeasurementETLViewSet, 'env_measurement_etl')
router.register(r'field_survey/field_collection_etl', FieldCollectionETLViewSet, 'field_collection_etl')
router.register(r'field_survey/sample_filter_etl', SampleFilterETLViewSet, 'sample_filter_etl')
# wet_lab
router.register(r'wet_lab/primer_pair', PrimerPairViewSet, 'primer_pair')
router.register(r'wet_lab/index_pair', IndexPairViewSet, 'index_pair')
router.register(r'wet_lab/index_removal_method', IndexRemovalMethodViewSet, 'index_removal_method')
router.register(r'wet_lab/size_selection_method', SizeSelectionMethodViewSet, 'size_selection_method')
router.register(r'wet_lab/quant_method', QuantificationMethodViewSet, 'quant_method')
router.register(r'wet_lab/amplification_method', AmplificationMethodViewSet, 'amplification_method')
router.register(r'wet_lab/extraction_method', ExtractionMethodViewSet, 'extraction_method')
router.register(r'wet_lab/extraction', ExtractionViewSet, 'extraction')
router.register(r'wet_lab/pcr_replicate', PcrReplicateViewSet, 'pcr_replicate')
router.register(r'wet_lab/pcr', PcrViewSet, 'pcr')
router.register(r'wet_lab/lib_prep', LibraryPrepViewSet, 'lib_prep')
router.register(r'wet_lab/pooled_lib', PooledLibraryViewSet, 'pooled_lib')
router.register(r'wet_lab/run_prep', RunPrepViewSet, 'run_prep')
router.register(r'wet_lab/run_result', RunResultViewSet, 'run_result')
router.register(r'wet_lab/fastq', FastqFileViewSet, 'fastq')
# freezer_inventory
router.register(r'freezer_inventory/return_action', ReturnActionViewSet, 'return_action')
router.register(r'freezer_inventory/freezer', FreezerViewSet, 'freezer')
router.register(r'freezer_inventory/rack', FreezerRackViewSet, 'rack')
router.register(r'freezer_inventory/box', FreezerBoxViewSet, 'box')
router.register(r'freezer_inventory/inventory', FreezerInventoryViewSet, 'inventory')
router.register(r'freezer_inventory/log', FreezerInventoryLogViewSet, 'log')
router.register(r'freezer_inventory/return_metadata', FreezerInventoryReturnMetadataViewSet, 'return_metadata')
router.register(r'freezer_inventory/inventory_location', FreezerInventoryLocNestedViewSet, 'inventory_location')
router.register(r'freezer_inventory/inventory_logs', FreezerInventoryLogsNestedViewSet, 'inventory_logs')
router.register(r'freezer_inventory/inventory_returns', FreezerInventoryReturnsNestedViewSet, 'inventory_returns')
# bioinfo_denoclust
router.register(r'bioinfo/quality_metadata', QualityMetadataViewSet, 'quality_metadata')
router.register(r'bioinfo/denoisecluster_method', DenoiseClusterMethodViewSet, 'denoisecluster_method')
router.register(r'bioinfo/denoisecluster_metadata', DenoiseClusterMetadataViewSet, 'denoisecluster_metadata')
router.register(r'bioinfo/feature', FeatureOutputViewSet, 'feature')
router.register(r'bioinfo/feature_read', FeatureReadViewSet, 'feature_read')
# bioinfo_taxon
router.register(r'bioinfo/refdb', ReferenceDatabaseViewSet, 'refdb')
router.register(r'bioinfo/domain', TaxonDomainViewSet, 'domain')
router.register(r'bioinfo/kingdom', TaxonKingdomViewSet, 'kingdom')
router.register(r'bioinfo/phylum', TaxonPhylumViewSet, 'phylum')
router.register(r'bioinfo/class', TaxonClassViewSet, 'class')
router.register(r'bioinfo/order', TaxonOrderViewSet, 'order')
router.register(r'bioinfo/family', TaxonFamilyViewSet, 'family')
router.register(r'bioinfo/genus', TaxonGenusViewSet, 'genus')
router.register(r'bioinfo/species', TaxonSpeciesViewSet, 'species')
router.register(r'bioinfo/annotation_method', AnnotationMethodViewSet, 'annotation_method')
router.register(r'bioinfo/annotation_metadata', AnnotationMetadataViewSet, 'annotation_metadata')
router.register(r'bioinfo/taxon_annotation', TaxonomicAnnotationViewSet, 'taxon_annotation')


urlpatterns = [
    # admin urls
    path('admin/', admin.site.urls),
    # API router
    path('api/', include(router.urls)),
    # allauth urls
    re_path(r'^account/', include('allauth.urls')),
    re_path(r'^account/disabled/signup/', signup, name='account_signup'), # re-registering signup to change url
    re_path(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),  # allauth email confirmation
    # dj-rest-auth urls - https://dj-rest-auth.readthedocs.io/en/latest/api_endpoints.html
    re_path(r'^rest-auth/login/$', users_views.CustomLoginView.as_view(), name='rest_login'),
    re_path(r'^rest-auth/', include('dj_rest_auth.urls')),
    re_path(r'^rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    re_path(r'^rest-auth/account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    # url(r'^rest-auth/registration/google/', GoogleLogin.as_view(), name='google_login')
    # drf-yasg urls
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
