from django.contrib import admin
from django.urls import path, include
from student_management_app import views
from student_management_app import Hodviews , Studentviews , Staffviews 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('base/',views.Base , name="base"),
    path('',views.login_page , name="login_page"),
    path('doLogin',views.dologin , name="dologin"), 
    path('doLogout',views.dologout , name="dologout"),
    
    # Profile Update
    path('profile',views.profile , name="profile"),
    path('profile/update',views.profile_update , name="profile_update"),
    
    
    
    
    
    # HOD URLS
    path('Hod/home', Hodviews.home , name ='hod_home'),
    # HOD student
    path('Hod/student/add', Hodviews.add_student , name='add_student'),
    path('Hod/student/view',Hodviews.view_student , name='view_student'),
    path('Hod/student/edit/<str:id>', Hodviews.edit_student , name='edit_student'),
    path('Hod/student/update',Hodviews.update_student , name='update_student'),
    path('Hod/student/delete/<str:admin>', Hodviews.delete_student , name='delete_student'),
    # HOD courses
    path('Hod/course/add', Hodviews.add_course , name='add_course'),
    path('Hod/course/view',Hodviews.view_course , name='view_course'),
    path('Hod/course/edit/<str:id>',Hodviews.edit_course , name='edit_course'),
    path('Hod/course/update',Hodviews.update_course , name='update_course'),
    path('Hod/course/delete/<str:id>',Hodviews.delete_course ,name = 'delete_course'),
    # HOD staff
    path('Hod/staff/add',Hodviews.add_staff, name='add_staff'),
    path('Hod/staff/view',Hodviews.view_staff , name='view_staff'),
    path('Hod/staff/edit/<str:id>',Hodviews.edit_staff, name='edit_staff'),
    path('Hod/staff/update/',Hodviews.update_staff, name='update_staff'),
    path('Hod/staff/delete/<str:admin>',Hodviews.delete_staff, name='delete_staff'),
    # HOD subjects
    path('Hod/subject/add',Hodviews.add_subject, name='add_subject'),
    path('Hod/subject/view',Hodviews.view_subject, name='view_subject'),
    path('Hod/subject/edit/<str:id>',Hodviews.edit_subject, name='edit_subject'),
    path('Hod/subject/update/',Hodviews.update_subject, name='update_subject'),
    path('Hod/subject/delete/<str:id>',Hodviews.delete_subject, name='delete_subject'),
    # HOD sessions
    path('Hod/session/add',Hodviews.add_session, name='add_session'),
    path('Hod/session/view',Hodviews.view_session, name='view_session'),
    path('Hod/session/edit/<str:id>',Hodviews.edit_session, name='edit_session'),
    path('Hod/session/update/',Hodviews.update_session, name='update_session'),
    path('Hod/session/delete/<str:id>',Hodviews.delete_session, name='delete_session'),
    # HOD Leave approval
    path('Hod/staff/leave_view',Hodviews.staff_leave_view, name='staff_leave_view'),    
    path('Hod/staff_approve_leave/<str:id>',Hodviews.staff_approve_leave, name='staff_approve_leave'),
    path('Hod/staff_disapprove_leave/<str:id>',Hodviews.staff_disapprove_leave, name='staff_disapprove_leave'),
    path('Hod/student/leave_view', Hodviews.student_leave_view, name='student_leave_view'),
    path('Hod/student_approve_leave/<str:id>', Hodviews.student_approve_leave, name='student_approve_leave'),
    path('Hod/student_disapprove_leave/<str:id>', Hodviews.student_disapprove_leave, name='student_disapprove_leave'),
    # Notifications
    path('Hod/Staff/send_notifications',Hodviews.staff_send_notifications, name='staff_send_notification'),
    path('Hod/Staff/save_notifications',Hodviews.staff_save_notifications, name='staff_save_notification'),
    path('Hod/Student/send_notifications',Hodviews.student_send_notifications, name='student_send_notification'),
    path('Hod/Student/save_notifications',Hodviews.student_save_notifications, name='student_save_notification'),
    # Feedback Reply
    path('Hod/staff/feedback_reply',Hodviews.staff_feedback_reply,name='staff_feedback_reply'),
    path('Hod/staff/feedback/save',Hodviews.staff_feedback_reply_save, name='staff_feedback_reply_save'),
    path('Hod/student/feedback_reply',Hodviews.student_feedback_reply,name='student_feedback_reply'),
    path('Hod/student/feedback/save',Hodviews.student_feedback_reply_save, name='student_feedback_reply_save'),
    # View Attendance
    path('Hod/view/attendance',Hodviews.hod_view_attendance, name='view_attendance'),
    
    
    
    
    
    
    
    
    
    
    
    
    # Staff Urls
    path('Staff/home',Staffviews.home, name='staff_home'),
    
    
    # Notifications
    path('Staff/notifications',Staffviews.notifications, name='notifications'),
    path('Staff/mark_as_done/<str:status>',Staffviews.staff_mark_as_done, name='staff_mark_as_done'),
    
    # Leave Apply
    path('Staff/apply_leave',Staffviews.staff_leave_apply, name='staff_apply_leave'),
    path('Staff/apply_leave_save',Staffviews.staff_apply_leave_save, name='staff_apply_leave_save'),
    
    # Send Feedback
    path('Staff/send_feedback',Staffviews.staff_send_feedback, name='staff_send_feedback'),
    path('Staff/feedback/save',Staffviews.staff_feedback_save, name='staff_feedback_save'),
    
    # Attendance
    path('Staff/take_attendance',Staffviews.staff_take_attendance,name='staff_take_attendance'),
    path('Staff/save_attendance',Staffviews.staff_save_attendance,name='staff_save_attendance'),
    path('Staff/view_attendance',Staffviews.staff_view_attendance,name='staff_view_attendance'),
    # Add Result
    
    path('Staff/add/result',Staffviews.staff_add_result,name='staff_add_result'),
    path('Staff/save/result',Staffviews.staff_save_result,name='staff_save_result'),
    
    
    
    
    
    
    
    # Students URL
    path('Student/home',Studentviews.home, name='student_home'),
    # Notification 
    path('Student/notification',Studentviews.student_notification, name='student_notification'),
    path('Student/mark_as_done/<str:status>',Studentviews.staff_mark_as_done, name='student_mark_as_done'),
    # Send Feedback
    path('Student/send_feedback',Studentviews.student_send_feedback, name='student_send_feedback'),
    path('Student/feedback/save',Studentviews.student_feedback_save, name='student_feedback_save'),
    # Leave Apply
    path('Student/apply_leave',Studentviews.student_leave_apply, name='student_apply_leave'),
    path('Student/apply_leave_save',Studentviews.student_apply_leave_save, name='student_apply_leave_save'),
    # Attendance
    path('Student/view_attendance',Studentviews.student_view_attendance,name='student_view_attendance'),
    # View Result
    path('Student/view_result',Studentviews.student_view_result,name='student_view_result'),
    
    
     
] + static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)