from django.shortcuts import render

# Create your views here.
# """
#  함수를 만들어서 어떤 상황에서 보일지
#  그리고 나서 url에서 정의해줘야 한다.
# """


def home(request):
    return render(request, 'home.html')


def helloworld(request):
    return render(request, 'helloworld.html')
