"""
URL configuration for web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from Mistakes.views import *

urlpatterns=[
    path('api/tutorials',Mahsulot_view.as_view()),
    path('api/tutorials/<int:id>',MahsulotDetail.as_view()),
    path('api/ish',Ishturi.as_view()),
    path('api/ish/<int:id>',IshDetail.as_view()),
    path('api/xodim',Xodim_view.as_view()),
    path('api/xodim/<int:id>',XodimDetail.as_view()),
    path('api/xato',Xato_view.as_view()),
    path('api/xato/<int:id>',XatoDetail.as_view()),
    path('api/missed',Missed_view.as_view()),
    path('api/missed/<int:id>',MissedDetail.as_view()),
    path('api/bulim',Bulim_View.as_view()),
    path('api/bulim/<int:id>',Bulim_Detail.as_view())
    
]