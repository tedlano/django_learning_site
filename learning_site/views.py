#from django.http import HttpResponse  # Step 19.4 removed
from django.shortcuts import render    # Step 19.4 added

def hello_world(request):
    return render(request, 'home.html')  # Step 19.4 added
    #return HttpResponse('Hello World')  # Step 19.4 removed