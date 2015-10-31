from django.contrib import admin

# Register your models here.

# ******** Step 14 addition start ********
from .models import Course
admin.site.register(Course)
# ********  Step 14 addition end  ********