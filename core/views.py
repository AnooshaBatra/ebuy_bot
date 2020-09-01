from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login as auth_login
import subprocess, os
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from core.models import EBUYRFQ
# Create your views here.


info_path = r"C:\Users\Administrator\Desktop\transviti\ebuy_automation\log.info"
error_path = r'C:\Users\Administrator\Desktop\transviti\ebuy_automation\log.error'
run_status = r'C:\Users\Administrator\Desktop\transviti\ebuy_automation\status.log'
bat_file = r'C:\Users\Administrator\Desktop\transviti\ebuy_automation\run_from_web_app.bat'

def Login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user=authenticate(username= username, password=password)
		if user is not None:
		 	print("authenticated")
		 	if user is not None:
		 		if user.is_active:
		 			auth_login(request, user)
		 			return redirect('index')
		 		else:
		 			messages.error(request,'username or password not correct')
		 			return redirect('login')
		 	else:
		 		form = AuthenticationForm()
		 		return render(request, 'todo/login.html', {'form': form})
	#return HttpResponse("dashboarddd", content_type='text/plain')

# @login_required
# def log(request):
# 	return render(request, 'log.html',{})


@login_required
def dash(request):
	return render(request, 'dashboard.html',{})

@login_required
def logout(request):
    logout(request)

# def launch(request):
# 	pass

@login_required
def log(request):
    # info_path = r'C:\Users\Administrator\Desktop\transviti\ebuy_automation\log.info'
    # error_path = r'C:\Users\Administrator\Desktop\transviti\ebuy_automation\log.error'
    # run_status = r'C:\Users\Administrator\Desktop\transviti\ebuy_automation\status.log'
    res= None
    try:
        res= EBUYRFQ.objects.all().filter(bot_name= "eb").order_by('id').last()
    except Exception as e:
        print(e)
    result = {
		'log_info' : {
		'name': 'Ebuy Automation',
		'source' : 'Unknown',
		'last_run': 'Unknown',
		'tables':'Unkown',
		'total_time':'Unknown',
		'status':'Unknown'
		}
	}
    if res != None:
        result['log_info']['name'] = res.info_name
        result['log_info']['source'] = res.info_source
        result['log_info']['last_run'] = res.last_run 
        result['log_info']['tables'] = res.tables_count
        result['log_info']['total_time'] = res.total_run_time
        result['log_error']= res.log_error
        status = res.status
        if status == 'running':
            result['status'] = 'Please wait! Bot is already running'
        elif status == 'stopped':
            result['status'] = 'Bot is not running'
        else:
            result['result'] = '404 - Status file not found'
    return render(request,'log.html',context=result)
   
            

def launch(request):
    
    # info_path = r'C:\Users\Administrator\Desktop\transviti\ebuy_automation\log.info'
    # error_path = r'C:\Users\Administrator\Desktop\transviti\ebuy_automation\log.error'
    # run_status = r'C:\Users\Administrator\Desktop\transviti\ebuy_automation\status.log'
    
    result = {
 		'log_info' : {
 		'name': 'Ebuy Automation',
 		'source' : 'Unknown',
 		'last_run': 'Unknown',
 		'tables':'Unkown',
 		'total_time':'Unknown',
 		'status':'Unknown'
		}
	}
    res= None
    try:
        res= EBUYRFQ.objects.all().filter(bot_name= "eb").order_by('id').last()
    except Exception as e:
        print(e)
    if res != None:
        result['log_info']['name'] = res.info_name
        result['log_info']['source'] = res.info_source
        result['log_info']['last_run'] = res.last_run 
        result['log_info']['tables'] = res.tables_count
        result['log_info']['total_time'] = res.total_run_time 
        result['log_error']=res.log_error
    else:
        result['log_info'] = '404 - Runtime info file not found'
        result['log_error'] = '404 - Error file not found'
    
     
    #run_status = r'C:\Users\Administrator\Desktop\transviti\ebuy_automation\status.log'
    try:
        status = res.status
        if status == 'running':
            result['alert'] = 'Please wait! Bot is already running'
            result['status'] = 'Please wait! Bot is already running'
            return render(request,'log.html',context=result)
        elif status == 'stopped':
            try:
                res.status= 'running'
                res.save()
                subprocess.run([bat_file])
                res.status="stopped"
                res.save()
            except:
                res.status= 'stopped'
                res.save()
                result['status'] = 'Bot is not running'
                result['alert'] = 'Something went wrong'
                return render(request,'log.html',result)
            result['alert'] = 'Bot is starting...'
            result['status'] = 'Please wait! Bot is already running'
            return render(request,'log.html',context=result)
        else:
            try:
                res.status= 'running'
                res.save()
                subprocess.run([bat_file])
                res.status= "stopped"
                res.save()
            except:
                res.status= 'stopped'
                res.save()
                result['status'] = 'Bot is not running'
                result['alert'] = 'Something went wrong'
                return render(request,'log.html',result)
            result['alert'] = 'Bot is starting...'
            result['status'] = 'Please wait! Bot is already running'
            return render(request,'log.html',result)
    except:
        return HttpResponse("Something went wrong",status=404)
        
 
