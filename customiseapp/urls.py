
from django.urls import path
from . import views

urlpatterns = [
 path("createbook/",views.createbook,name='createbook'),
 path("authors/",views.createauthor,name='author'),
 path("",views.listbook,name='booklist'),
 path("specbook/<int:books_id>/",views.specificbook,name='details'),
 path("updatbook/<int:book_id>/",views.updatebook,name='update'),
 path('deletebook/<int:book_id>/',views.deletebook,name='delete'),
 path("base/",views.new_index),
 path("search/",views.Search_Book,name='search')
]