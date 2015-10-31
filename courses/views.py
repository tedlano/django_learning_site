# from django.http import HttpResponse # Step 14 addition # Step 18.3 comment
from django.shortcuts import render

from .models import Course  # Step 14 addition

# Step 14 addition
def course_list(request):   
    courses = Course.objects.all()
    
    # Step 18.3 Addition
    return render(request, 'courses/course_list.html', {'courses': courses})
    
    """ Step 18.3 Commented out
    output = ', '.join([str(course) for course in courses])
    return HttpResponse(output)
    """
  
# Step 22.1 addition  
def course_detail(request, pk):
    course = Course.objects.get(pk=pk)
    return render(request,  'courses/course_detail.html', {'course': course})
    