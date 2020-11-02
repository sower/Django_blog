from django.urls import path

from . import views

app_name = 'article'

urlpatterns = [
    path('list/', views.article_list, name='list'),
    path('detail/<int:id>/', views.article_detail, name='detail'),
    path('create/', views.article_create, name='create'),
    path('delete/<int:id>/', views.article_delete, name='delete'),
    path(
        'safe-delete/<int:id>/',
        views.article_safe_delete,
        name='safe_delete'
    ),
    path('update/<int:id>/', views.article_update, name='update'),
]
