from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import subprocess, os

# Create your views here.
@login_required
def dashboard(request):
	 return render(request, 'dashboard.html',{})
	#return HttpResponse("dashboarddd", content_type='text/plain')
	

@login_required
def log(request):
    info_path = r'C:\Users\Administrator\Desktop\transviti\ebuy_automation\log.info'
    error_path = r'C:\Users\Administrator\Desktop\transviti\ebuy_automation\log.error'
    run_status = r'C:\Users\Administrator\Desktop\transviti\ebuy_automation\status.log'
    
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
    if os.path.exists(run_status):
        f = open(run_status)
        status = f.readline().strip()
        if status == 'running':
            result['status'] = 'Already Running'
    
        elif status == 'stopped':
            result['status'] = 'Not Running'
        f.close()
            
    with open(info_path) as log_info:
        for line in log_info:
            key = line.split('::')[0].strip()
            value = line.split('::')[1].strip()
            result['log_info'][key] = value
    
    with open(error_path) as log_error:
        result['log_error']=log_error.read()
    print("result:",result)
    return render(request,'log.html',context=result)

   
            

def launch(request):
    
    info_path = r'C:\Users\Administrator\Desktop\transviti\ebuy_automation\log.info'
    error_path = r'C:\Users\Administrator\Desktop\transviti\ebuy_automation\log.error'
    run_status = r'C:\Users\Administrator\Desktop\transviti\ebuy_automation\status.log'
    
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
    
    
            
    
    with open(info_path) as log_info:
        for line in log_info:
            key = line.split('::')[0].strip()
            value = line.split('::')[1].strip()
            result['log_info'][key] = value
    
    with open(error_path) as log_error:
        result['log_error']=log_error.read()
    
    
    
    
    
    run_status = r'C:\Users\Administrator\Desktop\transviti\ebuy_automation\status.log'
    if os.path.exists(run_status):
        f = open(run_status)
        status = f.readline().strip()
        f.close()
        if status == 'running':
            result['status'] = 'Already Running'
            return render(request,'log.html',context=result)
        elif status == 'stopped':
            try:
                os.remove(run_status)
                f = open(run_status,'w')
                f.write('running')
                f.close()
                subprocess.run([r'C:\Users\Administrator\Desktop\transviti\ebuy_automation\run_from_web_app.bat'])
                print("writing stopp")
                os.remove(run_status)
                f = open(run_status,'w')
                f.write('stopped')
                f.close()
            except:
                os.remove(run_status)
                f = open(run_status,'w')
                f.write('stopped')
                f.close()
                return HttpResponse("Something Went Wrong",status=404)
            result['status'] = 'Not Running'
            return render(request,'log.html',context=result)
    else:
        try:
            f = open(run_status,'w')
            f.write('running')
            f.close()
            subprocess.run([r'C:\Users\Administrator\Desktop\transviti\ebuy_automation\run_from_web_app.bat'])
            print("writing stopp")
            os.remove(run_status)
            f = open(run_status,'w')
            f.write('stopped')
            f.close()
        except:
            os.remove(run_status)
            f = open(run_status,'w')
            f.write('stopped')
            f.close()
            return HttpResponse("Something Went Wrong",status=404)
        result['status'] = 'Not Running'
        return render(request,'log.html',result)
        
    
     
