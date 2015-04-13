from django.db.models import Model, CharField, DateTimeField

class ThingsToDo(Model):
	toDo=CharField(max_length=1000)
	time=DateTimeField(null=True)
	where=CharField(max_length=1000)

class ThingsNotToDo(Model):
	notToDo=CharField(max_length=1000)
	time=DateTimeField(null=True)
	why=CharField(max_length=1000)