from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'BCAT.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('BiomCAT.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
