from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home/welcome.html', {'today': datetime.today()})


@login_required(login_url='/admin')
def authorized(request):
    return render(request, 'home/authorized.html', {})
