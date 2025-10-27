from django.shortcuts import render
from .models import Job

# Create your views here.
def index(request):
    jobs = Job.objects.all()
    return render(request, 'job_posts/index.html', {
        'jobs':jobs
    })

def job(request, title):
    job = Job.objects.get(title = title)
    return render(request, 'job_posts/job.html',{
        'job': job
    })