from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from student_management_app.models import CustomUser, Staff, Course, Subject, Student , Student_notification ,Student_feedback ,Student_leave , Attendance , Attendance_report , Student_result

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
    return render(request, 'Student/home.html',context)

@login_required(login_url='/')
def student_notification(request):
    student = Student.objects.filter(admin = request.user.id)
    for i in student:
        # print(i.id)
        student_id = i.id
        
        notification = Student_notification.objects.filter(student_id=student_id)
        
        context = {
            'notification': notification,
        }
    return render(request, 'Student/student_notification.html',context)


@login_required(login_url='/')
def staff_mark_as_done(request,status):
    notification = Student_notification.objects.get(id = status)
    notification.status = 1
    notification.save()
    
    return redirect('student_notification')




# Feedback
@login_required(login_url='/')
def student_send_feedback(request):
    student_id = Student.objects.get(admin = request.user.id)
    feedback_history = Student_feedback.objects.filter(student_id = student_id)
    
    context = {
        'feedback_history': feedback_history,
    }
    return render(request, 'Student/feedback.html' , context)



@login_required(login_url='/')
def student_feedback_save(request):
    if request.method == 'POST':
        feedback = request.POST.get('feedback')
        
        student = Student.objects.get(admin=request.user.id)
        
        feed = Student_feedback(
            student_id = student,
            feedback = feedback,
            feedback_reply = " ",
            
        )
        feed.save()
        
        messages.success(request, 'Feedback Sent!')
        return redirect('student_send_feedback')
    
    
    
    
    
# Leave Apply
@login_required(login_url='/')
def student_leave_apply(request):
    student = Student.objects.filter(admin = request.user.id)
    # print(staff)
    for i in student:
        # print(i.id)
        
        student_id = i.id
        
        student_leave_history = Student_leave.objects.filter(student_id=student_id)
        
        context = {
            'student_leave_history': student_leave_history,
        }
    return render(request, 'Student/apply_leave.html',context)



# Send Leave Request to HOD/Admin
@login_required(login_url='/')
def student_apply_leave_save(request):
    if request.method == 'POST':
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')
        
        student = Student.objects.get(admin = request.user.id)
        
        
        leave = Student_leave(
            student_id = student,
            date = leave_date,
            message = leave_message, 
        )
        
        leave.save()
        messages.success(request, 'Leave Application Send!')
        return redirect('student_apply_leave')
    
    
    
    
# View Attendance 

def student_view_attendance(request):
    student = Student.objects.get(admin = request.user.id)
    subject = Subject.objects.filter(course = student.course_id)
    action = request.GET.get('action')
    
    get_subject = None
    attendance_report = None
    
    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            get_subject = Subject.objects.get(id = subject_id)
            attendance_report = Attendance_report.objects.filter(student_id = student , attendance_id__subject_id = subject_id)
                
    context = {
        'subject': subject,
        'action':action,
        'get_subject':get_subject,
        'attendance_report':attendance_report,
    }
    return render(request, 'Student/view_attendance.html', context)


# View Result
def student_view_result(request):
    mark = None
    student = Student.objects.get(admin = request.user.id)
    
    result = Student_result.objects.filter(student_id = student)
    
    for i in result:
        assignment_mark = i.assignment_mark
        exam_mark = i.exam_mark
        
        mark = assignment_mark + exam_mark
        
    context = {
        'result': result,
        'mark':mark,
    }
    return render(request, 'Student/view_result.html',context)