from rest_framework import serializers
from .models import SuperUser, User, Book, Borrow
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class SuperUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperUser
        fields = ['id', 'username']


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        extra_kwargs = {
            'total_count': {'required': True}
        }


class BorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = ['id', 'book', 'user', 'borrow_date', 'return_date', 'status']
