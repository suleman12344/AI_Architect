from django.urls import path
from . import views

urlpatterns = [
    path('generate/', views.generate_floor_plan, name='generate_floor_plan'),
    path('images/<str:image_name>', views.serve_floor_plan_image, name='serve_floor_plan_image'),
    path('test-images/', views.test_images_directory, name='test_images_directory'),
]