from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser


class Company(models.Model):

	company_name = models.CharField(max_length=50)
	company_location =models.CharField(max_length=50)
	company_description=models.CharField(max_length=100)
	company_code=models.IntegerField(unique=True)
	created = models.DateField(null=True)
	updated=models.DateField(null=True)

	def __str__(self):
		return self.company_name
    



class Project(models.Model):
	company_name = models.ForeignKey(Company,on_delete=models.CASCADE)
	project_name=models.CharField(max_length=30)
	startdate=models.DateField()
	end_date=models.DateField()
	description=models.CharField(max_length=500)
	project_code=models.IntegerField(unique=True)


	def __str__(self):
		return self.project_name




class User(AbstractUser):
	

	ROLECHOICE=(
		('admin', "admin"),
		('teamleader', "teamleader"),
		('employee', "employee"),

		)
	role=models.CharField(max_length=30,choices=ROLECHOICE)
	emp_code=models.IntegerField(unique=True)
	salary = models.DecimalField(max_digits=7, decimal_places=3,default=0)
	emp_name=models.CharField(max_length=30)
	emp_email = models.EmailField()
	emp_mobile = models.CharField(max_length=12)




class Projectmodule(models.Model):
	project=models.ForeignKey(Project,on_delete=models.CASCADE)
	assign=models.ForeignKey(User,on_delete=models.CASCADE ,related_name="dev")
	employee=models.ManyToManyField(User)
	m_name=models.CharField(max_length=30)
	m_code=models.IntegerField(unique=True)
	end_date=models.DateField()






