from django.test import TestCase
from django.contrib.auth.models import User

from store.models import Category, Product

class TestCategoriesModel(TestCase):

    def setUp(self):
       self.data1 = Category.objects.create(name='Парфумерія', slug='parfumeriya')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))
    
    def test_category_model_entry(self):
        """
        Test Category model default name
        """
        data = self.data1
        self.assertEqual(str(data), 'parfumeriya')

class TestProductsModel(TestCase):
    def setUp(self):
       Category.objects.create(name='django', slug='django')
       User.objects.create(username='admin')
       self.data1 = Product.objects.create(category_id=1, title='Maison Francis Kurkdjian Baccarat Rouge 540',
                    created_by_id=1, slug='maison-francis-kurkdjian-baccarat-rouge-540', price='88.99', image='images/baccarat_ILTACrq.png')

    def test_products_model_entry(self):
        """
        Test product model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'Maison Francis Kurkdjian Baccarat Rouge 540')