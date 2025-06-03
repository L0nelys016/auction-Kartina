from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import modern_picture, classic_picture, abstract_picture, portret_picture, favorites_picture
from django.template.defaulttags import register
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def index(request):
    return render(request, 'main/main.html')


def modern_art(request):
    modern_pic = modern_picture.objects.all()

    # Создаем словарь {original_id: favorite_id} для современных картин
    favorites = favorites_picture.objects.filter(
        picture_type='modern',
        original_id__in=modern_pic.values_list('id', flat=True)
    )
    favorite_ids_dict = {fav.original_id: fav.id for fav in favorites}

    return render(request, 'main/Sovrem_iscusstvo.html', {
        'modern_pic': modern_pic,
        'favorite_ids_dict': favorite_ids_dict
    })


def classic_art(request):
    classic_pic = classic_picture.objects.all()

    # Создаем словарь {original_id: favorite_id} для классических картин
    favorites = favorites_picture.objects.filter(
        picture_type='classic',
        original_id__in=classic_pic.values_list('id', flat=True)
    )
    favorite_ids_dict = {fav.original_id: fav.id for fav in favorites}

    return render(request, 'main/Klassicheskoe_iskusstvo.html', {
        'classic_pic': classic_pic,
        'favorite_ids_dict': favorite_ids_dict
    })


def abstraction(request):
    abstract_pic = abstract_picture.objects.all()

    favorites = favorites_picture.objects.filter(
        picture_type='abstract',
        original_id__in=abstract_pic.values_list('id', flat=True)
    )
    favorite_ids_dict = {fav.original_id: fav.id for fav in favorites}

    return render(request, 'main/Abstrakcia.html', {
        'abstract_pic': abstract_pic,
        'favorite_ids_dict': favorite_ids_dict
    })


def Portrait(request):
    portret_pic = portret_picture.objects.all()

    favorites = favorites_picture.objects.filter(
        picture_type='portret',
        original_id__in=portret_pic.values_list('id', flat=True)
    )
    favorite_ids_dict = {fav.original_id: fav.id for fav in favorites}

    return render(request, 'main/Portreti.html', {
        'portret_pic': portret_pic,
        'favorite_ids_dict': favorite_ids_dict
    })


def favorites(request):
    favorite = favorites_picture.objects.all()
    return render(request, 'main/favorites.html', {'favorite': favorite})


@csrf_exempt
def add_to_favorites(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            picture_id = data.get('picture_id')
            picture_type = data.get('picture_type')  # 'modern', 'classic' и т.д.

            # Получаем картину в зависимости от типа
            if picture_type == 'modern':
                picture = modern_picture.objects.get(id=picture_id)
            elif picture_type == 'classic':
                picture = classic_picture.objects.get(id=picture_id)
            elif picture_type == 'abstract':
                picture = abstract_picture.objects.get(id=picture_id)
            elif picture_type == 'portret':
                picture = portret_picture.objects.get(id=picture_id)
            # ... другие типы

            # Проверяем, не добавлена ли уже
            if favorites_picture.objects.filter(original_id=picture.id, picture_type=picture_type).exists():
                return JsonResponse({'success': False, 'error': 'Уже в избранном'}, status=400)

            fav = favorites_picture.objects.create(
                title=picture.title,
                price=picture.price,
                picture=picture.picture,
                original_id=picture.id,
                picture_type=picture_type
            )

            return JsonResponse({'success': True, 'favorite_id': fav.id})

        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)


@csrf_exempt
def remove_from_favorites(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            favorite_id = data.get('favorite_id')  # получаем ID избранной записи

            # Удаляем запись из избранного по её ID
            try:
                favorite = favorites_picture.objects.get(id=favorite_id)
                favorite.delete()
                return JsonResponse({'success': True})
            except favorites_picture.DoesNotExist:
                return JsonResponse({'success': False, 'error': 'Запись не найдена'}, status=404)

        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)

    return JsonResponse({'success': False, 'error': 'Только POST-запросы'}, status=405)


def my_picture(request):
    # Получаем все картины из всех категорий
    modern_pic = modern_picture.objects.all()
    classic_pic = classic_picture.objects.all()
    abstract_pic = abstract_picture.objects.all()
    portret_pic = portret_picture.objects.all()

    return render(request, 'main/my_picture.html', {
        'modern_arts': modern_pic,
        'classic_arts': classic_pic,
        'abstract_arts': abstract_pic,
        'portret_arts': portret_pic,
    })


@csrf_exempt
def add_pic(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        category = request.POST.get('category')
        image = request.FILES.get('image')

        if category == 'modern':
            modern_picture.objects.create(title=title, price=price, picture=image)
        elif category == 'classic':
            classic_picture.objects.create(title=title, price=price, picture=image)
        elif category == 'abstract':
            abstract_picture.objects.create(title=title, price=price, picture=image)
        elif category == 'portret':
            portret_picture.objects.create(title=title, price=price, picture=image)

        return redirect('my_picture')

    return render(request, 'main/add_pic.html')

@csrf_exempt
def delete_picture(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            picture_id = data.get('picture_id')
            picture_type = data.get('picture_type')

            # Определяем модель в зависимости от типа картины
            if picture_type == 'modern':
                model = modern_picture
            elif picture_type == 'classic':
                model = classic_picture
            elif picture_type == 'abstract':
                model = abstract_picture
            elif picture_type == 'portret':
                model = portret_picture
            else:
                return JsonResponse({'success': False, 'error': 'Неверный тип картины'}, status=400)

            # Пытаемся найти и удалить картину
            try:
                picture = model.objects.get(id=picture_id)
                picture.delete()
                return JsonResponse({'success': True})
            except model.DoesNotExist:
                return JsonResponse({'success': False, 'error': 'Картина не найдена'}, status=404)

        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)

    return JsonResponse({'success': False, 'error': 'Только POST-запросы'}, status=405)


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматический вход после регистрации
            return redirect('/')  # Перенаправление на главную
    else:
        form = RegisterForm()

    return render(request, 'main/Registration.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Изменили с email на username
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'main/Avtorizacia.html', {
                'error': 'Неверный логин или пароль',
                'username': username  # Сохраняем введённый логин
            })

    return render(request, 'main/Avtorizacia.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def profile_view(request):
    return render(request, 'main/my_picture.html', {'user': request.user})