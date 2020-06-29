from django.db import models
from django.utils.text import slugify

# Create your models here.

class Job(models.Model):
    title=models.CharField(max_length=100)

    JOB_TYPE=(
        ('Full Time','Full Time'),
        ('Part Time','Part Time')
    )

    # Function to name file uploaded
    def uploadedfile(instance,filename):
        filename,ext=filename.split('.')
        return "jobs/%s.%s"%(instance.id,ext)

    job_type=models.CharField(max_length=15,choices=JOB_TYPE)
    description=models.TextField(max_length=1000)
    published_at=models.DateField(auto_now=True)
    vacancy= models.IntegerField(default=1)
    salary= models.IntegerField(default=0)
    experiance= models.IntegerField(default=1)
    category=models.ForeignKey('Category',on_delete=models.CASCADE)
    image=models.ImageField(upload_to=uploadedfile)


    slug=models.SlugField(blank=True, null=True)

    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Job,self).save(*args,**kwargs)

    def __str__(self):
        return self.title

class Category(models.Model):
    name=models.CharField(max_length=25)

    def __str__(self):
        return self.name