from django.contrib import admin
from models import ThingsToDo, ThingsNotToDo

class ThingsToDoAdmin(admin.ModelAdmin):
	list_display=('toDo','time')

class ThingsNotToDoAdmin(admin.ModelAdmin):
	list_display=('notToDo','time')

admin.site.register(ThingsToDo, ThingsToDoAdmin)
admin.site.register(ThingsNotToDo, ThingsNotToDoAdmin)