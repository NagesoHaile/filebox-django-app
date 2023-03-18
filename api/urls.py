from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name="home"),
    path('personal-infos/', views.getPersonalInfos,),
    path('personal-infos/add/',views.createPersonalInfo),
    path('personal-infos/<str:pk>/update',views.updatePersonalInfo),
    path('personal-infos/<str:pk>/delete',views.deletePersonalInfo),
    path('personal-infos/<str:pk>/', views.getPersonalInfo,),
]

