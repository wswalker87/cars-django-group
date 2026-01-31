from django.urls import path, register_converter
from .views import AllCars, AllUsers, SelectUser, SelectCars, CreateCar
from .converters import IntOrStrConverter

# To use this custom converter in a URL pattern, you need to register it with Django using the register_converter function.
register_converter(IntOrStrConverter, 'int_or_str')

urlpatterns = [
    path('', AllCars.as_view(), name="all_cars"),
    path('users', AllUsers.as_view(), name="all_users"),
    path('<int_or_str:id>', SelectCars.as_view(), name="selected_car"),
    path('users/<int_or_str:id>', SelectUser.as_view(), name="selected_user"),
    path('add/', CreateCar.as_view(), name='add_car')
]


