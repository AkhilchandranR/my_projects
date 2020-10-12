from django.db import models
import datetime
class entry(models.Model):
	content=models.TextField()
	date=models.DateTimeField(default=datetime.datetime.now())
	class Meta:
		db_table="entry"

# Create your models here.
