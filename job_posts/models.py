from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class Job(models.Model):
    company = models.CharField(max_length=500)
    title = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    logo = models.ImageField(upload_to='company_logos/', null=True, blank=True)
    com_description = models.TextField()
    two_line_des = models.TextField()
    job_details = models.JSONField(default=dict, blank=True)
    job_description = RichTextField()
    link = models.URLField()
    date = models.DateField(auto_now_add=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return (f"{self.company} : {self.title}")