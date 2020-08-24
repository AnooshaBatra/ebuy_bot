from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def dashboard(request):
	 return render(request, 'dashboard.html',{})
	#return HttpResponse("dashboarddd", content_type='text/plain')
@login_required
def log(request):
	 return render(request, 'log.html',{})



def launch(request):
	pass 