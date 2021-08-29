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
from allauth.account.views import confirm_email, signup, login, logout, password_change, \
    password_set, account_inactive, email, email_verification_sent, password_reset, \
    password_reset_done, password_reset_from_key, password_reset_from_key_done
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from users.views import CustomUserViewSet
from field_sites.views import EnvoBiomeFirstViewSet, EnvoBiomeSecondViewSet, EnvoBiomeThirdViewSet, \
    EnvoBiomeFourthViewSet, EnvoBiomeFifthViewSet, \
    EnvoFeatureFirstViewSet, EnvoFeatureSecondViewSet, EnvoFeatureThirdViewSet, EnvoFeatureFourthViewSet, \
    EnvoFeatureFifthViewSet, EnvoFeatureSixthViewSet, EnvoFeatureSeventhViewSet, SystemViewSet, FieldSitesViewSet
from sample_labels.views import SampleTypeViewSet, SampleLabelRequestViewSet, SampleLabelViewSet
from field_survey.views import FieldSurveyViewSet, FieldCrewViewSet, EnvMeasurementViewSet, FieldCollectionViewSet, \
    FieldSampleViewSet
from wet_lab.views import PrimerPairViewSet, IndexPairViewSet, IndexRemovalMethodViewSet, SizeSelectionMethodViewSet, \
    QuantificationMethodViewSet, ExtractionMethodViewSet, ExtractionViewSet, DdpcrViewSet, QpcrViewSet, \
    LibraryPrepViewSet, PooledLibraryViewSet, FinalPooledLibraryViewSet, RunPrepViewSet, RunResultViewSet, \
    FastqFileViewSet
from freezer_inventory.views import FreezerViewSet, FreezerRackViewSet, FreezerBoxViewSet, \
    FreezerInventoryViewSet, FreezerCheckoutViewSet
from bioinfo_denoising.views import DenoisingMethodViewSet, DenoisingMetadataViewSet, \
    AmpliconSequenceVariantViewSet, ASVReadViewSet
from bioinfo_taxon.views import ReferenceDatabaseViewSet, \
    TaxonDomainViewSet, TaxonKingdomViewSet, TaxonPhylumViewSet, \
    TaxonClassViewSet, TaxonOrderViewSet, TaxonFamilyViewSet, \
    TaxonGenusViewSet, TaxonSpeciesViewSet, \
    AnnotationMethodViewSet, AnnotationMetadataViewSet, TaxonomicAnnotationViewSet
from utility.views import GrantViewSet, ProjectViewSet, ProcessLocationViewSet, YesNoChoicesViewSet, \
    MeasureUnitsChoicesViewSet, VolUnitsChoicesViewSet, ConcentrationUnitsChoicesViewSet, \
    PhiXConcentrationUnitsChoicesViewSet, DdpcrUnitsChoicesViewSet, QpcrUnitsChoicesViewSet, \
    WindSpeedsChoicesViewSet, CloudCoversChoicesViewSet, PrecipTypesChoicesViewSet, \
    TurbidTypesChoicesViewSet, EnvoMaterialsChoicesViewSet, MeasureModesChoicesViewSet, \
    EnvInstrumentsChoicesViewSet, YsiModelsChoicesViewSet, EnvMeasurementsChoicesViewSet, \
    BottomSubstratesChoicesViewSet, WaterCollectionModesChoicesViewSet, CollectionTypesChoicesViewSet, \
    FilterLocationsChoicesViewSet, ControlTypesChoicesViewSet, FilterMethodsChoicesViewSet, \
    FilterTypesChoicesViewSet, CoreMethodsChoicesViewSet, SubCoreMethodsChoicesViewSet, \
    TargetGenesChoicesViewSet, LibPrepTypesChoicesViewSet, LibPrepKitsChoicesViewSet, \
    InvStatusChoicesViewSet, InvTypesChoicesViewSet, CheckoutActionsChoicesViewSet

router = routers.DefaultRouter()
# users
router.register(r'choices_yes_no', YesNoChoicesViewSet, 'choices_yes_no')
router.register(r'choices_measure_units', MeasureUnitsChoicesViewSet, 'choices_measure_units')
router.register(r'choices_vol_units', VolUnitsChoicesViewSet, 'choices_vol_units')
router.register(r'choices_concentration_units', ConcentrationUnitsChoicesViewSet, 'choices_concentration_units')
router.register(r'choices_phix_concentration_units', PhiXConcentrationUnitsChoicesViewSet, 'choices_phix_concentration_units')
router.register(r'choices_ddpcr_units', DdpcrUnitsChoicesViewSet, 'choices_ddpcr_units')
router.register(r'choices_qpcr_units', QpcrUnitsChoicesViewSet, 'choices_qpcr_units')
router.register(r'choices_wind_speeds', WindSpeedsChoicesViewSet, 'choices_wind_speeds')
router.register(r'choices_cloud_covers', CloudCoversChoicesViewSet, 'choices_cloud_covers')
router.register(r'choices_precip_types', PrecipTypesChoicesViewSet, 'choices_precip_types')
router.register(r'choices_turbid_types', TurbidTypesChoicesViewSet, 'choices_turbid_types')
router.register(r'choices_envo_materials', EnvoMaterialsChoicesViewSet, 'choices_envo_materials')
router.register(r'choices_measure_modes', MeasureModesChoicesViewSet, 'choices_measure_modes')
router.register(r'choices_env_instruments', EnvInstrumentsChoicesViewSet, 'choices_env_instruments')
router.register(r'choices_ysi_models', YsiModelsChoicesViewSet, 'choices_ysi_models')
router.register(r'choices_env_measurements', EnvMeasurementsChoicesViewSet, 'choices_env_measurements')
router.register(r'choices_bottom_substrates', BottomSubstratesChoicesViewSet, 'choices_bottom_substrates')
router.register(r'choices_water_collection_modes', WaterCollectionModesChoicesViewSet, 'choices_water_collection_modes')
router.register(r'choices_collection_types', CollectionTypesChoicesViewSet, 'choices_collection_types')
router.register(r'choices_filter_locations', FilterLocationsChoicesViewSet, 'choices_filter_locations')
router.register(r'choices_control_types', ControlTypesChoicesViewSet, 'choices_control_types')
router.register(r'choices_filter_methods', FilterMethodsChoicesViewSet, 'choices_filter_methods')
router.register(r'choices_filter_types', FilterTypesChoicesViewSet, 'choices_filter_types')
router.register(r'choices_core_methods', CoreMethodsChoicesViewSet, 'choices_core_methods')
router.register(r'choices_subcore_methods', SubCoreMethodsChoicesViewSet, 'choices_subcore_methods')
router.register(r'choices_target_genes', TargetGenesChoicesViewSet, 'choices_target_genes')
router.register(r'choices_lib_prep_types', LibPrepTypesChoicesViewSet, 'choices_lib_prep_types')
router.register(r'choices_lib_prep_kits', LibPrepKitsChoicesViewSet, 'choices_lib_prep_kits')
router.register(r'choices_inv_status', InvStatusChoicesViewSet, 'choices_inv_status')
router.register(r'choices_inv_types', InvTypesChoicesViewSet, 'choices_inv_types')
router.register(r'choices_checkout_actions', CheckoutActionsChoicesViewSet, 'choices_checkout_actions')

router.register(r'users', CustomUserViewSet, 'users')
# utility
router.register(r'grant', GrantViewSet, 'grant')
router.register(r'project', ProjectViewSet, 'project')
router.register(r'process_location', ProcessLocationViewSet, 'process_location')
# field sites
router.register(r'envo_biome_first', EnvoBiomeFirstViewSet, 'envo_biome_first')
router.register(r'envo_biome_second', EnvoBiomeSecondViewSet, 'envo_biome_second')
router.register(r'envo_biome_third', EnvoBiomeThirdViewSet, 'envo_biome_third')
router.register(r'envo_biome_fourth', EnvoBiomeFourthViewSet, 'envo_biome_fourth')
router.register(r'envo_biome_fifth', EnvoBiomeFifthViewSet, 'envo_biome_fifth')
router.register(r'envo_feature_first', EnvoFeatureFirstViewSet, 'envo_feature_first')
router.register(r'envo_feature_second', EnvoFeatureSecondViewSet, 'envo_feature_second')
router.register(r'envo_feature_third', EnvoFeatureThirdViewSet, 'envo_feature_third')
router.register(r'envo_feature_fourth', EnvoFeatureFourthViewSet, 'envo_feature_fourth')
router.register(r'envo_feature_fifth', EnvoFeatureFifthViewSet, 'envo_feature_fifth')
router.register(r'envo_feature_sixth', EnvoFeatureSixthViewSet, 'envo_feature_sixth')
router.register(r'envo_feature_seventh', EnvoFeatureSeventhViewSet, 'envo_feature_seventh')
router.register(r'system', SystemViewSet, 'system')
router.register(r'field_site', FieldSitesViewSet, 'field_site')
# sample_labels
router.register(r'sample_type', SampleTypeViewSet, 'sample_type')
router.register(r'sample_label_req', SampleLabelRequestViewSet, 'sample_label_req')
router.register(r'sample_label', SampleLabelViewSet, 'sample_label')
# field_survey
router.register(r'field_survey', FieldSurveyViewSet, 'field_survey')
router.register(r'field_crew', FieldCrewViewSet, 'field_crew')
router.register(r'env_measurement', EnvMeasurementViewSet, 'env_measurement')
router.register(r'field_collection', FieldCollectionViewSet, 'field_collection')
router.register(r'field_sample', FieldSampleViewSet, 'field_sample')
# wet_lab
router.register(r'primer_pair', PrimerPairViewSet, 'primer_pair')
router.register(r'index_pair', IndexPairViewSet, 'index_pair')
router.register(r'index_removal_method', IndexRemovalMethodViewSet, 'index_removal_method')
router.register(r'size_selection_method', SizeSelectionMethodViewSet, 'size_selection_method')
router.register(r'quant_method', QuantificationMethodViewSet, 'quant_method')
router.register(r'extraction_method', ExtractionMethodViewSet, 'extraction_method')
router.register(r'extraction', ExtractionViewSet, 'extraction')
router.register(r'ddpcr', DdpcrViewSet, 'ddpcr')
router.register(r'qpcr', QpcrViewSet, 'qpcr')
router.register(r'lib_prep', LibraryPrepViewSet, 'lib_prep')
router.register(r'pooled_lib', PooledLibraryViewSet, 'pooled_lib')
router.register(r'final_pooled_lib', FinalPooledLibraryViewSet, 'final_pooled_lib')
router.register(r'run_prep', RunPrepViewSet, 'run_prep')
router.register(r'run_result', RunResultViewSet, 'run_result')
router.register(r'fastq', FastqFileViewSet, 'fastq')
# freezer_inventory
router.register(r'freezer', FreezerViewSet, 'freezer')
router.register(r'rack', FreezerRackViewSet, 'rack')
router.register(r'box', FreezerBoxViewSet, 'box')
router.register(r'inventory', FreezerInventoryViewSet, 'inventory')
router.register(r'checkout', FreezerCheckoutViewSet, 'checkout')
# bioinfo_denoising
router.register(r'denoising_method', DenoisingMethodViewSet, 'denoising_method')
router.register(r'denoising_metadata', DenoisingMetadataViewSet, 'denoising_metadata')
router.register(r'asv', AmpliconSequenceVariantViewSet, 'asv')
router.register(r'asv_read', ASVReadViewSet, 'asv_read')
# bioinfo_taxon
router.register(r'refdb', ReferenceDatabaseViewSet, 'refdb')
router.register(r'domain', TaxonDomainViewSet, 'domain')
router.register(r'kingdom', TaxonKingdomViewSet, 'kingdom')
router.register(r'phylum', TaxonPhylumViewSet, 'phylum')
router.register(r'class', TaxonClassViewSet, 'class')
router.register(r'order', TaxonOrderViewSet, 'order')
router.register(r'family', TaxonFamilyViewSet, 'family')
router.register(r'genus', TaxonGenusViewSet, 'genus')
router.register(r'species', TaxonSpeciesViewSet, 'species')
router.register(r'annotation_method', AnnotationMethodViewSet, 'annotation_method')
router.register(r'annotation_metadata', AnnotationMetadataViewSet, 'annotation_metadata')
router.register(r'taxon_annotation', TaxonomicAnnotationViewSet, 'taxon_annotation')


urlpatterns = [
    #path('', IndexView.as_view(), name='index'),
    # admin urls
    path('admin/', admin.site.urls),
    # API router
    path('api/', include(router.urls)),
    # rest_auth urls
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    # allauth urls - added all to remove signup url
    # url(r'^account/', include('allauth.urls')),
    url(r'^account/disabled/signup/', signup, name='account_signup'),
    url(r'^account/login/', login, name='account_login'),
    url(r'^account/logout/', logout, name='account_logout'),
    url(r'^account/password/change/', password_change, name='account_change_password',),
    url(r'^account/password/set/', password_set, name='account_set_password'),
    url(r'^account/inactive/', account_inactive, name='account_inactive'),
    # allauth E-mail
    url(r'^account/email/', email, name='account_email'),
    url(r'^account/confirm-email/', email_verification_sent,
        name='account_email_verification_sent',),
    # restauth and allauth email confirmation
    url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$',
        confirm_email, name='account_confirm_email'),
    # allauth password reset
    url(r'^account/password/reset/', password_reset, name='account_reset_password'),
    url(r'^account/password/reset/done/', password_reset_done,
        name='account_reset_password_done',),
    url(r'^account/password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$',
        password_reset_from_key,
        name='account_reset_password_from_key',),
    url(r'^account/password/reset/key/done/', password_reset_from_key_done,
        name='account_reset_password_from_key_done',),
]
