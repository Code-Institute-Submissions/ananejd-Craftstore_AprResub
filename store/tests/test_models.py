from django.contrib.auth.models import User
from django.test import TestCase

from store.models import Category, Product


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='beads', slug='beads')

    def test_category_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'beads')


class TestProductsModel(TestCase):
    def setUp(self):
        Category.object.create(name='beads', slug='beads')
        User.object.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='beads_bag', created_by_id=1,
                                            slug='beads_bag', price='20.00', image='beads')
        self.data2 = Product.products.create(category_id=1, title='django wallet', created_by_id=1,
                                             slug='django-wallet', price='20.00', image='beads', is_active=False)
