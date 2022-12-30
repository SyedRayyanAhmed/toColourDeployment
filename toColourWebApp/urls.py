from django.urls import path
from . import views
from django.conf.urls.static import static
from toColourDeployment import settings

urlpatterns = [
    path('', views.Welcome),
    path('exe_toColour', views.Execute_toColour, name = 'exe_toColour'),
    ]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)