from django.db import models

# Create your models here.
class opentime(models.Model):
    available_time=models.DateField('Available Day')
    available_from=models.TimeField('Available from')
    available_until=models.TimeField('Available Until')
    message=models.CharField(max_length=200)
    
    def __str__(self):
        return self.message













