from django.shortcuts import render,HttpResponse
from .models import student
# Create your views here.
def index(request):
    if request.method=='POST' :
        name=request.POST.get('name')
        email=request.POST.get('email')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        class1=request.POST.get('class1')
        reg=request.POST.get('reg')
        test=request.POST.get('test')
        print("name is",name,email,dob,gender,class1,reg,test)
        if (float(test)>100) :
            return HttpResponse("Invalid test score")
        obj=student()
        obj.name=name
        obj.email=email
        obj.dob=dob
        obj.gender=gender
        obj.class1=class1
        obj.reg=reg
        obj.test=test
        obj.save()
        return HttpResponse("<h1> Data saved successfully</h1>") 
    return render(request,'index.html')
def list(request):
    obj=student.objects.all()
    return  render(request,'list.html',{'obj':obj})