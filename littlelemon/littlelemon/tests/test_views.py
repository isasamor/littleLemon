# from django.test import TestCase
# from littlelemon.restaurant.models import Menu
# from django.urls import reverse
# from littlelemon.restaurant.serializers import MenuSerializer


# class MenuViewTest(TestCase):
#     def setUp(self):
#         Menu.objects.create(title='Menu1', price=10)
#         Menu.objects.create(title='Menu2', price=20)
#         Menu.objects.create(title='Menu3', price=30)

#     def test_getall(self):
#         url = reverse('restaurant/menu/<int:pk>')  
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         serialized_data = MenuSerializer(Menu.objects.all(), many=True).data
#         self.assertEqual(response.data, serialized_data)
