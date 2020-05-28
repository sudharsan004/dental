from django.shortcuts import render
from django.core.mail import send_mail
from .models import opentime
def responsemail(tomail,name):
    send_mail(
            'From Dentrist website  ',
            'Hello, '+name+' Thanks for using oru website. \nOur Doctor will respond soon',
            '8921test@gmail.com',
            [tomail],
            fail_silently=False,)
def response(request):    
    if request.method=='POST':
        name=request.POST['name']
        mail=request.POST['mail']
        date=request.POST['date']
        time=request.POST['time']
        send_mail(
            'From Dentrist website  ',
            'Hello, '+name+' Thanks for using oru website. \nYour Appoinment has been confirmed.  You can vist the hospital on the specifed time.',
            '8921test@gmail.com',
            [mail],
            fail_silently=False,)
        send_mail(
            'Appoinment from '+name,
            name+'Has made an appoinment on :'+date+' in :'+time+'\n\n His message was: '+'\n\nHis',
            mail,
            ['sudharsansriram8921@gmail.com'],
            fail_silently=True,)
        print('hi')
        return render(request,'response.html',{'name':name})
    else:
        return render(request,'response.html')
        
def index(request):    
    availablity = opentime.objects.all()
    context = { 'availablity': availablity,}
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):   
    if request.method=='POST':
        name=request.POST['name']
        mail=request.POST['mail']
        subject=request.POST['subject']
        message=request.POST['message']
        responsemail(mail,name)
        send_mail(
            'message from '+name+' regarding '+subject,
            message+'\n\n his mail: '+mail,
            mail,
            ['sudharsansriram8921@gmail.com'],
            fail_silently=False,)
        return render(request,'contact.html',{'name':name,'mail':mail})
    else:
        return render(request,'contact.html')

def doctors(request):
    return render(request,'doctors.html')

def services(request):
    return render(request,'services.html')

def login(request):
    return render(request,'login.html')




