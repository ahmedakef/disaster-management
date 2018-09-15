from datetime import datetime
from djongo import models

# Create your models here.

class GeoJSON(models.Model):
	type		= models.CharField(max_length=15, default = "Point")
	coordinates = models.ListField()

	class Meta:
		abstract = True


class Disaster(models.Model):

	DANGER_LEVELS = (
		('E', 'Easy'),
		('M', 'Medium'),
		('D', 'Danger'),
		('ED', 'Extra Danger')
	)


	#required
	diameter = models.FloatField(default = 0.5)
	center_point = models.EmbeddedModelField(model_container=GeoJSON)
	level_of_danger = models.CharField(max_length=2, default = 'M', choices = DANGER_LEVELS)
	added = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
	lat			= models.FloatField()
	lang		= models.FloatField()

	#optional
	title = models.CharField(max_length=200, blank = True)
	description = models.CharField(max_length=500, blank = True)



# class Disaster(Document):
#     #required
#     diameter = IntField(default = 0.5)
#     center = PointField()
#     level_of_danger = IntField(default = 0.5, choices = DANGER_LEVELS)
#     date_added = DateTimeField(default=datetime.now)

#     #optional
#     title = StringField()
#     description = StringField()
#     text = StringField(required=True)