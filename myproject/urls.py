from django.contrib import admin
from django.urls import path
import myapp.views #myapp폴더안의 views.py
import wordcount.views

urlpatterns = [
    path('hello/', admin.site.urls), #경로이름/
    #path('', myapp.views.home, name="home"), 
    path('', wordcount.views.home, name="home"),
    #myapp폴더-views.py-home함수 호출, 이름을 home으로 지정
    #url이름은 함수이름과 동일하게 짓자
    path('about/', wordcount.views.about, name="about"),
    path('result/', wordcount.views.result, name="result"),
]
