from django.shortcuts import render
from django.contrib.auth.forms import PasswordChangeForm,UserCreationForm
from elearning.forms import editprofileform
from .models import session,lecturer
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
# Create your views here.


def about_view(request):
    context = {}
    return render(request, "about.html", context)


def session_view(request):
    sessions = session.objects.all()
    context = {
        "sessions": sessions
    }
    return render(request, "session.html", context)


def class_view(request, my_id):
    session_class = session.objects.get(id=my_id)
    context = {
        "class": session_class
    }
    return render(request, "class.html", context)


def lecturers_view(request):
    lecturers=lecturer.objects.all()
    context={
        "lecturers":lecturers,
    }
    return render(request,"lecturers.html",context)

def lecturer_view(request, my_id):
    lecturer_s = lecturer.objects.get(id=my_id)
    sessions = session.objects.all()

    context = {
        "lecturer":lecturer_s,
        "sessions":sessions 
    }
    return render(request, "lecturer.html", context)

class user_register_view(generic.CreateView):
    form_class=UserCreationForm
    template_name="registration/register.html"
    success_url=reverse_lazy("login")


class user_edit_view(generic.UpdateView):
    form_class=editprofileform
    template_name="registration/edit_profile.html"
    success_url=reverse_lazy('home')

    def get_object(self):
        return self.request.user

class passwordschangeview(PasswordChangeView):
    form_class=PasswordChangeForm
    success_url=reverse_lazy('password_success')

def password_success(request):
    return render(request,"registration/password_success.html",{})
    