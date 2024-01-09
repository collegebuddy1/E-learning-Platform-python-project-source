from django.contrib import admin

# Register your models here.
from .models import student, session,lecturer

admin.site.register(session)
admin.site.register(student)
admin.site.register(lecturer)


