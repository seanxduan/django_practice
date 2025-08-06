from django.contrib import admin

from .models import Question
#line of code to add our custom questions!

# Register your models here.

admin.site.register(Question)