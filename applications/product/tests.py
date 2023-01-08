import unittest

from django.urls import reverse

from applications.product.models import Category
from applications.product.serializers import ProductSerializer


class MyTestCase(unittest.TestCase):
    def test_something(self):
        category_1 = Category.objects.create(category_title='test')
        url = reverse('product-list')
        response = self.client.get(url)
        serializer_data = ProductSerializer(category_1).data
        self.assertEqual(serializer_data, response.data)
        print(response.data)


if __name__ == '__main__':
    unittest.main()
