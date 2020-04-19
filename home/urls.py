from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('events/<int:pk>/', views.events, name='events'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)