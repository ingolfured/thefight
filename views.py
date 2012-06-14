from django.shortcuts import render_to_response
import datetime

def home(request):
    return render_to_response('index.html', {'timi': datetime.datetime.now()})
