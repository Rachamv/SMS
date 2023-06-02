# Account App Documentation

The Account app is a key component of the School Management System. It provides user management, authentication, and profile functionalities for different user roles in the system.

## Functionality

The Account app offers the following features:

1. User Registration: Allows new users to create accounts and access the system.
2. User Authentication: Provides secure authentication for registered users.
3. User Profile Management: Allows users to manage their profiles, including name, photo, and other relevant information.
4. User Role-Based Access: Implements user roles and permissions to control access and functionality based on user roles.
5. Password Reset: Allows users to reset their passwords if forgotten.
6. Dashboard/Home Page: Offers personalized views for different user roles, providing role-specific information and functionality.
7. Logging and Audit Trail: Logs user actions and system events for monitoring and auditing purposes.

## Setup and Configuration

Follow these instructions to set up and configure the Account app:

### Prerequisites

- Python (version 3.6 or above)
- Django framework (version 3.2 or above)
- Pillow package (for image upload support)

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

1. Update the project's `settings.py` file to include the Account app in the `INSTALLED_APPS` setting:

```python
INSTALLED_APPS = [
    ...
    'account',
    ...
]
```

2. Configure the media file storage settings in `settings.py` to handle photo uploads:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

### Database Migration

Run the database migrations to create the necessary tables for the Account app:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Usage

1. Start the development server:

```bash
python manage.py runserver
```

2. Access the Account app in a web browser using the following URL:

```
http://localhost:8000/account/
```

3. Use the provided functionality for user registration, authentication, profile management, and other available features.

## Dependencies

The Account app has the following dependencies:

- Django (version 3.2 or above)
- Pillow (for image upload support)

Ensure that these dependencies are installed and compatible with your Django installation.

## User Roles and Permissions

The Account app defines the following user roles:

1. ChiefExecutive
2. HeadTeacher
3. Secretary
4. Teacher
5. Other Staff
6. Parent
7. Student

Each role has different access levels and permissions within the School Management System. Ensure that user roles are assigned correctly to control access and functionality.

Please refer to the project's documentation or contact the system administrator for specific role-based instructions and usage guidelines.

