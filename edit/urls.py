from django.urls import path

from . import views

app_name='edit'
urlpatterns=[
    path('<str:title>', views.edit, name='edit' )
]
