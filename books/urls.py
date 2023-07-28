from django.urls import path
from . import views


urlpatterns = [
    path('books/', views.book_list),
    path('books/<int:pk>/', views.book_detail),
    path('authors/', views.author_list),
    path('authors/<int:pk>/', views.author_detail)
]





# urlpatterns = [
#     path('welcome/', views.welcome),
#     path('hello/', views.hello),
#     path('get_books/<int:pk>/', views.get_books)
# ]