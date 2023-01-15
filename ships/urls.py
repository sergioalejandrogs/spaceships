from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar/', views.add, name='add'),
    path('editar/<int:id>', views.edit, name='edit'),
    path('eliminar/<int:id>', views.delete, name='delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   
