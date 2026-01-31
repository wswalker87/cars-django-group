from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from .models import Car, UserProfiles
from .serializers import CarSerializer
from django.core.serializers import serialize
# Create your views here.

class AllCars(APIView):
    def get(self, request): 
        cars = Car.objects.order_by("id") # "id"
        serialized_car = CarSerializer(cars, many=True)
        return Response(serialized_car.data)

class AllUsers(APIView):
    def get(self, request):
        users = UserProfiles.objects.order_by("account_id")
        serialized_user = CarSerializer(users, many=True)
        return Response(serialized_user.data)

class SelectCars(APIView):
    
    def get_car(self, id):
        cars = Car.objects.order_by(id=id)
        serialized_car = CarSerializer(cars, many=True)
        return Response(serialized_car.data)

    def put(self, request, id):
        cars = self.get_car(id)
        serialized_car = CarSerializer(cars, data=request.data)
        if serialized_car.is_valid():
            serialized_car.save()
            return Response(serialized_car.data)
        return Response(serialized_car.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        cars = self.get_car(id)
        cars.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)       

class SelectUser(APIView):

    def get_user(self, id):
        pass

    def put(self, request, id):
        pass    
    
    def delete(self, request, id):
        pass   

class CreateUser(APIView):

    def post(self,request):
        pass

class CreateCar(APIView):

    def post(self,request):
        serializer = CarSerializer(data=request.data)
        #print(serializer.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


