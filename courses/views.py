# from django.http import HttpResponse # Step 14 addition # Step 18.3 comment
from django.shortcuts import render, get_object_or_404  # Step 25.1 mod

from .models import Course, Step  # Step 14 add, Step 26.1 add

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
    # course = Course.objects.get(pk=pk)        # Step 25.1 com
    course = get_object_or_404(Course, pk=pk)   # Step 25.1 add
    return render(request,  'courses/course_detail.html', {'course': course})
    
# Step 26.1 Addition
def step_detail(request, course_pk, step_pk):
    step = get_object_or_404(Step, course_id=course_pk, pk=step_pk)
    return render(request, 'courses/step_detail.html', {'step': step})
    
    
    
    
    