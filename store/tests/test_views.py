from unittest import skip
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import Client, RequestFactory, TestCase
from store.views import all_products
from store.models import Category, Product


@skip("demonstrating skipping")
class TestSkip(TestCase):
    def test_skip_exmaple(self):
        pass


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        User.objects.create(username='admin')
        Category.objects.create(name='beads', slug='beads')
        Product.objects.create(category_id=1, title='beads_bag', created_by_id=1,
                               slug='beads_bag', price='99.99', image='beads_bag')

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """
        response = self.c.get('/', HTTP_HOST='noaddress.com')
        self.assertEqual(response.status_code, 400)

    def test_product_detail_url(self):
        response = self.c.get(
            reverse('store:product_detail', args=['beads_bag']))
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        # testing category response status
        response = self.c.get(
            reverse('store:category_list', args=['beads_bag']))
        self.assertEqual(response.status_code, 404)

    def test_homepage_html(self):
        request = HttpRequest()
        response = all_products(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Home</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)

    def test_view_function(self):
        request = self.factory.get('/item/beads_bag')
        response = all_products(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Home</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)
