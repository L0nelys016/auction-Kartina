from django.test import TestCase
from .models import (
    modern_picture,
    classic_picture,
    abstract_picture,
    portret_picture,
    favorites_picture
)

class PictureModelsTestCase(TestCase):

    def setUp(self):
        # Создаем базовые объекты для тестирования
        self.modern = modern_picture.objects.create(
            title='Современная картина',
            price=1000,
            picture='path/to/modern.jpg'
        )
        self.classic = classic_picture.objects.create(
            title='Классическая картина',
            price=2000,
            picture='path/to/classic.jpg'
        )
        self.abstract = abstract_picture.objects.create(
            title='Абстрактная картина',
            price=1500,
            picture='path/to/abstract.jpg'
        )
        
        
        self.portret = portret_picture.objects.create(
                title='Портрет',
                price=1200,
                picture='path/to/portret.jpg'
            )


        self.favorites = favorites_picture.objects.create(
                title='Избранное',
                price=3000,
                picture='favorites/fav1.jpg',
                original_id=self.modern.id,
                picture_type='modern'
            )



    def test_modern_picture_str(self):
        self.assertEqual(str(self.modern), 'Современная картина')

    def test_classic_picture_str(self):
        self.assertEqual(str(self.classic), 'Классическая картина')

    def test_abstract_picture_str(self):
        self.assertEqual(str(self.abstract), 'Абстрактная картина')
   
    def test_favorites_picture_unique_together(self):
        # Проверка ограничения уникальности
        with self.assertRaises(Exception):
            favorites_picture.objects.create(
                title='Дубликат',
                price=500,
                picture='favorites/fav2.jpg',
                original_id=self.modern.id,
                picture_type='modern'
            )

    def test_portret_picture_str(self):
        self.assertEqual(str(self.portret), 'Портрет')

    
