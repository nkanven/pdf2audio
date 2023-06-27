import os
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers, permissions
from rest.views import FileUploadView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()

schema_view = get_schema_view(
   openapi.Info(
      title=os.environ.get('PROJECT_NAME'),
      default_version=os.environ.get('PROJECT_VERSION'),
      description=os.environ.get('PROJECT_DESC'),
      terms_of_service=os.environ.get('TERMS_OF_SERVICE_URL'),
      contact=openapi.Contact(email=os.environ.get('ADMIN_EMAIL')),
      license=openapi.License(name=os.environ.get('SOFTWARE_LICENSE')),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^upload/(?P<filename>[^/]+)$', FileUploadView.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
