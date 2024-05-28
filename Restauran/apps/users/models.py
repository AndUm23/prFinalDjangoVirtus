from django.db import models
from django.contrib.auth.models import User
    
class Waiter(models.Model):
    CHARGE_CHOICES = (
        ('MG', 'MANAGER'),
        ('AT', 'ADMINTABLES'),
        ('EX', 'EXTRA')
    )
    
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, default=1)
    charge = models.CharField(max_length=60, choices=CHARGE_CHOICES, default = "MG")
        
    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name} - {self.get_charge_display()}"
   
