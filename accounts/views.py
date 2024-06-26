# Views for accounts app

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, LoginForm, PasswordChangeForm

# Register View
def registerView(request):
    # Processing the submitted registration form
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if (register_form.is_valid()):
            user = register_form.save()
            return HttpResponse("register success")
        else:
            messages.error(request, "Invalid data, Try again..!")
            
    #Creating the forms
    register_form = RegisterForm()
    context = {
        'register_form' : register_form,
        'title' : "Register as Candidate",
    }
    return render(request, 'accounts/register.html', context)

# Login View
def loginView(request):
    # View for login page
    login_form = LoginForm(request)
    if request.method == 'POST':
        login_form = LoginForm(data = request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                if user.is_official:
                    return redirect('official_dashboard')
                elif user.is_applicant:
                    return redirect('applicant_dashboard')
        else:
             messages.error(request, "Invalid username or password.")
    context = {
            'login_form' : login_form,
            'title'      : 'Login',
    }
    return render(request, 'accounts/login.html', context)

# Logout View
def logoutView(request):
    logout(request)
    #messages.info(request, "Logged out successfully.")
    return redirect('home')

# Password Reset View
@login_required
def passwordResetView(request):
    data = dict()
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            data['form_is_valid'] = True
            data['message'] = '<div class="alert alert-success alert-dismissible fade show" role="alert"><span class="alert-icon"><i class="ni ni-like-2"></i></span><span class="alert-text">Password Changed Successfully</span><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>'
        else:
            data['message'] = '<div class="alert alert-danger" role="alert">Invalid Credentials! Try again</div>'
    else:
        form = PasswordChangeForm(request.user)
        data['html_form'] = render_to_string('accounts/change_password.html', { 'form' : form }, request = request)
    return JsonResponse(data)

