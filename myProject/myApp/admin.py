from django.contrib import admin

from myApp.models import *

class customUserDisplay(admin.ModelAdmin):
    list_display=["username","email","city","first_name","last_name"]
    search_fields=["username","email","city"]
    
    fieldsets=[
       (
           "This is my Title",
           { 
            "fields":["username","email","password"]
            }
       ),
       (
           "Advance Option",
           {
               "classes":["collapse"],
               "fields":[("first_name","last_name"),"city",'profile_pic'],
           }
       )
    ]
    
admin.site.register(customUSer,customUserDisplay)
admin.site.register(categoryModel)
admin.site.register(TaskModel)

