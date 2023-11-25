from django.contrib import admin
from .models import AuthorAPI, BookAPI, CategoryAPI

# Register your models here.


admin.site.register(AuthorAPI)
admin.site.register(BookAPI)
admin.site.register(CategoryAPI)