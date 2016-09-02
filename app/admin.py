from django.contrib import admin
from app.models import Category, Event

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields ={ 'slug':['title'] }

admin.site.register(Category, CategoryAdmin)

class EventAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':['title']}


admin.site.register(Event, EventAdmin)

