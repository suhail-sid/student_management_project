from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from student_management_app.models import CustomUser, Course, Session_year, Student, Staff, Subject, Staff_notification , Staff_leave,Staff_feedback, Student_notification , Student_feedback , Student_leave , Attendance , Attendance_report


@login_required(login_url='/')
def home(request):
    student_count = Student.objects.all().count()
    staff_count = Staff.objects.all().count()
    course_count = Course.objects.all().count()
    subject_count = Subject.objects.all().count()
    
    
    student_gender_male = Student.objects.filter(gender = 'Male').count()
    student_gender_female = Student.objects.filter(gender = 'Female').count()
    
    context = {
        'student_count': student_count,
        'staff_count': staff_count,
        'course_count': course_count,
        'subject_count': subject_count,
        'student_gender_male':student_gender_male,
        'student_gender_female':student_gender_female,
    }
    return render(request, 'Hod/home.html',context)

# Student Functions
@login_required(login_url='/')
def add_student(request):
    course = Course.objects.all()
    session_year = Session_year.objects.all()
    
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')
        
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,"Eail is already registered!")
            return redirect('add_student')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,"username is already registered!")
            return redirect('add_student')
        else:
            
            user = CustomUser.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                profile_pic = profile_pic,
                user_type=3,
            )
            user.set_password(password)
            user.save()
              
            course = Course.objects.get(id=course_id)
            session_year = Session_year.objects.get(id=session_year_id)
            
            
            student = Student(
                admin = user,
                address = address,
                course_id = course,
                session_year_id = session_year,
                gender = gender,
            )
            student.save()
            messages.success(request, user.first_name +" "+ user.last_name +" "+"Successfully registered!")
            return redirect('add_student')
          
    context = {
        'course' : course,
        'session_year' : session_year,
    }
    return render(request, 'Hod/add_student.html', context)


@login_required(login_url='/')
def view_student(request):
    student = Student.objects.all()
    
    context = {
        'student' : student,
    }
    return render(request, 'Hod/view_student.html',context)

def edit_student(request, id):
    student = Student.objects.filter(id = id)
    course = Course.objects.all()
    session_year = Session_year.objects.all()
    
    context = {
        'student': student,
        'course': course,
        'session_year': session_year,
    }
    return render(request, 'Hod/edit_student.html', context)

@login_required(login_url='/')
def update_student(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')
        
        # To update data in user model
        user = CustomUser.objects.get(id=student_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        if profile_pic:
            user.profile_pic = profile_pic
        if password:
            user.set_password(password)
        user.save()
        
        # To update data in student model
        student = Student.objects.get(admin=student_id)
        student.address = address
        student.gender = gender
        
        # To get id of course and save it in student model
        course = Course.objects.get(id=course_id)
        student.course_id = course
        
        # To get id of session year and save it in student model
        session_year = Session_year.objects.get(id=session_year_id)
        student.session_year_id = session_year
        student.save()
        
        messages.success(request, "Credentials are updated!")
        return redirect('view_student')
    
    return render(request, 'Hod/edit_student.html')

@login_required(login_url='/')
def delete_student(request , admin):
    student = CustomUser.objects.get(id = admin)
    student.delete()
    messages.warning(request, "Record deleted!")
    return redirect( 'view_student')





# COURSE Function
@login_required(login_url='/')
def add_course(request):
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        course = Course(
            name = course_name,
        )
        course.save()
        messages.success(request,"Course added!")
        return redirect( 'add_course')
    return render(request, 'Hod/add_course.html')


@login_required(login_url='/')
def view_course(request):
    course = Course.objects.all()
    
    context = {
        'course': course,
    }
    return render(request, 'Hod/view_course.html',context)

@login_required(login_url='/')
def edit_course(request, id):
    course = Course.objects.get(id = id)
    
    context = {
        'course': course,
    }
    return render(request, 'Hod/edit_course.html',context)

@login_required(login_url='/')
def update_course(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        name = request.POST.get('course_name')
        
        course = Course.objects.get(id = course_id )
        course.name = name
        course.save()
        messages.success(request, 'Course updated successfully!')
        return redirect('view_course')
    return render(request, 'Hod/edit_course.html')

@login_required(login_url='/')
def delete_course(request , id):
    course = Course.objects.get(id = id)
    course.delete()
    messages.warning(request, 'Course deleted!')
    return redirect('view_course')






# Staff Functions
@login_required(login_url='/')
def add_staff(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, "Email is already registered!")
            return redirect('add_staff')
        elif CustomUser.objects.filter(username=username).exists():
            messages.warning(request, "Username is already registered!")
            return redirect('add_staff')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                profile_pic=profile_pic,
                user_type=2,
            )
            user.set_password(password)
            user.save()

            staff = Staff(
                admin=user,
                address=address,
                gender=gender,
            )
            staff.save()
            messages.success(request, "Staff added successfully!")
            return redirect("add_staff")

    return render(request, 'Hod/add_staff.html')


@login_required(login_url='/')
def view_staff(request):
    staff = Staff.objects.all()
    
    context = {
        'staff': staff,
    }
    return render(request, 'Hod/view_staff.html',context)

def edit_staff(request,id):
    staff = Staff.objects.get(id = id)
    
    context = {
        'staff': staff,
    }
    return render(request, 'Hod/edit_staff.html',context)


@login_required(login_url='/')
def update_staff(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        
        
        user = CustomUser.objects.get(id= staff_id)
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        if profile_pic:
            user.profile_pic = profile_pic
        if password:
            user.set_password(password)
        user.save()
        
        staff = Staff.objects.get(admin= staff_id)
        staff.gender = gender
        staff.address = address
        staff.save()
        messages.success(request,"Staff details Updated!")
        return redirect('view_staff')
        
    return render(request, 'Hod/edit_staff.html')


@login_required(login_url='/')
def delete_staff(request , admin):
    staff = CustomUser.objects.get(id = admin)
    staff.delete()
    messages.warning(request,"Staff deleted!")
    return redirect('view_staff')








# Subject Functions

@login_required(login_url='/')
def add_subject(request):
    course = Course.objects.all()
    staff = Staff.objects.all()
    
    if (request.method =="POST"):
        subject_name = request.POST.get('subject_name')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')
        
        course = Course.objects.get(id = course_id)
        staff = Staff.objects.get(id = staff_id)
        subject = Subject(
            name = subject_name,
            course = course,
            staff = staff,
        )
        subject.save()
        messages.success(request,"Subject added successfully!")
        return redirect('view_subject')
    
    context = {
        'course': course,
        'staff': staff,
    }
    return render(request, 'Hod/add_subject.html',context)

@login_required(login_url='/')
def view_subject(request):
    subject = Subject.objects.all()
    
    context = {
        'subject': subject,
    }
    return render(request, 'Hod/view_subject.html',context)

@login_required(login_url='/')
def edit_subject(request,id):
    subject = Subject.objects.get(id=id)
    course = Course.objects.all()
    staff = Staff.objects.all()
    
    context = {
        'subject':subject,
        'course':course,
        'staff':staff,
        }
    return render(request, 'Hod/edit_subject.html',context)


@login_required(login_url='/')
def update_subject(request):
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        subject_name = request.POST.get('subject_name')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')
        
        course = Course.objects.get(id=course_id)
        staff = Staff.objects.get(id=staff_id)
        
        subject = Subject(
            id=subject_id,
            name = subject_name,
            course = course,
            staff = staff,
        )
        subject.save()
        messages.success(request,"Subject upated successfully!")
        return redirect('view_subject')
    
    
@login_required(login_url='/')
def delete_subject(request, id):
    subject = Subject.objects.filter(id=id)
    subject.delete()
    messages.warning(request,"Subject deleted successfully!")
    return redirect('view_subject')








# Session Functions
@login_required(login_url='/')
def add_session(request):
    if request.method == 'POST':
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')
        
        session = Session_year(
            session_start = session_year_start,
            session_end = session_year_end,
        )
        
        session.save()
        messages.success(request,"Session are added successfully!")
        return redirect('add_session')
    return render(request , 'Hod/add_session.html')


@login_required(login_url='/')
def view_session(request):
    session = Session_year.objects.all()
    
    context = {
        'session': session,
    }
    return render(request, 'Hod/view_session.html',context)

@login_required(login_url='/')
def edit_session(request,id):
    session = Session_year.objects.filter(id = id)
    
    context = {
        'session': session,
    }
    return render(request, 'Hod/edit_session.html', context)

@login_required(login_url='/')
def update_session(request):
    if request.method == 'POST':
        session_id = request.POST.get('session_id')
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')
        
        session = Session_year(
            id= session_id,
            session_start = session_year_start,
            session_end = session_year_end,
        )
        
        session.save()
        
        messages.success(request,'Session updated!')
        return redirect('view_session')
    
@login_required(login_url='/')
def delete_session(request, id):
    session = Session_year.objects.get(id=id)
    session.delete()
    messages.warning(request,'Session deleted!')
    return redirect('view_session')





# Notification functions

# For Staff
@login_required(login_url='/')
def staff_send_notifications(request):
    staff = Staff.objects.all()
    see_notification = Staff_notification.objects.all().order_by('-id')[0:5]
    
    context = {
        'staff': staff,
        'see_notification':see_notification, 
        }
    return render(request,'Hod/staff_send_notification.html',context)

@login_required(login_url='/')
def staff_save_notifications(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        message = request.POST.get('message')
        
        
        staff = Staff.objects.get(admin=staff_id)
        notification = Staff_notification(
            staff_id = staff,
            message = message,
        )
        notification.save()
        messages.success(request,"Notification Sent Successfully!")
    return redirect('staff_send_notification')




# Staff Leave 
@login_required(login_url='/')
def staff_leave_view(request):
    
    staff_leave = Staff_leave.objects.all()
    
    context = {
        'staff_leave': staff_leave,
    }
    return render(request, 'Hod/staff_leave.html', context)


# Approve Leave
@login_required(login_url='/') 
def staff_approve_leave(request , id):
    leave = Staff_leave.objects.get(id = id)
    leave.status = 1
    leave.save()
    return redirect('staff_leave_view')

# Disapprove Leave
@login_required(login_url='/')
def staff_disapprove_leave(request , id):
    leave = Staff_leave.objects.get(id = id)
    leave.status = 2
    leave.save()
    return redirect('staff_leave_view')



# Staff Feedback Reply
@login_required(login_url='/')
def staff_feedback_reply(request):
    feedback = Staff_feedback.objects.all()
    feedback_history = Staff_feedback.objects.all().order_by('-id')[0:5]
    
    context = {
        'feedback': feedback,
        'feedback_history': feedback_history,
               }
    messages.success(request,"Reply Sent to staff!")
    return render(request, 'Hod/staff_feedback.html',context)


@login_required(login_url='/')
def staff_feedback_reply_save(request):
    if request.method == 'POST':
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')
        
        
        feedback = Staff_feedback.objects.get(id = feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.status = 1
        feedback.save()
        
        
        return redirect('staff_feedback_reply')
    
    
    






# Student Functions 

# Notification
@login_required(login_url='/')
def student_send_notifications(request):
    student = Student.objects.all()
    notification = Student_notification.objects.all()
    
    context = {
        'student': student,
        'notification': notification,
    }
    return render(request, 'Hod/student_send_notification.html',context)


@login_required(login_url='/')
def student_save_notifications(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        student_id = request.POST.get('student_id')
        
        student = Student.objects.get(admin = student_id)
        
        
        stud_notification = Student_notification(
            student_id = student,
            message = message,
        )
        stud_notification.save()
        messages.success(request, 'Student notification send successfully!')
        
        return redirect('student_send_notification')
    
    
    
    
    
# feedback
@login_required(login_url='/')
def student_feedback_reply(request):
    feedback = Student_feedback.objects.all()
    feedback_history = Student_feedback.objects.all().order_by('-id')[0:5]
    
    context = {
        'feedback': feedback,
        'feedback_history':feedback_history
               }
    messages.success(request,"Reply Sent to student!")
    return render(request, 'Hod/student_feedback.html',context)


@login_required(login_url='/')
def student_feedback_reply_save(request):
    if request.method == 'POST':
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')
        
        
        feedback = Student_feedback.objects.get(id = feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.status = 1
        feedback.save()
        
        
        return redirect('student_feedback_reply')
    
    
# Student Leave 
@login_required(login_url='/')
def student_leave_view(request):
    
    student_leave = Student_leave.objects.all()
    
    context = {
        'student_leave': student_leave,
    }
    return render(request, 'Hod/student_leave.html', context)


# Approve Leave
@login_required(login_url='/') 
def student_approve_leave(request , id):
    leave = Student_leave.objects.get(id = id)
    leave.status = 1
    leave.save()
    return redirect('student_leave_view')

# Disapprove Leave
@login_required(login_url='/')
def student_disapprove_leave(request , id):
    leave = Student_leave.objects.get(id = id)
    leave.status = 2
    leave.save()
    return redirect('student_leave_view')



# View Atendance
@login_required(login_url='/')
def hod_view_attendance(request):
    
    subject = Subject.objects.all()
    session_year = Session_year.objects.all()
    
    action = request.GET.get('action')
    
    get_subject = None
    get_session_year = None
    attendance_date = None
    attendace_report = None
    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')
            attendance_date = request.POST.get('attendance_date')
            
            
            get_subject = Subject.objects.get(id = subject_id)
            get_session_year = Session_year.objects.get(id = session_year_id)
            
            attendance = Attendance.objects.filter(subject_id = get_subject, attendance_date = attendance_date)
            for i in attendance:
                attendance_id = i.id 
                attendace_report = Attendance_report.objects.filter(attendance_id = attendance_id ) 
    
    context = {
        'subject': subject,
        'session_year':session_year,
        'action':action,
        'get_subject':get_subject,
        'get_session_year':get_session_year,
        'attendance_date':attendance_date,
        'attendace_report':attendace_report,
    } 
    return render(request, 'Hod/view_attendance.html',context)

