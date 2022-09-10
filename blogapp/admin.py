from django.contrib import admin
from .models import postmodel
from .models import commentmodel
from .models import contactmodel

# Register your models here.
admin.site.register(postmodel)
admin.site.register(commentmodel)
admin.site.register(contactmodel)