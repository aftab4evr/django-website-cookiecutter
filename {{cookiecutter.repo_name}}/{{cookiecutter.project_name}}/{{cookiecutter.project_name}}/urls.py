from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.views.generic.base import TemplateView

from django.conf.urls import url, include

admin.site.site_title = "{{ cookiecutter.project_name|title }} Administration"
admin.site.site_header = "{{ cookiecutter.project_name|title }} Administration"


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include(('website.urls', 'website'), namespace='website')),
]

handler404 = '{{ cookiecutter.project_name }}.views.handler404'
handler500 = '{{ cookiecutter.project_name }}.views.handler500'

if settings.DEBUG:
    urlpatterns += [
        url(r'^404/', TemplateView.as_view(template_name='404.html'), name='404'),
        url(r'^500/', TemplateView.as_view(template_name='500.html'), name='500'),
    ]
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
