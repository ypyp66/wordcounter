from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')
    '''렌더함수는 3개의 인자를 받을수 있음
    (request(고정), template이름, 딕셔너리형(선택))'''

def about(request):
    return render(request, 'about.html')
    
def result(request):
    text = request.GET['fulltext'] #fulltext 이름을 가진 요청을 가져옴
    words = text.split() #스페이스바 기준으로 나누어 리스트로 저장해줌
    countDict = {}

    for key in words:
        if key in countDict:
            countDict[key] += 1
        else:
            countDict[key] = 1

    return render(request, 'result.html', {'full': text, 'total': len(words), 'diction': countDict.items()})