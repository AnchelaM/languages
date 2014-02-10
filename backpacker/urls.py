from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.index', name='index'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/', 'app.views.about'),
    url(r'^indexee/', 'app.views.indexee'),
    url(r'^category/(?P<tag>\w+)/$', 'app.views.category'),
    url(r'^post/(?P<slug>\w+)/$', 'app.views.post'),
    url(r'^ckeditor/', include('ckeditor.urls')),
    ) + static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)
