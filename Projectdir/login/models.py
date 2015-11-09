from django.db.models import Model, CharField, DateTimeField, BooleanField

class Users(Model):
	email = CharField(max_length=100)
	password = CharField(max_length=200)
	firstName = CharField(max_length=100, null=True)
	lastNme = CharField(max_length=100, null=True)
	lastLogin = DateTimeField(null=True)
	isLoggedIn = BooleanField(default=False)
