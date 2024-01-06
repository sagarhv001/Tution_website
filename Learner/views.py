from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from random import randint
from django.conf import settings
from Learner.models import Learner
from Tutor.models import *

# Create your views here.
def index(request):
    if 'email' in request.session:
        user_obj = Learner.objects.get(email = request.session['email'])
        return render(request, 'index.html', {'user_data': user_obj})
    
    else:
        return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def courses(request):
    if request.method == 'GET':
        all_courses  = Course.objects.all()    
        return render(request,'courses.html', {'course': all_courses})
    else:
        selected_course = Course.objects.get(id = request.POST['course_id'])
        return render(request,'course_view.html', {'course': selected_course})  
def about(request):
    return render(request,'about.html')

def login(request):
     if request.method == 'GET':
        return render(request, 'login.html')
     else:
        session_user = Learner.objects.get(email = request.POST['email'])
        
        if request.POST['password'] == session_user.password:
            
            request.session['email'] = session_user.email
            return redirect('index')

        else:
            return render(request, 'login.html', {'msg': "Invalid Password!!"})
       
           
            


def signup(request):
     global c_otp
     global user_data
     if request.method == 'GET':
        return render(request, 'signup.html')
     else:
       
        form_email = request.POST['email']
        try:
            
            user_obj = Learner.objects.get(email = form_email)
            return render(request, 'signup.html', {'msg': 'This email is already in Use.'})

        except:
          
           
           
            if request.POST['password'] == request.POST['c_password']:
                
                c_otp = randint(100_000, 999_999)
                
                user_data = {
                    'first_name': request.POST['first_name'],
                    'last_name': request.POST['last_name'],
                    'email': request.POST['email'],
                    'password':request.POST['password'],
                    'mobile': request.POST['mobile'],
                }

                subject = 'Starforge Nexus Registration'
                message = f'Hello!! your OTP is {c_otp}'
                sender = settings.EMAIL_HOST_USER
                rec = [request.POST['email']]
                send_mail(subject, message, sender, rec)
                return render(request, 'otp.html')
            else:
                return render(request, 'signup.html', {'msg': 'BOTH passwords do not match !'})


def otp(request):
     

     if str(c_otp) == request.POST['otp']:
        
        Learner.objects.create(
            first_name = user_data['first_name'],
            last_name = user_data['last_name'],
            email = user_data['email'],
            password = user_data['password'],
            mobile = user_data['mobile']
        )
        
        return render(request, 'index.html', {'msg': "Signup Successfull"})

     else:
        return render(request, 'otp.html', {'msg': "entered OTP is INVALID"})


    
     

def logout(request):
    del request.session['email']
    return redirect('index')

def course_view(request):
    selected_course = Course.objects.get(id = request.POST['course_id'])
    context ={selected_course}
    return render(request, 'course_view.html',context)