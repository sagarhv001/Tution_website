from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from random import randint
from django.conf import settings
from Tutor.models import *
from Learner.models import *
from django.forms import ModelForm

technology = Technology.objects.all()

def tutor_index(request):
    if 'email' in request.session:
        tutor_obj = Tutor.objects.get(email = request.session['email'])
        return render(request, 'tutor_index.html', {'tutor_data': tutor_obj, 'technology': technology})

    else:
        return render(request,'tutor_index.html', {'technology': technology})

# Create your views here.
def tutor_signup(request):

    global tutor_c_otp
    tutor_c_otp = randint(100_000, 999_999)
    global tutor_data
    
    if request.method == 'GET':
        return render(request, 'tutor_signup.html', {'technology': technology})
    else:

       
       
         form_email = request.POST['email']
         try:
            
            tutor_obj = Tutor.objects.get(email = form_email)
            return render(request, 'tutor_signup.html', {'msg': 'This email is already in Use.','technology': technology})

         except:
           
           
            if request.POST['password'] == request.POST['c_password']:
                
                
                
                tutor_data = {
                    'first_name': request.POST['first_name'],
                    'last_name': request.POST['last_name'],
                    'email': request.POST['email'],
                    'designation': request.POST['designation'],
                    'experience': request.POST['experience'],
                    'password':request.POST['password'],
                    'mobile': request.POST['mobile'],
                }

                subject = 'Starforge Nexus Tutor Registration'
                message = f'Hello!! your OTP is {tutor_c_otp}'
                sender = settings.EMAIL_HOST_USER
                rec = [request.POST['email']]
                send_mail(subject, message, sender, rec)
                return render(request, 'tutor_otp.html')
            else:
                return render(request, 'tutor_signup.html', {'msg': 'BOTH passwords do not match !'})




def tutor_otp(request):
    

        if str(tutor_c_otp) == request.POST['t_otp']:
            
            Tutor.objects.create(
                first_name = tutor_data['first_name'],
                last_name = tutor_data['last_name'],
                email = tutor_data['email'],
                password = tutor_data['password'],
                designation = tutor_data['designation'],
                experience = tutor_data['experience'],
                mobile = tutor_data['mobile'],
            )
            
            return render(request, 'tutor_index.html', {'msg': "Signup Successfull"})

        else:
            return render(request, 'tutor_otp.html', {'msg': "entered OTP is INVALID"})


def tutor_login(request):
    if request.method == 'GET':
        return render(request, 'tutor_login.html')
    else:
        session_tutor = Tutor.objects.get(email = request.POST['email'])
        
        if request.POST['password'] == session_tutor.password:
            
            request.session['email'] = session_tutor.email
            return redirect('tutor_index')

        else:
            return render(request, 'tutor_login.html', {'msg': "Invalid Password!!"})
        
def tutor_logout(request):
    del request.session['email']
    return redirect('index')


def tutor_add_lecture(request):
    if request.method == 'GET':
        return render(request, 'tutor_add_lecture.html')
    else:
        course_data = {
            'course_name': request.POST['course_name'],
            'course_description': request.POST['course_description'],
            'course_duration': request.POST['course_duration'],
            'course_file': request.FILES['courses'],
        }
        session_tutor = Tutor.objects.get(email = request.session['email'])


        course_obj = Course.objects.create(
            course_name = course_data['course_name'],
            course_description = course_data['course_description'],
            Tutor = session_tutor,
            course_duration = course_data['course_duration'],
            course_file = course_data['course_file'],
        
        )
        return render(request, 'tutor_index.html', {'msg': "Course Added Successfully"})
