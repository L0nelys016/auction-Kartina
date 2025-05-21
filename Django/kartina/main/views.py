from django.shortcuts import render
from .models import modern_picture, classic_picture, abstract_picture, portret_picture

def index(request):
    return render(request, 'main/main.html')

def modern_art(request):
    modern_pic = modern_picture.objects.all()
    return render(request, 'main/Sovrem_iscusstvo.html', {'modern_pic': modern_pic})

def classic_art(request):
    classic_pic = classic_picture.objects.all()
    return render(request, 'main/Klassicheskoe_iskusstvo.html', {'classic_pic': classic_pic})

def abstraction(request):
    abstract_pic = abstract_picture.objects.all()
    return render(request, 'main/Abstrakcia.html', {'abstract_pic': abstract_pic})

def Portrait(request):
    portret_pic = portret_picture.objects.all()
    return render(request, 'main/Portreti.html', {'portret_pic': portret_pic})