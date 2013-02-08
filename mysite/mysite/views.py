from django.shortcuts import render_to_response
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('newapp/current_datetime.html', {'current_date': now})
	
def my_homepage_view(request):
    now = datetime.datetime.now()
    return render_to_response('newapp/home.html', {'current_date': now})
	
def sample_page_view(request):
    now = datetime.datetime.now()
    return render_to_response('newapp/page2.html', {'current_date': now})
   