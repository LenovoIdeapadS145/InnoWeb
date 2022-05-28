from django.contrib import admin

# Register your models here.
from .models import New_Model, New_Feedback
admin.site.register(New_Model)
admin.site.register(New_Feedback)