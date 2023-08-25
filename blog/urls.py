from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    # post views
    path('', views.post_list, name='list'),
    path('<int:id>/', views.post_detail, name='detail'),
]