from django.contrib import admin

from .models import LineModel, RouteModel
# Register your models here.
admin.site.register(LineModel)
admin.site.register(RouteModel)