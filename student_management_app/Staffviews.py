from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from student_management_app.models import Staff, Staff_notification , Staff_leave, Staff_feedback , Subject ,  Session_year , Student , Attendance , Attendance_report , Student_result , Course


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
    return render(request, 'Staff/home.html',context)


# Notification
@login_required(login_url='/')
def notifications(request):
    staff = Staff.objects.filter(admin = request.user.id)
    for i in staff:
        # print(i.id)
        staff_id = i.id
        
        notification = Staff_notification.objects.filter(staff_id=staff_id)
        
        context = {
            'notification': notification,
        }
        return render(request, 'Staff/notifications.html',context)
    
@login_required(login_url='/')
def staff_mark_as_done(request,status):
    notification = Staff_notification.objects.get(id = status)
    notification.status = 1
    notification.save()
    
    return redirect('notifications')


# Leave Apply
@login_required(login_url='/')
def staff_leave_apply(request):
    staff = Staff.objects.filter(admin = request.user.id)
    # print(staff)
    for i in staff:
        # print(i.id)
        
        staff_id = i.id
        
        staff_leave_history = Staff_leave.objects.filter(staff_id=staff_id)
        
        context = {
            'staff_leave_history': staff_leave_history,
        }
    return render(request, 'Staff/apply_leave.html',context)


# Send Leave Request to HOD/Admin
@login_required(login_url='/')
def staff_apply_leave_save(request):
    if request.method == 'POST':
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')
        
        staff = Staff.objects.get(admin = request.user.id)
        
        
        leave = Staff_leave(
            staff_id = staff,
            date = leave_date,
            message = leave_message, 
        )
        
        leave.save()
        messages.success(request, 'Leave Application Send!')
        return redirect('staff_apply_leave')
    
    

# Feedback
@login_required(login_url='/')
def staff_send_feedback(request):
    staff_id = Staff.objects.get(admin = request.user.id)
    feedback_history = Staff_feedback.objects.filter(staff_id = staff_id)
    
    context = {
        'feedback_history': feedback_history,
    }
    return render(request, 'Staff/feedback.html' , context)

@login_required(login_url='/')
def staff_feedback_save(request):
    if request.method == 'POST':
        feedback = request.POST.get('feedback')
        
        staff = Staff.objects.get(admin=request.user.id)
        
        feed = Staff_feedback(
            staff_id = staff,
            feedback = feedback,
            feedback_reply = " ",
            
        )
        feed.save()
        
        messages.success(request, 'Feedback Sent!')
        return redirect('staff_send_feedback')
    
    
    
    
# Attendance
@login_required(login_url='/')
def staff_take_attendance(request):
    staff_id = Staff.objects.get(admin=request.user.id)
    
    subject = Subject.objects.filter(staff = staff_id)
    session_year = Session_year.objects.all()
    action = request.GET.get('action')
    
    
    get_subject = None
    get_session_year = None
    students = None
    
    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')
            
            get_subject = Subject.objects.get(id = subject_id)
            get_session_year = Session_year.objects.get(id = session_year_id)
            
            subject = Subject.objects.filter(id = subject_id)
            for i in subject :
                student_id = i.course.id
                students = Student.objects.filter(course_id=student_id)
    
    context = {
        'subject': subject,
        'session_year': session_year,
        'get_subject': get_subject,
        'get_session_year': get_session_year,
        'action': action,
        'students': students,
    }
    return render(request , 'staff/take_attendance.html', context)


@login_required(login_url='/')
def staff_save_attendance(request):
    
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        session_year_id = request.POST.get('session_year_id')
        attendance_date = request.POST.get('attendance_date')
        students_id = request.POST.getlist('students_id')
        
        
        get_subject = Subject.objects.get(id = subject_id)
        get_session_year = Session_year.objects.get(id = session_year_id)
        
        attendance = Attendance(
            subject_id = get_subject,
            attendance_date = attendance_date,
            session_year_id = get_session_year,
        )
        attendance.save()
        
        for i in students_id :
            stud_id = i
            int_stud = int(stud_id)
            
            p_student = Student.objects.get(id = int_stud)
            
            attendance_report = Attendance_report(
                student_id = p_student,
                attendance_id = attendance,
            )
            attendance_report.save()
    messages.success(request, "Attendance Marked!")
    return  redirect('staff_take_attendance')



# view Attendance
@login_required(login_url='/')
def staff_view_attendance(request):
    staff_id = Staff.objects.get(admin=request.user.id)
    subject = Subject.objects.filter(staff_id = staff_id)
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
    return render(request, 'Staff/view_attendance.html',context)



# Add Student_result
@login_required(login_url='/')
def staff_add_result(request):
    staff = Staff.objects.get(admin = request.user.id)
    
    subject = Subject.objects.filter(staff_id = staff)
    session_year = Session_year.objects.all()
    
    action = request.GET.get('action')
    
    
    get_subject = None
    get_session = None
    students = None
    
    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')
            
            # print(subject_id,session_year_id)
            get_subject = Subject.objects.get(id = subject_id)
            get_session = Session_year.objects.get(id = session_year_id)
            
            subject = Subject.objects.filter(id = subject_id)
            for i in subject:
               student_id = i.course.id 
               students = Student.objects.filter(course_id = student_id) 
            
    context = {
        'subject': subject,
        'session_year':session_year,
        'action':action,
        'get_subject':get_subject,
        'get_session':get_session,
        'students':students,
        
    }
    return render(request, 'Staff/add_result.html',context)


@login_required(login_url='/')
def staff_save_result(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        session_year_id = request.POST.get('session_year_id')
        student_id = request.POST.get('student_id')
        assignment_mark = request.POST.get('assignment_mark')
        exam_mark = request.POST.get('exam_mark')

        get_student = Student.objects.get(admin = student_id)
        get_subject = Subject.objects.get(id=subject_id)

        check_exist = Student_result.objects.filter(subject_id=get_subject, student_id=get_student).exists()
        if check_exist:
            result = Student_result.objects.get(subject_id=get_subject, student_id=get_student)
            result.assignment_mark = assignment_mark
            result.exam_mark = exam_mark
            result.save()
            messages.success(request, "Successfully Result Updated")
            return redirect('staff_add_result')
        else:
            result = Student_result(student_id=get_student, 
                                    subject_id=get_subject, 
                                    exam_mark=exam_mark,
                                    assignment_mark=assignment_mark
                                    )
            result.save()
            messages.success(request, "Successfully Added Result")
            return redirect('staff_add_result')