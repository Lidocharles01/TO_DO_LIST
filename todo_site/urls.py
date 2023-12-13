# urls.py
from django.contrib import admin
from django.urls import path
from todo.views import index, remove, edit, complete

urlpatterns = [
    path('', index, name="todo"),
    path('del/<int:item_id>/', remove, name="remove"),
    path('edit/<int:item_id>/', edit, name="edit"),
    path('complete/<int:item_id>/', complete, name="complete"),
    path('admin/', admin.site.urls),
]
