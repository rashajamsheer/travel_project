from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def mywork(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpass = request.POST['conformation password']
        if password == cpass:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exist")
                return redirect('mywork')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exist")
                return redirect('mywork')
            else:
                 user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email,
                                        password=password)
                 user.save();
        else:
            messages.info(request, 'password not matched')
            return redirect('mywork')
        return redirect('/')

    return render(request,'mywork.html')