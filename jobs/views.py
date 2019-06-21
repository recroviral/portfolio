from django.shortcuts import render, get_object_or_404
from .models import jobs
# Create your views here.
def home(request):
    query = jobs.objects.all()
    return render(request,'jobs/index.html', {'myjobs':query})

def detail(request, job_id):
    job_detail = get_object_or_404(jobs, pk=job_id)
    return render(request, 'jobs/detail.html', {'myjobs': job_detail})
