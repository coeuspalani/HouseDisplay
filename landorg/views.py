from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def floors(request):
    return render(request,'floors.html')
def g_f(request):
    return render(request,'grndfloor.html')
def f_f(request):
    return render(request,'frstfloor.html')
def t_f(request):
    return render(request,'terracefloor.html')
def rm(request):
    return render(request,'rooms.html')