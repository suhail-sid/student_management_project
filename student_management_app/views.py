from django.shortcuts import render,redirect,HttpResponse
from student_management_app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from student_management_app.models import CustomUser 


# Create your views here.
@login_required(login_url='/')
def Base(request):
    return render(request , 'base.html')


def login_page(request):
    return render(request , 'login.html')


def dologin(request):
    if request.method == 'POST':
        
        username = request.POST.get('email')
        password = request.POST.get('password')
        # print(username,password)
        user = EmailBackEnd.authenticate(request,username=request.POST.get('email'),password=request.POST.get('password'))
        # print(user)
        
        if user is not None:
            login(request, user)
            
            
            user_type = user.user_type
            # print(user_type)
            
            
            if user_type == '1':
                return redirect('hod_home')
            elif user_type == '2':
                return redirect("staff_home")
            elif user_type == '3':
                return redirect("student_home")
            else:
                messages.error(request,"Invalid user or password !")
                return redirect('login_page')  
        else:
            messages.error(request,"Invalid user or password !")
            return redirect('login_page')
        
        
      
def dologout(request):
    logout(request)
    return redirect('login_page')




def profile(request):
    user = CustomUser.objects.get(id = request.user.id)
    # print(user)
    context ={
        "user": user,
    }
    return render(request, 'profile.html', context)



def profile_update(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        # email = request.POST.get('email')
        # username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            customuser = CustomUser.objects.get(id = id)
            
            
            if profile_pic!= None and profile_pic != " ":
                customuser.profile_pic = profile_pic
            customuser.first_name = first_name
            customuser.last_name = last_name
            if password != None and password != " ":
                customuser.set_password(password)
            customuser.save()
            messages.success(request,"Profile Updated!")
            return redirect("profile")
        except:
            messages.error(request,"Profile Update Failed!")
    return render(request, 'profile.html')