# Academic App Documentation

The Academic app is a key component of the School Management System. It handles the management of academic-related entities such as departments, classes, sections, sessions, class registrations, and guide teachers.

## Functionality

The Academic app offers the following features:

1. Department Management: Allows the creation, modification, and deletion of academic departments within the school.
2. Class Management: Provides functionality to create and manage different classes offered in the school.
3. Section Management: Allows the creation and management of sections within each class.
4. Session Management: Provides the ability to manage academic sessions or academic years.
5. Class Registration: Allows the registration of students for specific classes, sections, and sessions.
6. Guide Teacher Management: Offers functionality to assign guide teachers to specific classes.

## Setup and Configuration

Follow these instructions to set up and configure the Academic app:

### Prerequisites

- Python (version 3.6 or above)
- Django framework (version 3.2 or above)

### Installation

1. Clone the repository from GitHub:

```bash
git clone <repository_url>
```

2. Navigate to the project directory:

```bash
cd school_management_system
```

3. Create and activate a virtual environment (optional but recommended):

```bash
python3 -m venv venv
source venv/bin/activate
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Configuration

1. Update the project's `settings.py` file to include the Academic app in the `INSTALLED_APPS` setting:

```python
INSTALLED_APPS = [
    ...
    'academic',
    ...
]
```

### Database Migration

Run the database migrations to create the necessary tables for the Academic app:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Usage

1. Start the development server:

```bash
python manage.py runserver
```

2. Access the Academic app in a web browser using the following URL:

```
http://localhost:8000/academic/
```

3. Use the provided functionality for department management, class management, section management, session management, class registration, and guide teacher management.

## Dependencies

The Academic app has the following dependencies:

- Django (version 3.2 or above)

Ensure that Django is installed and compatible with your Python environment.

## Additional Considerations

The Academic app relies on the User and Authentication functionality provided by Django's built-in User model. Ensure that user authentication and login functionality are set up and configured correctly before using the Academic app.

Please refer to the project's documentation or contact the system administrator for specific instructions and usage guidelines related to the Academic app.

