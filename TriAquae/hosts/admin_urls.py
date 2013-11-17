from django.conf.urls import patterns, include, url

#from django.views.generic.simple import redirect_to
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import views_ip, views_user, views_auth


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #----- batch ip releated -----------------------
    url(r'^load_batch_ip/$', views_ip.load_batch_ip),
    url(r'^load_batch_ip_form/$', views_ip.load_batch_ip_form),
    
    #----- batch user releated -----------------------
    url(r'^load_batch_remoteuser/$', views_user.load_batch_remoteuser),
    url(r'^load_batch_remoteuser_form/$', views_user.load_batch_remoteuser_form),
    
    url(r'^load_batch_auth/$', views_auth.load_batch_auth),
    url(r'^load_batch_auth_form/$', views_auth.load_batch_auth_form),
    
    #url(r'^test/$', views_test.test_template)
   
)
