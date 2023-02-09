from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee
from django.contrib import messages
from django.views import View
from django.db.models import Q 

# Create your views here.

# add employee

def homepage(request):
    all_emp = Employee.objects.all()
    return render(request, 'emp_app/home.html', {'all_emp': all_emp})

def not_found_page(request, *args, **kwargs):
    pass

class AddEmployeeView(View):

    def get(self, request):
        form = EmployeeForm()
        return render(request, 'emp_app/add_employee.html', {'form': form})
    
    def post(self, request):
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congrats New Employee Success Created')
            return redirect('homepage') # redirecting at home page

        return render(request, 'emp_app/add_employee.html', {'form': form})

class UpdateeEmployee(View):
    def get(self, request,id=None):
            if id is not None and type(id) == int:
                try:
                    emp  = Employee.objects.get(pk=id)
                except Employee.DoesNotExist:
                    return redirect('page_not_found')
                else:
                    form = EmployeeForm(instance=emp)
                    return render(request, 'emp_app/update_employee.html',{'form': form})
            else:
                return redirect('page_not_found')
        
    def post(self, request, id=None):
            if id is not None and type(id) == int:

                try:
                     emp = Employee.objects.get(pk = id)
                except Employee.DoesNotExist:
                     return redirect('page_not_found')
                else:
                    form  = EmployeeForm(request.POST, request.FILES, instance=emp)

                    if form.is_valid():
                         form.save()
                         messages.success(request, 'Employee Data Succeddfuly Update')
                         return redirect('homepage')
                    return render(request, 'emp_app/update_employee.html',{'form': form})
                
            else:
                return redirect('page_not_found')
        
class DeleteEmployee(View):
     def get(self, request, id=None):
            if id is not None and type(id) == int:
                try:
                    emp = Employee.objects.get(pk = id)
                except Employee.DoesNotExist:
                     return redirect('page_not_found')
                else:
                    emp.delete()
                    messages.success(request, 'Employee Successfuly Deleted')
                    return redirect('homepage')
            else:
                return redirect('page_not_found')
            

def search_employees(request,*args, **kwargs):
    search  = request.GET['search']        # getting keywords to search the data
    
    result = Employee.objects.filter(
        Q(name__icontains = search)|       # name contains
        Q(email__icontains=search) |       # email icontains
        Q(salary__icontains = search)|     # salary icontains       
        Q(dept__name__icontains = search)| # dept name icontains
        Q(join_date__icontains = search))  # joining date icontains
    if result.count() <1:                  # checking result is must greater than or equal 1
        result = Employee.objects.all()    # if no object is found than return all obj
         
    return render(request, 'emp_app/home.html', {'all_emp': result})
     
        
        


            