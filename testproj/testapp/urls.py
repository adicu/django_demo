from django.conf.urls import patterns, include, url

urlpatterns = patterns('testapp.views',
    # Examples:
    # url(r'^$', 'testproj.views.home', name='home'),
    # url(r'^testproj/', include('testproj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', 'home'),
    url(r'^add_post$', 'add'),
    url(r'^regextest/(?P<arg1>.+)/', 'regex'),
)
