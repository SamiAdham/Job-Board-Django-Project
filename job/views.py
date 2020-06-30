from django.shortcuts import render
from . models import Job
from django.core.paginator import Paginator
from .form import Apply_Form,Add_job

# Create your views here.
def job_list(request):
    job_list=Job.objects.all()
    paginator = Paginator(job_list, 20) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={
        'jobs':page_obj
    }
    return render(request,'job/job_list.html',context)


def job_detail(request,slug):
    job_detail=Job.objects.get(slug=slug)

    # if click apply do soemthing

    if request.method=='POST':
        form=Apply_Form(request.POST, request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.job=job_detail
            myform.save()
    
    else:
        form=Apply_Form()
    

    context={
        'job':job_detail,
        'form':form
    }
    return render(request,'job/job_detail.html',context)


def add_job(request):

    # if click apply do soemthing

    if request.method=='POST':
        form=Add_job(request.POST, request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.job=job_detail
            myform.save()
        
    
    else:
        form=Add_job()
    

    context={
        'form':form,
    }
    return render(request,'job/add_job.html',context)