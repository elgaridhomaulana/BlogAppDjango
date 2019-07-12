from django.urls import path, include, re_path

from . import views

urlpatterns = [
	path('', views.BlogListView.as_view(), name='home'),
	path('post/<int:pk>/', views.BlogDetailView.as_view(), name='post_detail'),
]
