from django.urls import path

from . import views

app_name = 'article'

urlpatterns = [
    path('list/', views.article_list, name='list'),
    path('detail/<int:id>/', views.article_detail, name='detail'),
]
