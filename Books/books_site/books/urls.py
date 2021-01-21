from django.urls import path
from . import views


urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:book_pk>/', views.book_id, name='book_id'),
    # ex: /polls/5/results/
    path('author/<int:auth_id>/', views.author_id, name='author_id'),
    # ex: /polls/5/vote/
    path('authors/<str:first_letters>/', views.find_author, name='find_author'),
]
