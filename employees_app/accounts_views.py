from django.views import View
from django.contrib import messages
from django.shortcuts import render,redirect
from .accounts_forms import SignupForm,LoginForm,ChangePassword
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from .accounts_forms import UserProfileForm
from .models import Profile

# class HomepageView(View):
#     def get(self,request):
#         return render(request, 'accounts/login.html')

class SignupView(View):

    def get(self, request):
        if not request.user.is_authenticated:
            form = SignupForm()
            return render(request, 'accounts/signup.html', {'form': form})
        else:
           return redirect('dashboard')
        
    def post(self, request):
        if not request.user.is_authenticated:

            form = SignupForm(request.POST)
            if form.is_valid():
                uname = str(form.cleaned_data['username']).title()
                form.save()
                messages.success(request, f'Congrats {uname} Your Account Successfuly Created!')
                return redirect('login')
            return render(request, 'accounts/signup.html', {'form': form})
        else:
           return redirect('dashboard')
        
class LoginView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            form =  LoginForm()
            return render(request, 'accounts/login.html',{'form': form})
        else:
            return redirect('dashboard') 
    def post(self, request):
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get('username', None)
            password = form.cleaned_data.get('password', None)
            user = authenticate(username=uname, password=password)
            if user is not None:
               login(request, user)
               messages.success(request, f'Congrats {request.user.username} You have successfuly logged in dashboard ')
               return redirect('dashboard')
            
        print(form.errors)
        return render(request, 'accounts/login.html',{'form': form})
            
class DashboardView(LoginRequiredMixin,View):
   def get(self, request):
        return render(request, 'accounts/dashboard.html')
     
class PasswordChangeView(LoginRequiredMixin, View):
   
    def get(self, request):
           form = ChangePassword(user=request.user)
           return render(request, 'accounts/changepassword.html', {'form': form})
        
    def post(self, request):
        if request.user.is_authenticated:
            user = request.user
            form = ChangePassword(user=user, data=request.POST)
            if form.is_valid():
                form.save()
                user = str(request.user).title()
                messages.success(request, f'Congrats! {user} Your Password Changed Successfuly ')
                return redirect('dashboard')
            return render(request, 'accounts/changepassword.html', {'form': form})
        else:
            return redirect('login')
            
class LogoutView(LoginRequiredMixin, View):

    def get(self, request):
        if request.user.is_authenticated:
            user = str(request.user).title()
            logout(request)
            messages.success(request, f'{user} Your Successfuly Logout Thanks From  Krishna(admin) To Visit Our Website!  ')
            return redirect('login')
        else:
            return redirect('login')         


class UpdateProfileView(LoginRequiredMixin, View):
    def get(self, request):
        profile = Profile.objects.get(user__username = request.user.username)
        form  = UserProfileForm(instance=profile)
        return render(request, 'accounts/update_profile.html', {'form': form})  
    
    def post(self, request):
        profile  = Profile.objects.get(user__username = request.user.username)
        form  = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congrats Your Profile Successfuly Updated!')
            return redirect('dashboard')
        return render(request, 'accounts/update_profile.html', {'form': form})  
        
