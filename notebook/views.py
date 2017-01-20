import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.core.urlresolvers import reverse
from django.views.generic import CreateView
from django.contrib import auth
from django.template.context_processors import csrf

from .forms import NameForm
from notebook.models import NoteNames

Flag = 0

def home(request):
    args = {}
    args.update(csrf(request))
    auth.logout(request)
    global Flag
    Flag=0
    if request.POST:
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            next_page = request.GET.get('next')
            if next_page:
                return redirect(next_page)
            return redirect('table')
        else:
            args['login_error'] = "User not found"
            return render(request, 'notebook/home.html', args)
    return render(request, 'notebook/home.html')


@login_required
def table(request):
    global Flag
    globalFlag = Flag
    now = datetime.datetime.now()
    if Flag==0:
        Flag+=1
    noteNames = NoteNames.objects.all()
    list = NoteNames.objects.filter(dateOfBirth__month=now.month, dateOfBirth__day=now.day)
    context = {
        'noteNames': noteNames,
        'globalFlag': globalFlag,
        'list': list
    }
    return render(request, 'notebook/table.html', context)


@login_required
def addnote(request):
    form = NameForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('table')
        else:
            return render(request, 'notebook/addnote.html', locals())
    return render(request, 'notebook/addnote.html', locals())


@login_required
def removenote(request, noteId):
    n = NoteNames.objects.get(pk=noteId)
    n.delete()
    return redirect('table')

@login_required
def editnote(request, noteId):
    note = get_object_or_404(NoteNames, pk=noteId)
    form = NameForm(request.POST or None, instance=note)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('table')
        else:
           return render(request, 'notebook/editnote.html', locals())
    return render(request, 'notebook/editnote.html', locals())


def logout(request):
    global Flag
    Flag=0
    auth.logout(request)
    return redirect('home')
