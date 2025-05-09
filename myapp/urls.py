from django.urls import path
from .views import project_data_raw_view,login_view

urlpatterns = [
    path('projects/', project_data_raw_view, name='product-list'),
    path('login/', login_view, name='login'),
]