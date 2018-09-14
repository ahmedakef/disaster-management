
from djongo import models
from django.contrib.auth.models import User



class Account(models.Model):
    ## required to associate Account model with User model (Important)
    user = models.OneToOneField(User, null=True, blank=True,on_delete=models.CASCADE)

    ## additional fields
    phone = models.IntegerField(blank=True, default=1)    

    def __str__(self):
        return self.user.username
