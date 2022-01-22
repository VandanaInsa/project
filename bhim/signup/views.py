from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
import pyautogui as pu
def signup(request):
       if request.method=='POST':
          username=request.POST['username']
          firstname = request.POST['first_name']
          lastname = request.POST['last_name']
          email = request.POST['email_id']
          password = request.POST['password']

          if User.objects.filter(username=username).exist():
              pu.alert("username already exist")
              return render(request,'signup.html')
          else:
              x= User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
              x.save()
              pu.confirm("user created")
              return redirect('/')
       else:
        return render(request,'b.html')
# Create your views here.
