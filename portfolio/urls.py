from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 
from . import views

urlpatterns = [
    path('', views.portfolio, name = 'portfolio'),
    path('newpost/', views.post, name='newpost'),
    path('edit/<int:post_id>', views.post, name = "post_edit"),
    path('delete/<int:post_id>', views.post_delete, name = "post_delete"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

