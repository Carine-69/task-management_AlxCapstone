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

Models

Task Model:

class Task(models.Model):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

    PRIORITY_CHOICES = [
        (LOW, 'low'),
        (MEDIUM, 'medium'),
        (HIGH, 'high'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField()
    priority_level = models.PositiveIntegerField(choices=PRIORITY_CHOICES, default=LOW)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title

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

License

This project is licensed under the MIT License - see the LICENSE file for details.

Contact

For any inquiries or feedback, feel free to reach out to:

Name: Carine Umugabekazi

Email: umugabecarinegmail.com

Thank you for exploring the Task Management App! Your feedback and suggestions are always welcome.

