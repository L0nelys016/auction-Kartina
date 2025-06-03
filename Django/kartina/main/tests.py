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
        
        


    def test_modern_picture_str(self):
        self.assertEqual(str(self.modern), 'Современная картина')

    def test_classic_picture_str(self):
        self.assertEqual(str(self.classic), 'Классическая картина')

    def test_abstract_picture_str(self):
        self.assertEqual(str(self.abstract), 'Абстрактная картина')

   

    
