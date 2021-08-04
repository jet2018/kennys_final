
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.db.models import query
from django.http.response import JsonResponse
from app.forms import MyCoverageForm
import datetime
from django import template
from employees.models import DailyPerfomance
from authentication.models import AddEmployer
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from employees.models import DailyPerfomance
from django.views.generic import TemplateView, DetailView, ListView
from django.shortcuts import render
# from django.template.base import


now = datetime.datetime.now()
# sweek = calendar.setlastweekday(calendar.FRIDAY)
today = now.date()
time = now.time()
year = now.year
month = now.month
day = now.day
get_week = datetime.datetime.strptime(
    str(datetime.date.today()), "%Y-%m-%d")
# getting the current week of the year
week_of_year = int(get_week.strftime("%V"))


class ProfileView(TemplateView):
    template_name = "profile.html"


def UploadProfilePik(request):
    if request.method == 'POST' or request.is_ajax():
        Image = request.FILES.get('image')
        message = ""
        try:
            myprofile = AddEmployer.objects.get(user=request.user)
            myprofile.user_image = Image
            myprofile.save()
            message = "Uploaded"
        except AddEmployer.DoesNotExist:
            message = "Error, try again"
        return JsonResponse({"message": message})


def ResetPasword(request):
    if request.method == 'POST' and request.is_ajax():
        if request.POST.get('old_password') != '' and request.POST.get('new_password') != '':
            current_password = request.user.password
            matchcheck = check_password(
                request.POST.get('old_password'), current_password)
            if matchcheck:
                user = User.objects.get(pk=request.user.id)
                user.set_password(request.POST.get('new_password'))
                user.save()
                return JsonResponse({"message": 'Password updated successfully, logging you out!', "code": True})
            else:
                return JsonResponse({"message": 'No account is associated with the given password!', "code": False})
        else:
            return JsonResponse({"message": 'Some fields are still empty', "code": False})
    return redirect(request.user.username+'/profile')


def PaymentsListView(request):
    last_month = DailyPerfomance.objects.filter(
        Employer__user=request.user, date__month=month-1)
    daily_all = DailyPerfomance.objects.filter(
        Employer__user=request.user)
    last_year = DailyPerfomance.objects.filter(
        Employer__user=request.user, date__year=int(year-1))
    this_month = DailyPerfomance.objects.filter(
        Employer__user=request.user, date__month=month)
    last_week = DailyPerfomance.objects.filter(
        Employer__user=request.user, date__week=int(week_of_year-1))
    # get the total of the last amount
    last_month_all = []
    for lmonth in last_month:
        last_month_all.append(
            int(lmonth.Employer.hourly_charge.amount)*lmonth.hours_worked)
    total_last_month_all = sum(last_month_all)

    # get the total of the last year
    this_month_all = []
    for tmonth in this_month:
        this_month_all.append(
            int(tmonth.Employer.hourly_charge.amount)*tmonth.hours_worked)

    total_this_month_all = sum(this_month_all)

    # get the total of the last year
    last_year_all = []
    for lyear in last_year:
        last_year_all.append(
            int(lyear.Employer.hourly_charge.amount)*lyear.hours_worked)

    total_last_year_all = sum(last_year_all)

    # get the total of the last year
    last_week_all = []
    for lweek in last_week:
        last_week_all.append(
            int(lweek.Employer.hourly_charge.amount)*lweek.hours_worked)
    total_last_week_all = sum(last_week_all)

    return render(request, 'payments.html', {
        'last_month': total_last_month_all,
        'last_year': total_last_year_all,
        'daily': daily_all,
        'this_month': total_this_month_all,
        'last_week': total_last_week_all
    })


# class PerformanceView(ListView):
#     model = DailyPerfomance
#     template_name = "performance.html"
#     context_object_name = "performances"

#     # redefining the queeryset to pick where the month is the current one

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         queryset = DailyPerfomance.objects.filter(
#             Employer__user=self.request.user, date__month=month)
#         return queryset


def UserUpdate(request):
    """Update user information"""
    if request.is_ajax() and request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        user.save()
        return JsonResponse({"code": True})
    return redirect(request.user.username+'/profile')


def UserPhoneAndAddress(request):
    """Update user information"""
    if request.is_ajax() and request.method == 'POST':
        location = request.POST.get('address')
        phone = request.POST.get('phone')

        user = AddEmployer.objects.get(user=request.user)
        user.location = location
        user.phone = phone
        user.save()
        return JsonResponse({"code": True})
    return redirect(request.user.username+'/profile')


def UserJobTitle(request):
    """Update user information"""
    if request.is_ajax() and request.method == 'POST':
        title = request.POST.get('job_title')

        user = AddEmployer.objects.get(user=request.user)
        user.job_title = title
        user.save()
        return JsonResponse({"code": True})
    return redirect(request.user.username+'/profile')


@login_required(login_url="/login/")
def index(request):

    context = {}
    context['segment'] = 'index'
    context['form'] = MyCoverageForm()
    context['emp'] = AddEmployer.objects.get(user=request.user)
    try:
        context['todays'] = DailyPerfomance.objects.get(
            Employer__user=request.user, date__day=day)
    except DailyPerfomance.DoesNotExist:
        context['todays'] = None

    try:
        context['yesto'] = DailyPerfomance.objects.get(
            Employer__user=request.user, date__day=day-1)
    except DailyPerfomance.DoesNotExist:
        context['yesto'] = None

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))


# uodate/add daily coverage
def UpdateAddDailyCoverage(request):
    if request.method == 'POST':
        todays = DailyPerfomance.objects.get(
            Employer__user=request.user, date__day=day)
        todays.daily_coverage = request.POST.get('daily_coverage')
        todays.save()
    return redirect("/")


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))
