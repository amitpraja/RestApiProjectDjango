from django.contrib import admin
from testapp.models import client,project

# Register your models here.
class clientadmin(admin.ModelAdmin):
    list_display= [ 'client_name','created_at','created_by']
admin.site.register(client,clientadmin)

class projectadmin(admin.ModelAdmin):
    list_display= ['project']
admin.site.register(project,projectadmin)
