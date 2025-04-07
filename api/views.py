from rest_framework import generics, views, serializers
from rest_framework.response import Response
from .models import SuperUser, User, Book, Borrow
from .serializers import (
    SuperUserSerializer, CustomTokenObtainPairSerializer,
    UserSerializer, BookSerializer, BorrowSerializer
)
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer


class HealthCheckView(views.APIView):
    def get(self, request):
        return Response({"status": "ok"})


class DatabaseHealthCheckView(views.APIView):
    def get(self, request):
        try:
            from django.db import connection
            connection.ensure_connection()
            return Response({"status": "ok"})
        except Exception as e:
            return Response({"status": "error", "error": str(e)}, status=500)


class StatsView(views.APIView):

    def get(self, request):
        stats = {
            'books_count': Book.objects.count(),
            'users_count': User.objects.count(),
            'borrows_count': Borrow.objects.count(),
            'active_borrows_count': (
                Borrow.objects.filter(status='active').count()
            ),
            'inactive_borrows_count': (
                Borrow.objects.filter(status='returned').count()
            )
        }
        return Response(stats)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class SuperUserRegisterView(generics.CreateAPIView):
    queryset = SuperUser.objects.all()
    serializer_class = SuperUserSerializer


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def perform_create(self, serializer):
        serializer.save()


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BorrowListView(generics.ListCreateAPIView):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer

    def perform_create(self, serializer):
        book = serializer.validated_data['book']
        active_borrows = (
            Borrow.objects.filter(book=book, status='active').count()
        )

        if active_borrows >= book.total_count:
            raise serializers.ValidationError("No available books")

        serializer.save(status='active')


class BorrowDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer


class BorrowReturnView(generics.UpdateAPIView):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = 'returned'
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class APIRootView(views.APIView):
    def get(self, request):
        base_url = request.build_absolute_uri('/')

        routes = {
            "General": {
                "health": f"{base_url}health/",
                "database-health": f"{base_url}database-health/",
                "stats": f"{base_url}stats/",
            },
            "Authentication": {
                "login": f"{base_url}auth/login/",
                "register": f"{base_url}auth/register/",
            },
            "Books": {
                "list": f"{base_url}books/",
                "detail": f"{base_url}books/1/",
            },
            "Users": {
                "list": f"{base_url}users/",
                "detail": f"{base_url}users/1/",
            },
            "Borrows": {
                "list": f"{base_url}borrows/",
                "detail": f"{base_url}borrows/1/",
                "return": f"{base_url}borrows/1/return/",
            }
        }

        return Response({
            "message": "Libroll API is running!",
            "routes": routes,
        })
