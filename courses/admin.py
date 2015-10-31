from django.contrib import admin

from.models import Course, Step     # Step 14 and 23.3 additions

# Step 23.4 addition
class StepInline(admin.StackedInline):
    model = Step

# Step 23.4 addition
class CourseAdmin(admin.ModelAdmin):
    inlines = [StepInline,]

admin.site.register(Course, CourseAdmin)         # Step 14 addition, 23.4 mod
admin.site.register(Step)           # Step 23.3 addition