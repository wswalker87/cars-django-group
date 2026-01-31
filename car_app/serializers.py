from rest_framework import serializers
from .models import Car, AppUser, CarModel, UserProfiles, Advertisement

class CarModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CarModel
        fields = ('id', 'make','model')

class CarSerializer(serializers.ModelSerializer):
    
    car_model = CarModelSerializer()

    class Meta:
        model = Car
        fields = ('id', 'number_of_owners', 'registration_number', 
                'manufacture_year', 'number_of_doors', 'mileage', 'car_model')

    def create(self, validated_data):
        car_model_data = validated_data.pop('car_model')
        car_model = CarModel.objects.create(**car_model_data)
        car = Car.objects.create(car_model=car_model, **validated_data)
        return car
    def update(self, instance, validated_data):
        car_model_data = validated_data.pop('car_model')

        instance.make = validated_data.get('make', instance.make)
        instance.model = validated_data.get('model', instance.model)
        instance.save()

        if car_model_data is not None:
            car_model_instances = []

            for model_instance in car_model_data:
                make = model_instance.get('make')
                model = model_instance.get('model')
            car_model = CarModel.objects.get_or_create(make=make, model=model)
            model_instance.append(car_model)
            
class AppUserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = AppUser
        fields = ('id', 'first_name', 'last_name', 'email', 'password')

class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ('id', 'advertisement_date', 'car_id')

class UserSerializer(serializers.ModelSerializer):

    account_id = AppUserSerializer(many=True)
    advertisement = AdvertisementSerializer(many=True)

    class Meta:
        model = UserProfiles
        fields = ('account_id', 'street_name', 'street_number', 'zip_code', 'city', 'seller_account')
    
        def create(self, validated_data):
            users_data = validated_data.pop('account_id', 'seller_account')
            users = UserProfiles.objects.create(**validated_data)
            for user_data in users_data:
                user = UserProfiles.objects.create(**users_data)
                users.account_id.seller_account.add(user)
            return users
    
