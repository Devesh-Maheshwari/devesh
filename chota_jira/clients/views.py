from django.shortcuts import render,get_object_or_404, redirect,HttpResponseRedirect,HttpResponse
from django.urls import reverse_lazy


from .models import Company,Project,Projectmodule,User
from .forms import NameForm, EmployeeForm, ProjectForm, projectmodform, UserForm, LoginForm
from django.contrib.auth import login

from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth import authenticate



@login_required(login_url='clients/login')
def index(request):
	company_list=Company.objects.order_by('id')
	context={'company_list':company_list}

	return render(request, 'clients/index.html',context)


@login_required
def details(request,id):
	company =  get_object_or_404(Company, pk=id)

	return render(request, 'clients/details.html',{'company':company})



@login_required
def empindex(request):
	emp_list=User.objects.order_by('id')
	context={'emp_list':emp_list}

	return render(request, 'clients/emp.html',context)

@login_required
def empdetail(request,id):
	emp=get_object_or_404(User,pk=id)
	return render(request,'clients/empdetail.html',{'emp':emp})


@login_required
def employeeedit(request,id):
	instance = get_object_or_404(User, id=id)
	form =EmployeeForm(request.POST or None, instance=instance)
	if form.is_valid():
		form.save()
		return redirect('/clients/e/' + str(instance.id) + '/')
	return render(request, 'clients/employee.html', {'form': form}) 


@login_required
def delete_empview(request,id):
	

	employee =  get_object_or_404(User, pk=id)
	employee.delete()
	return redirect('/')
	
@login_required
def company(request):
	if request.method=='POST':
		form =NameForm(request.POST)
		if form.is_valid():
			company=Company()
			company.company_name=form.cleaned_data.get('company_name','default1')
			company.company_location=form.cleaned_data.get('company_location','default2')
			company.company_description=form.cleaned_data.get('company_description','default3')
			company.company_code=form.cleaned_data.get('company_code','default4')
			

			company.save()
			return HttpResponse("your details have been submited")
	else:
		form=NameForm()
		context={'form':form}
		return render(request, 'clients/company.html',context)



@login_required
def company1(request,id): 
    instance = get_object_or_404(Company, id=id)
    form = NameForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('/clients/' + str(instance.id) + '/')
        
    return render(request, 'clients/company.html', {'form': form}) 



@login_required
def deleteview(request,id):
	company =  get_object_or_404(Company, pk=id)
	company.delete()
	return redirect('/clients/')



@login_required
def projectindex(request,id):

	company=Company.objects.get(pk=id)
	context={'company':company, 'id' : id}
	return render(request, 'clients/proj.html',context)





@login_required
def projectdetails(request,id):
	proj=get_object_or_404(Project,pk=id)
	return render(request,'clients/projectdetails.html',{'proj':proj})





class projectCreate(CreateView):
	form_class = ProjectForm

	template_name = 'clients/project.html'

	def form_valid(self, ProjectForm):
		ProjectForm.instance.created_by = self.request.user
		return super().form_valid(ProjectForm)

	def get_form_kwargs(self):
		kwargs = super(projectCreate, self).get_form_kwargs()
		tmp = (self.request.path).split('/')
		comp_id = tmp[len(tmp)-1]
		kwargs['company_id'] = int(comp_id)
		return kwargs
	# success_url = reverse('clients:p')
	success_message = "project was added successfully"


	# def get_form_kwargs(self):
	#  	kwargs = super().get_form_kwargs()
	#  	path = self.request.path.split('/')
	#  	id = path[len(path) - 1]
	#  	kwargs.update(project_id=id)
	# 	return kwargs

class projectedit(UpdateView):
	model=Project
	template_name = 'clients/project.html'
	fields = ['company_name', 'project_name', 'startdate', 'end_date', 'description', 'project_code']
	# success_url = reverse_lazy('clients:projectdetails')


	def get_success_url(self, **kwargs):
		return reverse_lazy('clients:projectdetails', args=(self.object.id,))


class projectdelete(DeleteView):
	model = Project
	success_url = reverse_lazy('clients:p')
	def get(self, request, *args, **kwargs):
		return self.post(request, *args, **kwargs)


@login_required
def projectmodindex(request):
	projectmod_list=Projectmodule.objects.order_by('id')
	context={'projectmod_list':projectmod_list}
	return render(request, 'clients/projectmod.html',context)

@login_required
def projectmoddetails(request,id):
	print("devesh will become programmer")
	projmod=get_object_or_404(Projectmodule,id=id)
	
	return render(request, 'clients/projectmoddetails.html',{'projmod':projmod})

@login_required
def addprojectmod(request):
	if request.method=='POST':
		print("Inside Post")
		print(request.POST)
		form=projectmodform(request.POST)
		print('jksfbjksgr bguewguig weguigje gjes fib yg')
		if form.is_valid():
			form.save()
			return HttpResponse('your details have saved')
	else:
		form=projectmodform()
		context={'form':form}
		return render(request,'clients/addprojectmod.html',context)


def projectmodedit(request,id):

	instance =get_object_or_404(Projectmodule,id=id)
	form=projectmodform(request.POST or None,instance=instance)
	if form.is_valid():
		form.save()
		return redirect('/clients/pm/'+str(instance.id))
	return render(request,'clients/addprojectmod.html',{'form':form})


def projectmoddelete(request,id):
	projectmod=get_object_or_404(Projectmodule,pk=id)
	projectmod.delete()
	return redirect('/clients/pm')




def auth_login(request):
	print("shdg suig gsdui saui ")

	if request.method == "POST":
		form = LoginForm(request.POST)

		print(request.POST)
		username = request.POST.get('email_or_emp_mobile_or_username')
		password = request.POST.get('password')
		print()
		user = authenticate(username=username, password=password)
		if user:
			login(request,user)
			return HttpResponseRedirect('/clients/index')
		else:

			return render(request, 'clients/login.html')
	else:

		return render(request, 'clients/login.html')



class UserFormView(FormView):
	form_class=UserForm
	template_name='clients/registration.html'


	def get(self,request):
		form=self.form_class(None)
		return render(request,self.template_name,{'form':form})

	def post(self,request):
		form=self.form_class(request.POST)
		if form.is_valid():
			print('hiasdfd')
			user=form.save()
			username=form.cleaned_data['username']
			password=form.cleaned_data['password1']
			user.set_password(password)
			user.save()
			return redirect('/clients/')

		else:
			print(form.errors)

def home(request):
    return render(request,'clients/home.html')


