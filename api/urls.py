from django.urls import path
from .views import (
    HealthCheckView, DatabaseHealthCheckView, StatsView,
    CustomTokenObtainPairView, SuperUserRegisterView,
    UserListView, UserDetailView,
    BookListView, BookDetailView,
    BorrowListView, BorrowDetailView, BorrowReturnView,
    APIRootView
)
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('', APIRootView.as_view(), name='api-root'),
    path('health/', HealthCheckView.as_view(), name='health-check'),
    path(
        'database-health/',
        DatabaseHealthCheckView.as_view(),
        name='database-health-check'
    ),
    path('stats/', StatsView.as_view(), name='stats'),

    # Authentication
    path(
        'auth/login/', CustomTokenObtainPairView.as_view(), name='login'
    ),
    path(
        'auth/register/', SuperUserRegisterView.as_view(), name='register'
    ),
    path(
        'auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'
    ),

    # Users
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    # Books
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Borrows
    path('borrows/', BorrowListView.as_view(), name='borrow-list'),
    path(
        'borrows/<int:pk>/',
        BorrowDetailView.as_view(),
        name='borrow-detail'
    ),
    path(
        'borrows/<int:pk>/return/',
        BorrowReturnView.as_view(),
        name='borrow-return'
    ),
]
