from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static
# from djangular.views import DjangularModuleTemplateView

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'travel.views.index', name='index'),
    url(r'^recommend$', 'travel.views.recommend', name='recommend'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
