from django.shortcuts import render,HttpResponse
NUM_OF_PROJECTS=7
# Create your views here.
def home(request):
    context={
        'no_of_projects':[x for x in range(1,NUM_OF_PROJECTS+1)],
    }
    return render(request,'home/index.html',context=context)

def project(request,number):
    return render(request,'home/'+str(number)+'.html')