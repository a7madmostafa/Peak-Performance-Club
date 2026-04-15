from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Branch(BaseModel):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Member(BaseModel):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    balance = models.FloatField()

    def __str__(self):
        return self.name
    
    @property
    def is_vip(self):
        return self.balance > 1000

class Trainer(BaseModel):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.name

   
class GymClassQuerySet(models.QuerySet):

    def trending(self):
        return self.annotate(num_members=models.Count('members')).filter(num_members__gt=5).order_by('-num_members')
    
class GymClassManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return GymClassQuerySet(self.model, using=self._db)
    
    def trending(self):
        return self.get_queryset().trending()
    

class GymClass(BaseModel):
    name = models.CharField(max_length=100)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    base_price = models.FloatField()
    members = models.ManyToManyField(Member, related_name='classes')

    objects = GymClassManager()

    def early_bird_price(self):
        if self.start_date > timezone.now() + timedelta(days=30):
            return round(self.base_price * 0.8) # self.base_price * 0.8
        return self.base_price
    
    def __str__(self):
        return self.name

class Equipment(BaseModel):
    name = models.CharField(max_length=100)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    purchase_date = models.DateField()
    price = models.FloatField()
    is_damaged = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

class EquipmentManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(is_damaged=True)
    
class DamagedEquipment(Equipment):
    objects = EquipmentManager()

    class Meta:
        proxy = True
        verbose_name = "Maintenance Alert"