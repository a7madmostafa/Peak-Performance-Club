from django.contrib import admin

from .models import Branch, Equipment, DamagedEquipment, GymClass, Member, Trainer

# Register your models here.
admin.site.register(Branch)
admin.site.register(Member)
admin.site.register(Trainer)
admin.site.register(GymClass)
admin.site.register(Equipment)   
admin.site.register(DamagedEquipment)