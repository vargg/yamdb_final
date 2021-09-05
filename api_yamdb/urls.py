from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

urlpatterns = [
    path(
        '',
        RedirectView.as_view(url='redoc', permanent=True),
        name='index'
    ),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),

]

schema_view = get_schema_view(
    openapi.Info(
        title="YaMDb API",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    path(
        'redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='redoc'
    ),
]
