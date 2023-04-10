from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Grade)
admin.site.register(Subject)
admin.site.register(Topic)
admin.site.register(Question)
admin.site.register(AnswerOption)
