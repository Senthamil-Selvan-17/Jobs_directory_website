from django.shortcuts import render
from .models import Job
from django.utils import timezone
from datetime import timedelta

# Create your views here.
def index(request):
    one_week_data = timezone.now().date() - timedelta(days=7)  # it gives the date before seven days which used in filter to give data after that date
    jobs = Job.objects.all().filter(date__gte = one_week_data).order_by('-date') #it gives data in descending,  gte is lookup which means greater than or equal to  
    return render(request, 'job_posts/index.html', {
        'jobs':jobs
    })

def job(request, slug):
    jobs = Job.objects.all()
    job = Job.objects.get(slug = slug)
    return render(request, 'job_posts/job.html',{
        'job': job, 'jobs':jobs
    })