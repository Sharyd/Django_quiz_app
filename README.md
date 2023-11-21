# Django Quiz App

This Django Quiz App is a web application that allows users to take quizzes on various topics.

## Features

  ## Admin UI
  - **Quiz Management**: Create and manage quizzes with ease through the admin interface of Django.
  - **Question & Choice Management**: Add questions and multiple-choice answers to each quiz and one correct answer.

  ## Web Quiz App
  - **Score**: The app tracks scores and shows a completion page with correct answers.
  - **Step form**: Next and Back button with build in step form
  - **Dark/Light mode**: Dark/Light mode with pure css and little of js
  - **Responsive Design**: The app is fully responsive and works on various devices and screen sizes.

## Technology Stack

- **Backend**: Django
- **Frontend**: HTML, CSS
- **Database**: SQLite (default), can be configured for PostgreSQL or MySQL
- **Hosting**: AWS Elastic Beanstalk
- **Static & Media Files**: AWS S3 (if applicable)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8+
- pip
- virtualenv (optional)

### Installation

Clone the repository

bash
Copy code
git clone https://github.com/your-username/your-quiz-app.git
cd 
Set up a virtual environment (recommended)

```
python -m venv venv
source venv/bin/activate  # For Windows use `venv\Scripts\activate`
```
**Install dependencies**

```pip install -r requirements.txt```

**Apply migrations to create the database schema.**

```
python manage.py migrate
```
**Create an admin user**

```
python manage.py createsuperuser
```
**Collect static files**

```
python manage.py collectstatic
```
**Run the development server**

```
python manage.py runserver
```

