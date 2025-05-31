from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_index, name='book_index'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('books/create/', views.BookCreate.as_view(), name='book_create'),
    
    # primary key is needed for update and delete views instead of book_id because CBV's use pk as the default identifier to retrieve objects
    path('books/<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'), 
    path('books/<int:pk>/delete/', views.BookDelete.as_view(), name='book_delete'),
]
