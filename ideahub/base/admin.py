from django.contrib import admin

# Register your models here.
from .models import Panel, Idea, Message

admin.site.register(Panel)
admin.site.register(Idea)
admin.site.register(Message)
