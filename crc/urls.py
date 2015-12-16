from django.conf.urls import patterns, include, url
from wiki.urls import get_pattern as get_wiki_pattern
from django_nyt.urls import get_pattern as get_nyt_pattern
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # :
    # url(r'^$', 'crc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/$', include(admin.site.urls)),
    url(r'^$', 'crc.views.home', name='home'),
    url(r'^faculty/$', 'crc.views.faculty', name='faculty'),
    url(r'^postdocs/$', 'crc.views.postdocs', name='postdocs'),
    url(r'^topics/$', 'crc.views.topics', name='topics'),
    url(r'^groups/$', 'crc.views.groups', name='groups'),
    url(r'^courses/$', 'crc.views.courses', name='courses'),

)

urlpatterns += patterns('',
    (r'wiki/notifications/', get_nyt_pattern()),
    (r'wiki/', get_wiki_pattern()),
)
