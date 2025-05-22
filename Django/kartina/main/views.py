from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import modern_picture, classic_picture, abstract_picture, portret_picture, favorites_picture


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


def favorites(request):
    favorite = favorites_picture.objects.all()
    return render(request, 'main/favorites.html', {'favorite': favorite})


@csrf_exempt
def add_to_favorites(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Получаем или создаем запись в избранном
            fav, created = favorites_picture.objects.get_or_create(
                title=data['title'],
                defaults={
                    'price': data['price'],
                    'picture': data['picture']
                }
            )

            # Если запись уже существовала (не была создана), удаляем ее
            if not created:
                fav.delete()
                return JsonResponse({'success': True, 'action': 'removed'})

            return JsonResponse({'success': True, 'action': 'added'})

        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})