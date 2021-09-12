from django.urls import path
from . import views


urlpatterns = [
    # locations
    path("location", views.LocationList.as_view()),
    path("location/<int:pk>", views.LocationDetail.as_view()),
    # iseeya_users    
    path("iseeya_user", views.ISeeYaUserList.as_view()),
    path("iseeya_user/<int:pk>", views.ISeeYaUserDetail.as_view()),
    # profiles
    path("profile", views.ProfileList.as_view()),
    path("profile/<int:pk>", views.ProfileDetail.as_view()),
    # iseeya_maps
    path("iseeya_map", views.ISeeYaMapList.as_view()),
    path("iseeya_map/<int:pk>", views.ISeeYaMapDetail.as_view()),
    # marker
    path("marker", views.MarkerList.as_view()),
    path("marker/<int:pk>", views.MarkerDetail.as_view()),
    # users
    path("get_iseeya_user", views.get_iseeya_user)
]