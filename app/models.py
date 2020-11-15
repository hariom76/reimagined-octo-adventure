from django.db import models

# Create your models here.
class bank_users(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    current_balance = models.IntegerField()

    
class transfer_money(models.Model):
    from_user = models.CharField(max_length=50)
    to_user = models.CharField(max_length=50)
    amount = models.IntegerField()