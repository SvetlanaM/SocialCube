from django.conf import settings
from django.conf.urls import patterns, include, url
from profiles.views import UserDetailView, OrganisersListView, UserContactDetailView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : settings.STATIC_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.backends.default.urls')),
    url(r'^$', 'profiles.views.home', name='home'),
    url(r'^organisers/all$', OrganisersListView.as_view(), name='organisers'),
    url(r'^organisers/(?P<slug>\w+)/personal-information/$', UserDetailView.as_view()),
    url(r'^organisers/(?P<slug>\w+)/contact-information/$', UserContactDetailView.as_view()),
    url(r'^edit/personal-information/$', 'profiles.views.edit_personal_information', name="edit"),
    url(r'^create/$', 'profiles.views.add_profile'),
   
    
    

)
