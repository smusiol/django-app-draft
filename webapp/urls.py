from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
    'document_root': settings.STATIC_ROOT,
    }),
    (r'^$', TemplateView.as_view(template_name='index.html')),
    # url(r'^blog/', include('blog.urls')),

    url(r'^panel/', include(admin.site.urls)),
)


# Debug toolbar configuration
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )