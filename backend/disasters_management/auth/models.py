
from djongo import models
from django.contrib.auth.models import User

class GeoJSON(models.Model):
	type		= models.CharField(max_length=15, default = "Point")
	coordinates = models.ListField()

	class Meta:
		abstract = True


class Account(models.Model):

    ACCOUNT_TYPE = (
        ('o', 'organizaation'),
        ('h', 'human')
    )

    ## required to associate Account model with User model (Important)
    user = models.OneToOneField(User, null=True, blank=True, related_name="account", on_delete=models.CASCADE)
    type = models.IntegerField(choices=ACCOUNT_TYPE, blank=False, null=True)
    center_point = models.EmbeddedModelField(model_container=GeoJSON)
    lat     = models.FloatField()
    lang    = models.FloatField()

    ## additional fields
    phone = models.IntegerField(blank=True, default=1)    


    objects = models.DjongoManager()

    def __str__(self):
        return self.user.username
