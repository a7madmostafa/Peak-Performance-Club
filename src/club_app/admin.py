from django.contrib import admin

from .models import Branch, Member, Trainer, GymClass, Equipment

admin.site.register(Branch)
admin.site.register(Member)
admin.site.register(Trainer)
admin.site.register(GymClass)
admin.site.register(Equipment)
