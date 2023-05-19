from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name = 'home'),
	path('update-task/<str:pk>', views.update_task, name = 'update_task'),
	path('delete-task/<str:pk>', views.delete, name = 'delete_task')

]