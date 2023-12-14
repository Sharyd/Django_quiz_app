# Django Quiz App

This Django Quiz App is a web application that allows users to take quizzes on various topics.

## Production User for Admin UI
  - url: http://djangoquizapp-env-10.eba-zuszb39k.eu-north-1.elasticbeanstalk.com/admin/
  - username: TestQuiz
  - password: test123456*

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

## Installation

To set up the Django Quiz App for development, follow these steps:

1. **Clone the repository**

    Open a terminal and run:

    ```bash
    git clone https://github.com/Sharyd/Django_quiz_app.git
    cd Django_quiz_app
    ```

2. **Set up a virtual environment (recommended)**

    This isolates your project dependencies from other Python projects.

    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows use `venv\Scripts\activate`
    ```

3. **Install Django and other dependencies**

    Ensure you have all the required packages including Django itself installed.

    ```bash
    pip install -r requirements.txt
    ```

    If `requirements.txt` does not specify Django or if you need to install it separately:

    ```bash
    pip install django
    ```

4. **Apply migrations**

    Create the database schema based on the Django models defined.

    ```bash
    python manage.py migrate
    ```

5. **Create an admin user**

    Set up a superuser account for accessing the Django admin interface.

    ```bash
    python manage.py createsuperuser
    ```

6. **Collect static files**

    Gather all static assets into the directory specified by `STATIC_ROOT` in settings.

    ```bash
    python manage.py collectstatic
    ```

7. **Run the development server**

    Start the application on your local machine.

    ```bash
    python manage.py runserver
    ```


Remember to replace the `SECRET_KEY` in the `settings.py` file with a new generated one for production environments. You can generate a new secret key using the following command in a Python shell:
python
```
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

