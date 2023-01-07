from django.contrib import admin

# Register your models here.
from .models import Bol, Stage, Pad, Well, sandType

admin.site.register(Bol)
admin.site.register(sandType)
admin.site.register(Pad)
admin.site.register(Stage)
admin.site.register(Well)
