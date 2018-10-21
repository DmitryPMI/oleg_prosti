from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(TelegramUser)
admin.site.register(IntroQuestion)
admin.site.register(Answer)
admin.site.register(UserAnswer)
admin.site.register(Event)