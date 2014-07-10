"""URL mappings."""

from django.conf.urls import patterns, url
from django.views.i18n import javascript_catalog
from django.views.generic import View, ListView, TemplateView, DetailView

from .views import MainPageView, ScannerList, DomainList, RuleList
from .views import CSVReportDetails, ReportDetails, ReportList
from .views import ScannerCreate, ScannerUpdate, ScannerDelete, ScannerRun
from .views import DomainCreate, DomainUpdate, DomainValidate, DomainDelete
from .views import RuleCreate, RuleUpdate, RuleDelete
from .views import DialogSuccess
from .models import Scanner


js_info_dict = {
    'packages': ('os2webscanner', 'recurrence')
}

urlpatterns = patterns(
    '',
    # App URLs
    url(r'^$', MainPageView.as_view(), name='index'),
    url(r'^scanners/$', ScannerList.as_view(), name='scanners'),
    url(r'^scanners/add/$', ScannerCreate.as_view(), name='scanner_add'),
    url(r'^scanners/(?P<pk>\d+)/delete/$', ScannerDelete.as_view(),
        name='scanner_delete'),
    url(r'^scanners/(?P<pk>\d+)/run/$', ScannerRun.as_view(),
        name='scanner_run'),
    url(r'^scanners/(?P<pk>\d+)/askrun/$',
        DetailView.as_view(template_name='os2webscanner/scanner_askrun.html',
                           model=Scanner),
        name='scanner_askrun'),
    url(r'^scanners/(?P<pk>\d+)/$', ScannerUpdate.as_view(),
        name='scanner_update'),
    url(r'^domains/$', DomainList.as_view(), name='domains'),
    url(r'^domains/add/$', DomainCreate.as_view(), name='domain_add'),
    url(r'^domains/(?P<pk>\d+)/validate/$', DomainValidate.as_view(),
        name='domain_validate'),
    url(r'^(domains)/(\d+)/(success)/$', DialogSuccess.as_view()),
    url(r'^domains/(?P<pk>\d+)/$', DomainUpdate.as_view(),
        name='domain_update'),
    url(r'^domains/(?P<pk>\d+)/delete/$', DomainDelete.as_view(),
        name='domain_delete'),
    url(r'^rules/$', RuleList.as_view(), name='rules'),
    url(r'^rules/add/$', RuleCreate.as_view(), name='rule_add'),
    url(r'^rules/(?P<pk>\d+)/$', RuleUpdate.as_view(),
        name='rule_update'),
    url(r'^rules/(?P<pk>\d+)/delete/$', RuleDelete.as_view(),
        name='rule_delete'),
    url(r'^reports/$', ReportList.as_view(), name='reports'),
    url(r'^report/(?P<pk>[0-9]+)/$', ReportDetails.as_view(), name='report'),
    url(r'^report/(?P<pk>[0-9]+)/csv/$', CSVReportDetails.as_view(),
        name='csvreport'),
    # Login/logout stuff
    url(r'^accounts/login/', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}, name='login'),
    url(r'^accounts/logout/', 'django.contrib.auth.views.logout',
        {'template_name': 'logout.html'}, name='logout'),

    # General dialog success handler
    url(r'^(scanners|domains|rules)/(\d+)/(created)/$',
        DialogSuccess.as_view()),
    url(r'^(scanners|domains|rules)/(\d+)/(saved)/$',
        DialogSuccess.as_view()),
    url(r'^jsi18n/$', javascript_catalog, js_info_dict)
)
