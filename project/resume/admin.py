from django.contrib import admin

from resume.models import Post,contact
# Register your models here.




class PostAdmin(admin.ModelAdmin):
    date_hierarchy= 'created_date'


class contactAdmin(admin.ModelAdmin):
    list_display= ('name', 'email')
    list_filter=('email',)
    date_hierarchy= 'created_date'

admin.site.register(contact,contactAdmin)
admin.site.register(Post,PostAdmin)