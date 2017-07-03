"""lawyer_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from index import views
from index import upload
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.index_view),
    url(r'^index/$', views.index_view),
    url(r'^about_us/$', views.about_us_view),
    url(r'^news/$', views.news_view),
    url(r'^contact_us/$', views.contact_us_view),
    url(r'^law_list/$', views.law_list_view),
    url(r'^service/$', views.service_view),
    url(r'^success_cases/$', views.success_cases_view),
    url(r'^communications/$', views.communications_view),

    url(r'^admin/uploads/(?P<dir_name>[^/]+)$', views.upload_image),
    # url(r'^uploads/(?P<path>.*)$', views.static.serve, {"document_root": settings.MEDIA_ROOT, }),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
