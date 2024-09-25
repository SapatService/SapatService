from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="SapatKg API",
      default_version='v1',
      description="Документация API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="Saparbekovtoni@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('api/Esenbek/', admin.site.urls),
    path('api/AboutUs/', include('AboutUs.urls')),
    path('api/OurServices/', include('OurServices.urls')),
    path('api/Reviews/', include('Reviews.urls')),
#    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
