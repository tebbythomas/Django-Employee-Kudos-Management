from django.shortcuts import render, redirect
from django.http import HttpResponse
from profiles.models import Profile, KUDOS_COUNT_DEFAULT
from kudos.models import Kudo
from companies.models import Company
from django.contrib.auth.models import User
from django.contrib import messages, auth
import datetime
import csv, io


# Function to check if the Kudos count has not been reset and needs to be reset
def kudosReset(request, current_user):
    # To get the date of the Monday of the current week
    currentDate = datetime.date.today()
    startWeekCurrent = currentDate - datetime.timedelta(currentDate.weekday())
    # Retrieve the profile of the current user
    profile = Profile.objects.get(user=current_user)
    # Retrieve the date of the Monday of the week the kudos was last updated
    kudosLastUpdatedDate = profile.kudosLastUpdated.date()
    startWeekKudos = kudosLastUpdatedDate - datetime.timedelta(kudosLastUpdatedDate.weekday())
    # If the current Monday and the Monday of the last Kudos reset are not same 
    #  then reset the kudos count and last updated fields
    if startWeekCurrent != startWeekKudos:
        Profile.objects.filter(user=current_user).update(kudosCount=KUDOS_COUNT_DEFAULT, kudosLastUpdated=datetime.datetime.now())
        messages.success(
                request, 'New week - Kudos Count Reset!')
    return


# Function to handle requests to the home page / dashboard
def index(request):
    # To only allow access to logged in users
    if not request.user.is_authenticated:
        # If they aren't logged in redirect them to the login page
        return render(request, 'accounts/login.html')
    # Get current user
    current_user = User.objects.get(username=request.user)
    # Reset the current user's kudos count if needed
    kudosReset(request, current_user)
    # POST request called when a Kudos is sent
    if request.method == 'POST':
        to_colleague_username = request.POST['to_colleague']
        message = request.POST['message']
        if User.objects.filter(username__exact=to_colleague_username).exists():
            toColleague = User.objects.get(username=to_colleague_username)
            fromColleague = current_user
            kudo = Kudo(fromColleague=current_user,
                        toColleague=toColleague, message=message)
            kudo.save()
            profile = Profile.objects.get(user=current_user)
            # The user who sent the kudos has his/her count decremented by 1
            newKudos = profile.kudosCount - 1
            Profile.objects.filter(user=current_user).update(
                kudosCount=newKudos)
            messages.success(
                request, 'Kudos successfully given!')

    # Get current user's profile    
    current_profile = Profile.objects.get(user=current_user)
    colleagues_profiles = Profile.objects.filter(company=current_profile.company)
    colleagues = list()
    # Get list of colleagues
    for profile in colleagues_profiles:
        if profile.user.username != current_user.username:
            colleagues.append(profile)
    kudos_given = Kudo.objects.filter(fromColleague=current_user)
    kudos_received = Kudo.objects.filter(toColleague=current_user)

    context = {
        'profile': current_profile,
        'colleagues': colleagues,
        'kudos_given': kudos_given,
        'kudos_received': kudos_received
    }
    if current_profile.kudosCount == 0:
        # Prevent sending of Kudos
        context['noMoreKudos'] = True
    return render(request, 'pages/index.html', context)


# Function to save individual uploaded employee data
def save_employee_data(request, employee_data, line_count):
    line_count = line_count + 1
    if User.objects.filter(username__iexact=employee_data['email']).exists():
        messages.error(request, f"Error! Line: {line_count} {employee_data['email']} email is taken")
        return redirect('upload_employees')
    elif User.objects.filter(email__iexact=employee_data['email']).exists():
        messages.error(request, f"Error! Line: {line_count} {employee_data['email']} email is taken")
        return redirect('upload_employees')
    else:
        # Store user detals
        email = employee_data['email'].lower()
        user = User.objects.create_user(
            first_name=employee_data['first_name'], last_name=employee_data['last_name'], username=employee_data['email'], password=employee_data['password'], email=employee_data['email'])
        user.save()
        companyObj = None
        if Company.objects.filter(name=employee_data['company']).exists():
            companyObj = Company.objects.get(name=employee_data['company'])
        else:
            companyObj = Company(name=employee_data['company'])
            companyObj.save()
        profile = Profile(user=user, company=companyObj)
        profile.save()
    return


# Function to upload employees
def upload_employees(request):
    if request.method == 'POST':
        if not request.FILES['upload_employees_file'].name.endswith('.csv'):
            messages.error(request, 'Uploaded file is not a CSV')
            return render(request, 'pages/upload_employees.html')
        # Encoding CSV file
        csv_file = io.TextIOWrapper(request.FILES['upload_employees_file'].file, encoding=request.encoding)
        csv_reader = csv.reader(csv_file, delimiter=',')
        # Reading CSV file
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                employee_data = dict()
                employee_data["first_name"] = row[0].strip()
                employee_data["last_name"] = row[1].strip()
                employee_data["company"] = row[2].strip()
                employee_data["email"] = row[3].strip()
                employee_data["password"] = row[4].strip()
                # Save individual row of employee data
                save_employee_data(request, employee_data, line_count)
                line_count += 1
        print(f'Processed {line_count} lines.')
        messages.success(
                request, 'Employee details succesfully uploaded and saved')
    return render(request, 'pages/upload_employees.html')


# Function to save individual kudos data
def save_kudos_data(request, kudos_data, line_count):
    line_count = line_count + 1
    # Checking if colleague who is sending or giving the kudos exists
    from_colleague_name = kudos_data['from_name'].split()
    from_colleague = None
    try:
        from_colleague = User.objects.get(first_name=from_colleague_name[0], last_name=from_colleague_name[1])
    except User.DoesNotExist:
        messages.error(request, f"Error! Line: {line_count} User: {kudos_data['from_name']} doesn't exist yet")
        return render(request, 'pages/upload_kudos.html')
    # Checking if colleague who is receiving the kudos exists
    to_colleague_name = kudos_data['to_name'].split()
    to_colleague = None
    try:
        to_colleague = User.objects.get(first_name=to_colleague_name[0], last_name=to_colleague_name[1])
    except User.DoesNotExist:
        messages.error(request, f"Error! Line: {line_count} User: {kudos_data['to_name']} doesn't exist yet")
        return render(request, 'pages/upload_kudos.html')
    if from_colleague == to_colleague:
        messages.error(request, f"Error! Line: {line_count} User: {kudos_data['from_name']} is sending a kudos to himself / herself which isn't allowed")
        return render(request, 'pages/upload_kudos.html')
    if Profile.objects.get(user=from_colleague).company != Profile.objects.get(user=to_colleague).company:
        messages.error(request, f"Error! Line: {line_count} User: {kudos_data['from_name']} is sending kudos to {kudos_data['to_name']} who is not in the same company")
        return render(request, 'pages/upload_kudos.html')
    if Profile.objects.get(user=from_colleague).kudosCount == 0:
        messages.error(request, f"Error! Line: {line_count} User: {kudos_data['from_name']} has 0 kudos left to send to {kudos_data['to_name']}")
        return render(request, 'pages/upload_kudos.html')
    message = kudos_data['message']
    kudo = Kudo(fromColleague=from_colleague,
                toColleague=to_colleague, message=message)
    kudo.save()
    profile = Profile.objects.get(user=from_colleague)
    # The user who sent the kudos has his/her count decremented by 1
    newKudos = profile.kudosCount - 1
    Profile.objects.filter(user=from_colleague).update(
        kudosCount=newKudos)
    return


# Function to upload kudos
def upload_kudos(request):
    if request.method == 'POST':
        if not request.FILES['upload_kudos_file'].name.endswith('.csv'):
            messages.error(request, 'Uploaded file is not a CSV')
            return render(request, 'pages/upload_kudos.html')
        # Encoding csv
        csv_file = io.TextIOWrapper(request.FILES['upload_kudos_file'].file, encoding=request.encoding)
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                kudos_data = dict()
                kudos_data['from_name'] = row[0].strip()
                kudos_data['to_name'] = row[1].strip()
                kudos_data['message'] = row[2].strip()
                # Save each row of kudos data
                save_kudos_data(request, kudos_data, line_count)
                line_count += 1
        print(f'Processed {line_count} lines.')
        messages.success(
                request, 'Kudos details succesfully uploaded and saved')
    return render(request, 'pages/upload_kudos.html')
