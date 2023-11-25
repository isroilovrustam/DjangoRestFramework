from django.contrib import admin
from .models import AuthorGeneric, BookGeneric, CategoryGeneric

# Register your models here.


admin.site.register(AuthorGeneric)
admin.site.register(BookGeneric)
admin.site.register(CategoryGeneric)