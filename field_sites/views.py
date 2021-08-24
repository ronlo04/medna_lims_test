from django.urls import reverse
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters import rest_framework as filters
# import datetime
from django.utils import timezone
from utility.serializers import SerializerExportMixin
from .models import EnvoBiomeFirst, EnvoBiomeSecond, EnvoBiomeThird, EnvoBiomeFourth, EnvoBiomeFifth, \
    EnvoFeatureFirst, EnvoFeatureSecond, EnvoFeatureThird, EnvoFeatureFourth, \
    EnvoFeatureFifth, EnvoFeatureSixth, EnvoFeatureSeventh, FieldSite, Region
# from django.shortcuts import render
# from django.http import HttpResponse
from django_filters.views import FilterView
from .tables import FieldSiteTable
from django_tables2.views import SingleTableMixin
# from django_tables2.paginators import LazyPaginator
from .serializers import EnvoBiomeFirstSerializer, EnvoBiomeSecondSerializer,\
    EnvoBiomeThirdSerializer, EnvoBiomeFourthSerializer, EnvoBiomeFifthSerializer,    \
    EnvoFeatureFirstSerializer, EnvoFeatureSecondSerializer,\
    EnvoFeatureThirdSerializer, EnvoFeatureFourthSerializer,\
    EnvoFeatureFifthSerializer, EnvoFeatureSixthSerializer,\
    EnvoFeatureSeventhSerializer, FieldSiteSerializer, GeoFieldSiteSerializer, \
    GeoRegionSerializer
import datetime
import csv
from django.http import HttpResponse
from rest_framework import generics
from rest_framework import viewsets
from .forms import AddFieldSiteForm


class EnvoBiomeFirstViewSet(viewsets.ModelViewSet):
    serializer_class = EnvoBiomeFirstSerializer
    queryset = EnvoBiomeFirst.objects.all()


class EnvoBiomeSecondViewSet(viewsets.ModelViewSet):
    serializer_class = EnvoBiomeSecondSerializer
    queryset = EnvoBiomeSecond.objects.all()


class EnvoBiomeThirdViewSet(viewsets.ModelViewSet):
    serializer_class = EnvoBiomeThirdSerializer
    queryset = EnvoBiomeThird.objects.all()


class EnvoBiomeFourthViewSet(viewsets.ModelViewSet):
    serializer_class = EnvoBiomeFourthSerializer
    queryset = EnvoBiomeFourth.objects.all()


class EnvoBiomeFifthViewSet(viewsets.ModelViewSet):
    serializer_class = EnvoBiomeFifthSerializer
    queryset = EnvoBiomeFifth.objects.all()


class EnvoFeatureFirstViewSet(viewsets.ModelViewSet):
    serializer_class = EnvoFeatureFirstSerializer
    queryset = EnvoFeatureFirst.objects.all()


class EnvoFeatureSecondViewSet(viewsets.ModelViewSet):
    serializer_class = EnvoFeatureSecondSerializer
    queryset = EnvoFeatureSecond.objects.all()


class EnvoFeatureThirdViewSet(viewsets.ModelViewSet):
    serializer_class = EnvoFeatureThirdSerializer
    queryset = EnvoFeatureThird.objects.all()


class EnvoFeatureFourthViewSet(viewsets.ModelViewSet):
    serializer_class = EnvoFeatureFourthSerializer
    queryset = EnvoFeatureFourth.objects.all()


class EnvoFeatureFifthViewSet(viewsets.ModelViewSet):
    serializer_class = EnvoFeatureFifthSerializer
    queryset = EnvoFeatureFifth.objects.all()


class EnvoFeatureSixthViewSet(viewsets.ModelViewSet):
    serializer_class = EnvoFeatureSixthSerializer
    queryset = EnvoFeatureSixth.objects.all()


class EnvoFeatureSeventhViewSet(viewsets.ModelViewSet):
    serializer_class = EnvoFeatureSeventhSerializer
    queryset = EnvoFeatureSeventh.objects.all()


class FieldSitesViewSet(viewsets.ModelViewSet):
    serializer_class = FieldSiteSerializer
    queryset = FieldSite.objects.all()


class FieldSitesFilterView(SerializerExportMixin, SingleTableMixin, FilterView):
    """View site filter view with REST serializser and django-tables2"""
    # export_formats = ['csv','xlsx'] # set in user_sites in default
    model = FieldSite
    table_class = FieldSiteTable
#    table_pagination = {
#        'paginator_class': LazyPaginator,
#    }
    export_name = 'site_' + str(timezone.now().replace(microsecond=0).isoformat())
    serializer_class = FieldSiteSerializer
    filter_backends = (filters.DjangoFilterBackend,)


class FieldSitesListView(generics.ListAPIView):
    queryset = FieldSite.objects.all()
    serializer_class = FieldSiteSerializer


class GeoFieldSitesListView(generics.ListAPIView):
    queryset = FieldSite.objects.all()
    serializer_class = GeoFieldSiteSerializer


class GeoRegionsListView(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = GeoRegionSerializer


class FieldSiteDetailView(DetailView):
    model = FieldSite
    context_object_name = 'site'
    fields = ['grant', 'system', 'region', 'general_location_name', 'purpose', 'geom',
              'created_by', 'created_datetime']

#    def get_object(self, queryset=None):
#        return queryset.get(self.kwargs['pk'])


class FieldSiteExportDetailView(DetailView):
    # this view is only for adding a button in SiteDetailView to download the single record...
    model = FieldSite
    context_object_name = 'site'

    def render_to_response(self, context, **response_kwargs):
        site = context.get('site')  # getting User object from context using context_object_name
        file_name = 'site'
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=' + file_name + str(
            timezone.now().replace(microsecond=0).isoformat()) + '.csv'
        writer = csv.writer(response)
        writer.writerow(['id','site_id', 'grant', 'system', 'region', 'general_location_name',
                         'purpose', 'lat', 'lon', 'srid', 'created_by', 'created_datetime'])
        writer.writerow([site.id, site.site_id, site.grant.grant_label, site.system.system_label,
                         site.region.region_label,
                         site.general_location_name, site.purpose, site.geom.y,
                         site.geom.x, site.geom.srid, site.created_by.email,site.created_datetime])
        return response


class AddFieldSiteView(LoginRequiredMixin,CreateView):
    # LoginRequiredMixin prevents users who aren’t logged in from accessing the form.
    # If you omit that, you’ll need to handle unauthorized users in form_valid().
    form_class = AddFieldSiteForm
    # model = Site
    # fields = ['grant', 'system', 'region', 'general_location_name', 'purpose', 'geom']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.created_datetime = timezone.now()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('users:site_detail', kwargs={"pk": self.object.pk})