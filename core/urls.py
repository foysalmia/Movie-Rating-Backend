from django.contrib import admin
from django.urls import path,include
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('admin/', admin.site.urls),
    path('api/',include("movieRating.urls")),
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.jwt')),
]
