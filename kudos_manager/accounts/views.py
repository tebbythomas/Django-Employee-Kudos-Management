from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from profiles.models import Profile
from companies.models import Company


# Function handling account registration
def register(request):
    if request.method == 'POST':
        # Retrieving all details from POST request
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        # Setting the email as the username
        username = request.POST['email']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2'] 
        company_count = Company.objects.all().count()
        # Adding new company if no companies currently stored
        if company_count == 0:
            if request.POST['newCompanyInput'] == '':
                messages.error(request, 'Please enter a company name')
                return redirect('register')
            company_name = request.POST['newCompanyInput']
        else:
            # Checking if a new company was entered and storing it
            if 'newCompanyInput' in request.POST and request.POST['newCompanyInput']!= '':
                company_name = request.POST['newCompanyInput']
            else:
                company_name = request.POST['company']
        if password == password2:
            # Check username
            if ' ' in username:
                messages.error(request, 'Email cannot have spaces')
                return redirect('register')
            if User.objects.filter(username__iexact=username).exists():
                messages.error(request, 'That email is taken')
                return redirect('register')
            elif User.objects.filter(email__iexact=email).exists():
                messages.error(request, 'That email is being used')
                return redirect('register')
            else:
                # Store user detals
                email = email.lower()
                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, username=username, password=password, email=email)
                user.save()
                if Company.objects.filter(name=company_name).exists():
                    companyObj = Company.objects.get(name=company_name)
                else:
                    companyObj = Company(name=company_name)
                    companyObj.save()
                profile = Profile(user=user, company=companyObj)
                profile.save()

                messages.success(
                    request, 'You are now registered and can login')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        # Retrieving the list of companies to populate the dropdown during registration
        companies = Company.objects.all()
        context = {
            "companies": companies
        }
        return render(request, 'accounts/register.html', context)


# Function handling user login
def login(request):
    if request.method == 'POST':
        # Retrieving the credentials from the POST request
        username = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


# Function to handle account logout
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('login')
    return redirect('login')
