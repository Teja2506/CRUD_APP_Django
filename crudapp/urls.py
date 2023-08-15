from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('std_mgmt_sys', views.sms, name='sms'),
    path('register', views.register, name='register'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutuser, name='logout'),
    path('addStudent', views.addStudent, name='addstudent'),
    path('delStudent/<int:id>', views.delStudent, name='delstudent'),
    path('updateStudent/<int:id>', views.updateStudent, name='updatestudent'),
    path('updatedStudent/<int:id>', views.updatedStudent, name='updatedstudent'),
]