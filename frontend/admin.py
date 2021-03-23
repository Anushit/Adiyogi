from django.contrib import admin
from .models import Employee,Country,City,State,Post
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'username','firstname','email','status']
    search_fields = ['username']
    list_per_page = 5


class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','title_description','content','meta_description','image']

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(State)
admin.site.register(Post,PostAdmin)