from django.db import models

# Create your models here.
class Job(models.Model):
    company = models.CharField(max_length=500)
    title = models.TextField()
    com_description = models.TextField()
    job_details = models.JSONField(default=dict, blank=True)
    job_description = models.TextField()
    link = models.URLField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f"{self.company} : {self.title}")