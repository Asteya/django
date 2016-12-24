from django.contrib import admin
from .models import Cause,Ngo,Story,Talk

admin.site.register(Cause)
admin.site.register(Ngo)
admin.site.register(Story)
admin.site.register(Talk)

# Register your models here.
