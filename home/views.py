from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'home/welcome.html', {'today': datetime.today()})


@login_required
def authorized(request):
    return render(request, 'home/authorized.html', {})
