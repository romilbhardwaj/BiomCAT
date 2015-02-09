from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from BiomCAT.forms import TestSubjectForm
from BiomCAT.models import TestSubject, ControlGroup
import django.core.exceptions

# Create your views here.

def home(request):
    return render(request, 'home.html')

def training(request):
    if request.method == 'POST':
        form = TestSubjectForm(request.POST)
        if form.is_valid():
            newTestSubject = form.save(commit=False)
            request.user.testsubject = newTestSubject
            user_count = len(User.objects.all())
            newTestSubject.control_group = ControlGroup.objects.get(name = str(user_count%2))
            newTestSubject.save()
            form.save_m2m()
            request.user.save()
            return HttpResponseRedirect('/training/')

    else:
        try:
            request.user.testsubject
        except TestSubject.DoesNotExist:
            form = TestSubjectForm()
            return render(request, 'newuser.html', {'form': form})
    return render(request, 'training.html')

def question(request):
    return render(request, 'testing.html')