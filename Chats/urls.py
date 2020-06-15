from . import views
from django.urls import path


urlpatterns = [
	
	path('send/', views.send, name = 'send'),
	path('', views.regUser, name = 'reguser'),
	path('login/', views.login_user, name = 'login')


	]