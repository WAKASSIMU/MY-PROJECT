from django.contrib import admin
from .models import Patient, Street, Chairperson
# Register your models here.
admin.site.register(Patient)
admin.site.register(Street)
admin.site.register(Chairperson)