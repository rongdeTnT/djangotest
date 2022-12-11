from django.shortcuts import render,HttpResponse

def index(request):
    return render(request, 'index.html')

def users_list(request):
    return render(request, "users_list.html")

def users_add(request):
    return render(request, "users_add.html")