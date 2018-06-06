from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views
from clients.views import auth_login

app_name = 'clients'

urlpatterns = [

	path('index', views.index, name='index'),
	path('<int:id>/',views.details, name='details'),
	path('e',views.empindex,name='e'),
	path('e/<int:id>/',views.empdetail,name='empdetail'),
	path('company/',views.company,name='company_html'),
	path('company1/<int:id>/',views.company1,name='company'),

	path('emp/<int:id>',views.employeeedit,name='employeeedit'),
	path('delete1/<int:id>',views.delete_empview,name='delete'),
    path('delete/<int:id>',views.deleteview,name='delete12'),
    
    path('p',views.projectindex,name='p'),
    path('proj/',views.projectCreate.as_view(),name='project'),
    path('proj/<int:id>',views.projectdetails,name='projectdetails'),

    path('project/<pk>/',views.projectedit.as_view(),name='projectedit'),
    path('project1/<pk>',views.projectdelete.as_view(),name='projectdelete'),
    path('pm',views.projectmodindex,name='pm'),
    path('pm/<int:id>',views.projectmoddetails,name='projectmoddetail'),
    path('projm/',views.addprojectmod,name='addprojectmod'),
    path('pm/edit/<int:id>',views.projectmodedit,name='editprojectmod'),
    path('pm/delete/<int:id>',views.projectmoddelete,name='deleteprojectmod'),
    path('register/',views.UserFormView.as_view()),
    path('login/', auth_login,name='login'),
    path('logout/', auth_views.logout,{'template_name':'clients/logout.html'},name='logout'),

  
]