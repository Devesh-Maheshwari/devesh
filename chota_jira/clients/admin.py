from django.contrib import admin


from .models import Company,Project,Projectmodule,User



admin.site.register(Company)
admin.site.register(Project)

admin.site.register(Projectmodule)
admin.site.register(User)
