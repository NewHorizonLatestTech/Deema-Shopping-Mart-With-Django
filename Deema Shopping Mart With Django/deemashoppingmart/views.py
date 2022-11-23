from django.shortcuts import render
from django.http import HttpResponse
# from shoppingmart.models import Student_Data
# from shoppingmart.models import adeemaform_1
from . import views

def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')

def adeemaform(request):
    # m=""
    # if request.method == 'POST':
    #     name=request.POST.get('name')
    #     email=request.POST.get('email')
    #     password=request.POST.get('password')
    #     age=request.POST.get('age')
    #     father_name=request.POST.get('father_name')
    #     datetime=request.POST.get('datetime')   
    #     data=adeemaform_1(name=name,age=age,email=email,password=password,father_name=father_name,datetime=datetime)
    #     data.save()
    #     m="Your Data Has Been Sent Bro Let's You Can Go And Check Our Website"
    return render(request,'adeemaform.html')
    # ,{'m':m}
def form(request):
    # d=""
    # if request.method == 'POST':
    #     User_name=request.POST.get('User_name')
    #     Father_name=request.POST.get('Father_name')
    #     Email=request.POST.get('Email')
    #     Password=request.POST.get('Password')
    #     About_user=request.POST.get('About_user')
    #     Dath_Of_Birth=request.POST.get('Dath_Of_Birth')   
    #     prof_pic=request.POST.get('prof_pic')            
    #     data=Student_Data(User_name=User_name,Father_name=Father_name,Email=Email,Password=Password,About_user=About_user,Dath_Of_Birth=Dath_Of_Birth,prof_pic=prof_pic)
    #     data.save()
        # print(data)
    #     d="Your Data Has Been Sent Bro Let's You Can Go And Check Our Website"
    return render(request,'form.html')
    

# ,{'d':d}
  

