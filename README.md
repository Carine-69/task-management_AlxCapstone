Task Management App

Overview

The Task Management App is a platform designed to help users manage their tasks efficiently. Inspired by my personal challenges with task management, this project aims to provide a simple yet effective tool for tracking, organizing, and prioritizing tasks. The app leverages Django and the Django REST Framework for backend development, providing a robust and scalable solution.

Features

User Authentication: Secure login and registration system using Django's built-in authentication.

Task Management:

Add, edit, and delete tasks.

Assign due dates and priorities to tasks.

Track task progress using status updates (Pending, In Progress, Completed).

Priority Levels:

Low, Medium, and High priority levels.

Responsive Design: Ensures usability on various devices.

Motivation

I often find myself struggling with time management, procrastination, and missing deadlines. This project was developed to address these challenges personally and to create a tool that could potentially help others facing similar issues. My goal is to continuously improve the app, making it more user-friendly and feature-rich.

Technologies Used

Backend:

Django

Django REST Framework

Database:

PostSQLite (default for development)

Tools:

Python 3.11.9

Git/GitHub for version control

Ubuntu Terminal

Installation and Setup

Clone the repository:

git clone https://github.com/Carine-69/task-management_AlxCapstone.git

Navigate to the project directory:

cd TaskManager

Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Apply migrations:

python manage.py migrate

Run the development server:

python manage.py runserver

Access the app at http://127.0.0.1:8000/ in your browser.

1   register:

Method: POST

URL = http://127.0.0.1:8000/auth/register/
 
Body, Raw, Json =

{ "username": "Annick", "email": "newstudent@example.com", "password": "password123456" }

Send  (id =3)


2  login:

Method: POST

URL=  http://127.0.0.1:8000/auth/login/

Body, Raw, Json =
{ "username": "Umutoni", "password": "password456" }
 
Access and refresh tokens will be generated you want to make sure that you save them


3. Create task:

Method: POST

URL= http://127.0.0.1:8000/tasks/

 Go to authorization, choose Bearer token  INSERT ACCESS TOKEN

Body, Raw, Json=

{
  "title": "Postman Guide Task",
  "Description": "Write a guide to help users understand how to use Postman with Django API.",
  "user": 3,
  "task_name": "Write Postman Guide",
  "due_date": "2025-01-20"}
}

Send

Edit Body, Raw, Json=
{
  "title": "Driving test",
  "Description": "Driving test to get driver’s licence.",
  "user": 3,
  "task_name": "Driving licence test",
  "due_date": "2025-03-20"}
}

4 Read:
Method: GET
URL= http://127.0.0.1:8000/tasks/

Send 

5 Update a task:

Method: PUT

URL= http://127.0.0.1:8000/tasks/1/

1 is the ID or number of the task

Meaning it is our first task= 

{
  "Title":”alx capstone project",
  "Description": "Test crud operations of alx capstone with postman.",
  "user": 3,
  "task_name": "updated to Task management ",
  "due_date": "2025-01-12"}
}


Send



6 delete a task:

Method: DELETE

URL = http://127.0.0.1:8000/tasks/2/


I choose to delete task 2
Send 

Quick example on how to perfom CRUD operations in postman:

1   register:

Method: POST

URL = http://127.0.0.1:8000/auth/register/
 
Body, Raw, Json =

{ "username": "Annick", "email": "newstudent@example.com", "password": "password123456" }

Send  (id =3)


2  login:

Method: POST

URL=  http://127.0.0.1:8000/auth/login/

Body, Raw, Json =
{ "username": "Umutoni", "password": "password456" }
 
Access and refresh tokens will be generated you want to make sure that you save them


3. Create task:

Method: POST

URL= http://127.0.0.1:8000/tasks/

 Go to authorization, choose Bearer token  INSERT ACCESS TOKEN

Body, Raw, Json=

{
  "title": "Postman Guide Task",
  "Description": "Write a guide to help users understand how to use Postman with Django API.",
  "user": 3,
  "task_name": "Write Postman Guide",
  "due_date": "2025-01-20"}
}

Send

Edit Body, Raw, Json=
{
  "title": "Driving test",
  "Description": "Driving test to get driver’s licence.",
  "user": 3,
  "task_name": "Driving licence test",
  "due_date": "2025-03-20"}
}

4 Read:
Method: GET
URL= http://127.0.0.1:8000/tasks/

Send 

5 Update a task:

Method: PUT

URL= http://127.0.0.1:8000/tasks/1/

1 is the ID or number of the task

Meaning it is our first task= 

{
  "Title":”alx capstone project",
  "Description": "Test crud operations of alx capstone with postman.",
  "user": 3,
  "task_name": "updated to Task management ",
  "due_date": "2025-01-12"}
}


Send



6 delete a task:

Method: DELETE

URL = http://127.0.0.1:8000/tasks/2/


I choose to delete task 2
Send 


Future Improvements

Deployment: Host the app using platforms like Heroku or AWS.

Notifications: Add email or push notifications to remind users about upcoming deadlines.

Enhanced UI/UX: Improve the design for better usability and aesthetics.

Collaboration: Allow task sharing and collaboration among multiple users.

Analytics: Provide insights on task completion trends and productivity metrics.

Challenges Faced

Learning Django REST Framework for the first time.

Overcoming procrastination and time management hurdles.

Balancing learning and implementation to complete the project effectively.

Lessons Learned

Breaking tasks into smaller, manageable pieces helps in completing the project more efficiently.

Researching and applying concepts immediately is an effective way to learn and grow.

Consistent effort and perseverance lead to tangible results.


Contact

For any inquiries or feedback, feel free to reach out to:

Name: Carine Umugabekazi

Email: umugabecarinegmail.com

Thank you for exploring the Task Management App! Your feedback and suggestions are always welcome.

