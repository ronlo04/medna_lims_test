from django import forms
from django_filters import rest_framework as filters
from field_site.models import FieldSite
from users.models import CustomUser
from utility.models import Project
from utility.widgets import CustomSelect2Multiple, CustomSelect2
from .models import FieldSurvey, FieldCrew, EnvMeasureType, EnvMeasurement, \
    FieldCollection, WaterCollection, SedimentCollection, \
    FieldSample, FilterSample, SubCoreSample


########################################
# FRONTEND - FILTERS                   #
########################################
class GeoFieldSurveyMapFilter(filters.FilterSet):
    pk = filters.CharFilter(field_name='project_ids', lookup_expr='iexact')

    class Meta:
        model = FieldSurvey
        fields = ['project_ids', ]


class FieldSurveyFilter(filters.FilterSet):
    project_ids = filters.ModelMultipleChoiceFilter(field_name='project_ids__project_label', queryset=Project.objects.all(), widget=CustomSelect2Multiple, label='Project')
    site_id = filters.ModelChoiceFilter(field_name='site_id__site_id', queryset=FieldSite.objects.all(), widget=CustomSelect2, label='Site ID')
    username = filters.ModelChoiceFilter(field_name='username__agol_username', queryset=CustomUser.objects.all(), widget=CustomSelect2, label='Username')
    supervisor = filters.ModelChoiceFilter(field_name='supervisor__agol_username', queryset=CustomUser.objects.all(), widget=CustomSelect2, label='Supervisor')
    water_filterer = filters.ModelChoiceFilter(field_name='water_filterer__agol_username', queryset=CustomUser.objects.all(), widget=CustomSelect2, label='Water Filterer')
    survey_datetime = filters.DateFilter(input_formats=['%Y-%m-%d', '%d-%m-%Y'], lookup_expr='icontains', widget=forms.SelectDateWidget(attrs={'class': 'form-control', }), label='Survey DateTime')

    class Meta:
        model = FieldSurvey
        fields = ['username', 'supervisor', 'survey_datetime', 'site_id', 'project_ids', ]


class FieldCrewFilter(filters.FilterSet):
    survey_global_id = filters.ModelChoiceFilter(field_name='survey_global_id__survey_global_id', queryset=FieldSurvey.objects.all(), widget=CustomSelect2, label='Survey Global ID')
    created_datetime = filters.DateFilter(input_formats=['%Y-%m-%d', '%d-%m-%Y'], lookup_expr='icontains', widget=forms.SelectDateWidget(attrs={'class': 'form-control', }), label='Created DateTime')
    created_by = filters.ModelChoiceFilter(field_name='username__email', queryset=CustomUser.objects.all(), widget=CustomSelect2, label='Created By')

    class Meta:
        model = FieldSurvey
        fields = ['survey_global_id', 'created_datetime', 'created_by', ]


class EnvMeasurementFilter(filters.FilterSet):
    survey_global_id = filters.ModelChoiceFilter(field_name='survey_global_id__survey_global_id', queryset=FieldSurvey.objects.all(), widget=CustomSelect2, label='Survey Global ID')
    env_measure_datetime = filters.DateFilter(input_formats=['%Y-%m-%d', '%d-%m-%Y'], lookup_expr='icontains', widget=forms.SelectDateWidget(attrs={'class': 'form-control', }), label='Created DateTime')
    created_by = filters.ModelChoiceFilter(field_name='username__email', queryset=CustomUser.objects.all(), widget=CustomSelect2, label='Created By')

    class Meta:
        model = EnvMeasurement
        fields = ['survey_global_id', 'env_measure_datetime', 'created_by', ]


class WaterCollectionFilter(filters.FilterSet):
    survey_global_id = filters.ModelChoiceFilter(field_name='field_collection__survey_global_id', queryset=FieldSurvey.objects.all(), widget=CustomSelect2, label='Survey Global ID')
    water_collect_datetime = filters.DateFilter(input_formats=['%Y-%m-%d', '%d-%m-%Y'], lookup_expr='icontains', widget=forms.SelectDateWidget(attrs={'class': 'form-control', }), label='Collected DateTime')
    created_by = filters.ModelChoiceFilter(field_name='username__email', queryset=CustomUser.objects.all(), widget=CustomSelect2, label='Created By')

    class Meta:
        model = WaterCollection
        fields = ['survey_global_id', 'water_collect_datetime', 'created_by', ]


class SedimentCollectionFilter(filters.FilterSet):
    survey_global_id = filters.ModelChoiceFilter(field_name='field_collection__survey_global_id', queryset=FieldSurvey.objects.all(), widget=CustomSelect2, label='Survey Global ID')
    core_datetime_start = filters.DateFilter(input_formats=['%Y-%m-%d', '%d-%m-%Y'], lookup_expr='icontains', widget=forms.SelectDateWidget(attrs={'class': 'form-control', }), label='Collected DateTime')
    created_by = filters.ModelChoiceFilter(field_name='username__email', queryset=CustomUser.objects.all(), widget=CustomSelect2, label='Created By')

    class Meta:
        model = WaterCollection
        fields = ['survey_global_id', 'core_datetime_start', 'created_by', ]


class FilterSampleFilter(filters.FilterSet):
    project_ids = filters.ModelMultipleChoiceFilter(field_name='field_sample__collection_global_id__survey_global_id__project_ids__project_label', queryset=Project.objects.all(), widget=CustomSelect2Multiple, label='Project')
    site_id = filters.ModelChoiceFilter(field_name='field_sample__collection_global_id__survey_global_id__site_id__site_id', queryset=FieldSite.objects.all(), widget=CustomSelect2, label='Site ID')
    username = filters.ModelChoiceFilter(field_name='field_sample__collection_global_id__survey_global_id__username__agol_username', queryset=CustomUser.objects.all(), widget=CustomSelect2, label='Username')
    supervisor = filters.ModelChoiceFilter(field_name='field_sample__collection_global_id__survey_global_id__supervisor__agol_username', queryset=CustomUser.objects.all(), widget=CustomSelect2, label='Supervisor')
    filter_datetime = filters.DateFilter(input_formats=['%Y-%m-%d', '%d-%m-%Y'], lookup_expr='icontains', widget=forms.SelectDateWidget(attrs={'class': 'form-control', }), label='Filter DateTime')
    field_sample_barcode = filters.ModelChoiceFilter(field_name='field_sample__field_sample_barcode__barcode_slug', queryset=FieldSample.objects.all(), widget=CustomSelect2, label='Barcode')

    class Meta:
        model = FieldSurvey
        fields = ['username', 'supervisor', 'filter_datetime', 'site_id', 'project_ids', 'field_sample_barcode', ]


class SubCoreSampleFilter(filters.FilterSet):
    project_ids = filters.ModelMultipleChoiceFilter(field_name='field_sample__collection_global_id__survey_global_id__project_ids__project_label', queryset=Project.objects.all(), widget=CustomSelect2Multiple, label='Project')
    site_id = filters.ModelChoiceFilter(field_name='field_sample__collection_global_id__survey_global_id__site_id__site_id', queryset=FieldSite.objects.all(), widget=CustomSelect2, label='Site ID')
    username = filters.ModelChoiceFilter(field_name='field_sample__collection_global_id__survey_global_id__username__agol_username', queryset=CustomUser.objects.all(), widget=CustomSelect2, label='Username')
    supervisor = filters.ModelChoiceFilter(field_name='field_sample__collection_global_id__survey_global_id__supervisor__agol_username', queryset=CustomUser.objects.all(), widget=CustomSelect2, label='Supervisor')
    subcore_datetime_start = filters.DateFilter(input_formats=['%Y-%m-%d', '%d-%m-%Y'], lookup_expr='icontains', widget=forms.SelectDateWidget(attrs={'class': 'form-control', }), label='SubCore DateTime')
    field_sample_barcode = filters.ModelChoiceFilter(field_name='field_sample__field_sample_barcode__barcode_slug', queryset=FieldSample.objects.all(), widget=CustomSelect2, label='Barcode')

    class Meta:
        model = FieldSurvey
        fields = ['username', 'supervisor', 'subcore_datetime_start', 'site_id', 'project_ids', 'field_sample_barcode', ]


########################################
# SERIALIZER FILTERS                   #
########################################
class GeoFieldSurveySerializerFilter(filters.FilterSet):
    created_by = filters.CharFilter(field_name='created_by__email', lookup_expr='iexact')
    project_ids = filters.CharFilter(field_name='project_ids__project_code', lookup_expr='iexact')
    site_id = filters.CharFilter(field_name='site_id__site_id', lookup_expr='iexact')
    username = filters.CharFilter(field_name='username__email', lookup_expr='iexact')
    supervisor = filters.CharFilter(field_name='supervisor__email', lookup_expr='iexact')
    qa_editor = filters.CharFilter(field_name='qa_editor__email', lookup_expr='iexact')
    survey_datetime = filters.DateFilter(input_formats=['%m-%d-%Y'], lookup_expr='icontains')

    class Meta:
        model = FieldSurvey
        fields = ['created_by', 'project_ids', 'site_id', 'username', 'supervisor', 'qa_editor', 'survey_datetime']


class FieldCrewSerializerFilter(filters.FilterSet):
    created_by = filters.CharFilter(field_name='created_by__email', lookup_expr='iexact')
    survey_global_id = filters.CharFilter(field_name='survey_global_id__survey_global_id', lookup_expr='iexact')

    class Meta:
        model = FieldCrew
        fields = ['created_by', 'survey_global_id', ]


class EnvMeasureTypeSerializerFilter(filters.FilterSet):
    env_measure_type_code = filters.CharFilter(field_name='env_measure_type_code', lookup_expr='iexact')

    class Meta:
        model = EnvMeasureType
        fields = ['env_measure_type_code']


class EnvMeasurementSerializerFilter(filters.FilterSet):
    created_by = filters.CharFilter(field_name='created_by__email', lookup_expr='iexact')
    survey_global_id = filters.CharFilter(field_name='survey_global_id__survey_global_id', lookup_expr='iexact')
    env_measurement = filters.CharFilter(field_name='env_measurement__env_measure_type_code', lookup_expr='iexact')

    class Meta:
        model = EnvMeasurement
        fields = ['created_by', 'survey_global_id', ]


class FieldCollectionSerializerFilter(filters.FilterSet):
    created_by = filters.CharFilter(field_name='created_by__email', lookup_expr='iexact')
    survey_global_id = filters.CharFilter(field_name='survey_global_id__survey_global_id', lookup_expr='iexact')
    collection_type = filters.CharFilter(field_name='collection_type', lookup_expr='iexact')

    class Meta:
        model = FieldCollection
        fields = ['created_by', 'survey_global_id', 'collection_type']


class WaterCollectionSerializerFilter(filters.FilterSet):
    created_by = filters.CharFilter(field_name='created_by__email', lookup_expr='iexact')
    water_control = filters.CharFilter(field_name='water_control', lookup_expr='iexact')
    water_vessel_label = filters.CharFilter(field_name='water_vessel_label', lookup_expr='iexact')
    was_filtered = filters.CharFilter(field_name='was_filtered', lookup_expr='iexact')

    class Meta:
        model = WaterCollection
        fields = ['created_by', 'water_control', 'water_vessel_label', 'was_filtered']


class SedimentCollectionSerializerFilter(filters.FilterSet):
    created_by = filters.CharFilter(field_name='created_by__email', lookup_expr='iexact')
    core_control = filters.CharFilter(field_name='core_control', lookup_expr='iexact')
    core_label = filters.CharFilter(field_name='core_label', lookup_expr='iexact')
    subcores_taken = filters.CharFilter(field_name='subcores_taken', lookup_expr='iexact')

    class Meta:
        model = SedimentCollection
        fields = ['created_by', 'core_control', 'core_label', 'subcores_taken']


class FieldSampleSerializerFilter(filters.FilterSet):
    created_by = filters.CharFilter(field_name='created_by__email', lookup_expr='iexact')
    collection_global_id = filters.CharFilter(field_name='collection_global_id__collection_global_id', lookup_expr='iexact')
    sample_material = filters.CharFilter(field_name='sample_material__sample_material_code', lookup_expr='iexact')
    is_extracted = filters.CharFilter(field_name='is_extracted', lookup_expr='iexact')
    barcode_slug = filters.CharFilter(field_name='barcode_slug', lookup_expr='iexact')

    class Meta:
        model = FieldSample
        fields = ['created_by', 'collection_global_id', 'sample_material',
                  'is_extracted', 'barcode_slug']


class FilterSampleSerializerFilter(filters.FilterSet):
    created_by = filters.CharFilter(field_name='created_by__email', lookup_expr='iexact')

    class Meta:
        model = FilterSample
        fields = ['created_by', ]


class SubCoreSampleSerializerFilter(filters.FilterSet):
    created_by = filters.CharFilter(field_name='created_by__email', lookup_expr='iexact')

    class Meta:
        model = SubCoreSample
        fields = ['created_by', 'field_sample', ]


class FilterJoinSerializerFilter(filters.FilterSet):
    field_sample = filters.CharFilter(field_name='field_sample__field_sample_barcode', lookup_expr='iexact')

    class Meta:
        model = SubCoreSample
        fields = ['created_by', 'field_sample', ]


########################################
# SERIALIZERS - NESTED FILTERS         #
########################################
class FieldSurveyEnvsNestedSerializerFilter(filters.FilterSet):
    # project_ids = filters.CharFilter(field_name='project_ids__project_code', lookup_expr='iexact')
    site_id = filters.CharFilter(field_name='site_id__site_id', lookup_expr='iexact')
    username = filters.CharFilter(field_name='username__email', lookup_expr='iexact')
    supervisor = filters.CharFilter(field_name='supervisor__email', lookup_expr='iexact')
    survey_datetime = filters.DateFilter(input_formats=['%m-%d-%Y'], lookup_expr='icontains')
    field_sample_barcode = filters.CharFilter(field_name='field_collections__field_samples__barcode_slug', lookup_expr='iexact')
    env_measure_type = filters.CharFilter(field_name='env_measurements__env_measurement__env_measure_type_code', lookup_expr='iexact')

    class Meta:
        model = FieldSurvey
        fields = ['site_id', 'username', 'supervisor', 'survey_datetime', 'field_collections']


class FieldSurveyFiltersNestedSerializerFilter(filters.FilterSet):
    # project_ids = filters.CharFilter(field_name='project_ids__project_code', lookup_expr='iexact')
    site_id = filters.CharFilter(field_name='site_id__site_id', lookup_expr='iexact')
    username = filters.CharFilter(field_name='username__email', lookup_expr='iexact')
    supervisor = filters.CharFilter(field_name='supervisor__email', lookup_expr='iexact')
    survey_datetime = filters.DateFilter(input_formats=['%m-%d-%Y'], lookup_expr='icontains')
    field_sample_barcode = filters.CharFilter(field_name='field_collections__field_samples__barcode_slug', lookup_expr='iexact')

    class Meta:
        model = FieldSurvey
        fields = ['site_id', 'username', 'supervisor', 'survey_datetime', 'field_collections']


class FieldSurveySubCoresNestedSerializerFilter(filters.FilterSet):
    # project_ids = filters.CharFilter(field_name='project_ids__project_code', lookup_expr='iexact')
    site_id = filters.CharFilter(field_name='site_id__site_id', lookup_expr='iexact')
    username = filters.CharFilter(field_name='username__email', lookup_expr='iexact')
    supervisor = filters.CharFilter(field_name='supervisor__email', lookup_expr='iexact')
    survey_datetime = filters.DateFilter(input_formats=['%m-%d-%Y'], lookup_expr='icontains')
    field_sample_barcode = filters.CharFilter(field_name='field_collections__field_samples__barcode_slug', lookup_expr='iexact')

    class Meta:
        model = FieldSurvey
        fields = ['site_id', 'username', 'supervisor', 'survey_datetime', 'field_collections']
