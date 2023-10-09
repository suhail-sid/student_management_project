# Note-All the UI is used in the project is directly downloaded from the internet directly but the functionality is done.

# College Management System

A web-based College Management System implemented using Python and Django.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [User Roles](#user-roles)
  - [Functionality](#functionality)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The College Management System is a comprehensive web application designed to streamline administrative tasks in educational institutions. It offers a range of features to manage students, faculty, subjects, sessions, attendance, and results effectively.

## Features

- **User Authentication:** Secure user authentication system for different roles, including students, staff, and Heads of Department (HODs).

- **User Roles:**
  - **HOD (Head of Department):** Can add staff and students, manage subjects, and create new academic sessions.
  - **Teacher (Staff):** Mark attendance for students and assign grades to students for their respective subjects.
  - **Student:** Access their own attendance and results, providing a passive view of their academic information.

- **Dashboard:** Each user role has a personalized dashboard to access relevant information and perform tasks.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed.
- Django framework installed.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/suhail-sid/college-management-system.git



1. Navigate to the project directory:
cd college-management-system


2.Install project dependencies:
pip install -r requirements.txt


3.Run database migrations:
python manage.py migrate

4.Create a superuser (admin) account:
python manage.py createsuperuser

5.Start the development server:
python manage.py runserver

6.Access the application in your web browser at http://127.0.0.1:8000/.


USAGE
User Roles
1.HOD (Head of Department):
Login with HOD credentials.
Add staff and students to the system.
Manage subjects and create new academic session years with subjects.
Teacher (Staff):

2.Login with teacher credentials.
Mark attendance for students.
Assign grades to students for the subjects they teach.
Student:

3.Login with student credentials.
Access personal attendance and academic results.



Functionality
HOD (Head of Department):

Add Staff and Students:
On the HOD dashboard, use the "Add Staff" and "Add Students" functionality to add new staff and students to the system.
Manage Subjects:
Add and manage subjects that are taught at the institution.
Create New Academic Sessions:
Create new academic session years and associate subjects with them.
Teacher (Staff):

Mark Attendance:
On the teacher dashboard, mark attendance for students in the subjects they teach.
Assign Grades:
Assign grades or marks to students for the subjects they are responsible for.
Student:

View Attendance:
Log in as a student to access your own attendance records.
Access Academic Results:
View your academic results and grades.
Each user role has access to a personalized dashboard tailored to their responsibilities and tasks.

Contributing
Contributions are welcome! If you would like to contribute to this project, please follow these steps:


License
This project is licensed under the MIT License. See the LICENSE file for details.
