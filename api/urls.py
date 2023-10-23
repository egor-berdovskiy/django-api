from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:user_id>/', views.UserDetail.as_view()),
    path('users/create/', views.UserCreate.as_view()),
    path('users/update/<int:user_id>/', views.UserUpdate.as_view()),
    path('users/delete/<int:user_id>/', views.UserDelete.as_view()),
    path('users/check/<int:user_id>/', views.UserCheck.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
