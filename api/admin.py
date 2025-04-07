from django.contrib import admin
from .models import SuperUser, User, Book, Borrow

admin.site.register(SuperUser)
admin.site.register(User)
admin.site.register(Book)
admin.site.register(Borrow)
