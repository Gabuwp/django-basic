from django.shortcuts import render


context = {'text':'Olá Home!'}
def index(request):
    print("index")
    return render(request,'home/index.html',context=context)