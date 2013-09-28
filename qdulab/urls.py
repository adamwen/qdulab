from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'qdulab.views.home', name='home'),
    #url(r'^qdulab/', include('qdulab.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'lessons.views.index'),
    url(r'^index$', 'lessons.views.index', name='index'),
    url(r'^lesson/book/(?P<lesson_pk>\d+)$', 'lessons.views.book',
        name="book_lesson"),
    url(r'^lesson/cancel/(?P<lesson_pk>\d+)$', 'lessons.views.cancel_lesson',
        name='cancel_lesson'),

    url(r'^account/login$', 'logins.views.user_login', name='login'),
    url(r'^account/logout$', 'logins.views.user_logout', name='logout'),
    url(r'^account/register$', 'logins.views.user_register', name='register'),

)
urlpatterns += staticfiles_urlpatterns()
