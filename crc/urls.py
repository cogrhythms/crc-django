from django.conf.urls import patterns, include, url
from wiki.urls import get_pattern as get_wiki_pattern
from django_nyt.urls import get_pattern as get_nyt_pattern
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # :
    # url(r'^$', 'crc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'crc.views.home', name='home')
)

urlpatterns += patterns('',
    (r'wiki/notifications/', get_nyt_pattern()),
    (r'wiki/', get_wiki_pattern()),
)
