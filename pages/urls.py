from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.index_view, name='home'),
    path('upload_endpoint/', views.upload_endpoint, name="upload_endpoint"),
]
