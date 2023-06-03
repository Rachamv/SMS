# Administration App Documentation

The Administration app is a key component of the School Management System. It handles the administrative tasks and functionalities related to managing the school, staff, and other administrative processes.

## Functionality

The Administration app offers the following features:

1. User Management: Allows the creation, modification, and deletion of user accounts with different roles and permissions.
2. Staff Management: Provides functionality to manage staff members, including their roles, designations, and contact information.
3. School Information: Allows the management of basic school information such as name, address, contact details, and logo.
4. Academic Year Management: Provides the ability to manage academic years, including setting the current active academic year.
5. School Calendar: Allows the creation and management of important dates and events for the school.
6. Noticeboard: Provides functionality to create and publish notices or announcements for staff and students.
7. Reporting: Offers reporting capabilities to generate various reports related to staff, students, and school activities.

## Setup and Configuration

Follow these instructions to set up and configure the Administration app:

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

1. Update the project's `settings.py` file to include the Administration app in the `INSTALLED_APPS` setting:

```python
INSTALLED_APPS = [
    ...
    'administration',
    ...
]
```

2. Configure the authentication and authorization settings in the `settings.py` file according to your project's requirements.

### Database Migration

Run the database migrations to create the necessary tables for the Administration app:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Usage

1. Start the development server:

```bash
python manage.py runserver
```

2. Access the Administration app in a web browser using the following URL:

```
http://localhost:8000/administration/
```

3. Use the provided functionality for user management, staff management, school information management, academic year management, school calendar, noticeboard, and reporting.

## Dependencies

The Administration app has the following dependencies:

- Django (version 3.2 or above)

Ensure that Django is installed and compatible with your Python environment.

## Additional Considerations

The Administration app relies on user authentication and authorization provided by Django's built-in User model. Ensure that user authentication and login functionality are set up and configured correctly before using the Administration app.

Please refer to the project's documentation or contact the system administrator for specific instructions and usage guidelines related to the Administration app.
