#정보를 어떤상황에서 어떻게 처리할건지 함수를 정의해놓음
from django.shortcuts import render

# Create your views here.

def home(request): #요청이 들어왔을 때 home.html을 반환하는 함수
    #이름은 html파일명과 같게하자
    return render(request, 'home.html')