from django.contrib import admin
from .models import Post
# Register your models here.

#Чтобы наша модель стала доступна на странице администрирования, нам нужно зарегистрировать её
admin.site.register(Post)