from django.urls import path
from back_end import views
from django.contrib.auth import views as auth_views

app_name = 'back_end'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('view-profile/', views.view_profile, name='view_profile'),
    path('edit-profile/', views.edit_user, name='edit_user'),
    path('change-password/', views.pass_form, name='pass_form'),
    path('login-page/', auth_views.LoginView.as_view(template_name='back_end/login.html'), name='login'),
    path('logout-page/', auth_views.LogoutView.as_view(template_name='back_end/logout.html'), name='logout'),  
    path('registeration-page/', views.register, name='register'),
    path('display-post/', views.DisplayPost.as_view(), name='show_post'),
    path('detail-post/<int:pk>/', views.DetailPost.as_view(), name='show_detail_post'),
    path('add-post/', views.AddPost.as_view(), name='add_post'),
    path('edit-post/<int:pk>/', views.EditPost.as_view(), name='edit_post'),
    path('delete-post/<int:pk>/', views.DeletePost.as_view(), name='del_post'),
]