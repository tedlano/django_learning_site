from django.db import models

# Create your models here.

# Step 8 addition
class Course(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
# End Step 8 addition 

    # Step 13.1 addition
    def __str__(self):
        return self.title
        
# Step 23.1 addition
class Step(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField(blank=True, default='')    # Step 26.4 add
    order = models.IntegerField(default=0)
    course = models.ForeignKey(Course)
    
    # sTEP 24.1 addition
    class Meta:
        ordering = ['order',]
    
    def __str__(self):
        return self.title