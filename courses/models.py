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