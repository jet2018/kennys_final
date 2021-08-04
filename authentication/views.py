
from django.contrib.auth.decorators import login_required
from authentication.models import AddEmployer
from employees.models import DailyPerfomance

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, auth
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm
import datetime

now = datetime.datetime.now()

today = now.date()
time = now.time()
year = now.year
month = now.month
day = now.day
# yesto = now.day-1
# print(yesto)


# login view. Handles caapturing users entry time
def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                # login the user
                emp = AddEmployer.objects.get(user=user)

                # check if the user had logged in sometime back today
                try:
                    cur_user_instance = User.objects.get(username=username)
                    msg = 'Welcome back, '+username
                except User.DoesNotExist:
                    msg = 'User does not exist'
                # if they have, then just log them in.
                if cur_user_instance.last_login and cur_user_instance.last_login.date() == today:
                    msg = "Welcome back "+username
                    login(request, user)
                # otherwise, record their login time
                else:
                    # record the their time of login
                    daily_check = DailyPerfomance(
                        Employer=emp, checked_in_at=time)
                    daily_check.save()
                    login(request, user)
                return redirect("/",  {"msg": msg})
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):

    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})


@login_required(login_url='/login/')
def logout(request):
    try:
        print(time)
        # login the user
        emp = AddEmployer.objects.get(user=request.user)
        print(emp)
        # record the their time of login
        try:
            check = DailyPerfomance.objects.filter(
                Employer=emp, date__day=day)
            daily_check = check[0]
            daily_check.checked_out_at = time

            daily_check.save()
            auth.logout(request)
        except DailyPerfomance.DoesNotExist:
            pass
    except AddEmployer.DoesNotExist:
        pass
    return redirect("/")
