# Attendance App Documentation

The Attendance app is a Django-based web application that allows teachers or administrators to manage and track attendance for students and employees. It provides functionality to mark attendance, search and filter attendance records, generate attendance reports, and perform bulk attendance updates.

## Table of Contents
1. [Installation](#installation)
   - [Prerequisites](#prerequisites)
   - [Setup](#setup)
2. [Usage](#usage)
   - [Marking Attendance](#marking-attendance)
   - [Searching Attendance](#searching-attendance)
   - [Generating Reports](#generating-reports)
   - [Bulk Attendance Updates](#bulk-attendance-updates)
3. [Configuration](#configuration)
4. [Contributing](#contributing)
5. [License](#license)

## Installation

### Prerequisites

Before setting up the Attendance app, make sure you have the following prerequisites installed on your system:

- Python (version 3.6 or higher)
- Django (version 3.2 or higher)
- Other dependencies specified in the `requirements.txt` file of the app.

### Setup

To set up the Attendance app, follow these steps:

1. Clone the repository or download the source code from the project's repository.

2. Navigate to the project directory using the command line.

3. Create a virtual environment to isolate the app's dependencies:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

6. Apply the database migrations to create the necessary tables:

   ```bash
   python manage.py migrate
   ```

7. (Optional) Load sample data (e.g., classes, students, employees) into the database:

   ```bash
   python manage.py loaddata sample_data.json
   ```

8. Start the development server:

   ```bash
   python manage.py runserver
   ```

9. Access the app in your web browser at `http://localhost:8000/attendance/`.

## Usage

### Marking Attendance

1. To mark attendance for a student, go to the URL `/attendance/student/<class_name>/<student_id>/`, where `<class_name>` is the ID of the class and `<student_id>` is the ID of the student.

2. Select the appropriate period and attendance status from the form.

3. Click the "Submit" button to mark the attendance. The student's attendance record will be saved in the database.

### Searching Attendance

1. On the main attendance page (`/attendance/`), you can use the search form to filter attendance records based on various criteria such as date, student name, student ID, class name, employee name, and employee ID.

2. Enter the desired search parameters and click the "Search" button to filter the attendance records accordingly.

3. The filtered attendance records will be displayed on the same page.

### Generating Reports

1. To generate an attendance report, go to the URL `/attendance/attendance_report/`.

2. The attendance report will be generated as a PDF file and downloaded automatically. The report includes attendance information for both students and employees.

### Bulk Attendance Updates

1. To perform bulk attendance updates for multiple students, go to the URL `/attendance/student/bulk/`.

2. Select the desired class and period from the form.

3. Choose the attendance status (

e.g., present, absent) for all the students in the class.

4. Click the "Submit" button to update the attendance for all selected students simultaneously.

## Configuration

The Attendance app comes with some configurable options that you can adjust according to your needs. The main configuration files are:

- `settings.py`: This file contains the general configuration settings for the Django project, including database settings, static files, templates, etc.

- `forms.py`: This file defines the forms used in the app, allowing you to customize the form fields, widgets, and validation as required.

- `models.py`: This file defines the database models used in the app, allowing you to modify the structure and behavior of the attendance-related objects.

- `urls.py`: This file contains the URL patterns for the app, allowing you to define the routing and URL structure.

Please refer to the Django documentation for more information on configuring Django projects and apps.

## Contributing

If you would like to contribute to the Attendance app, please follow these steps:

1. Fork the repository and clone it to your local machine.

2. Create a new branch for your feature or bug fix.

3. Make the necessary changes in your branch.

4. Write tests to cover the changes, ensuring that the existing tests pass as well.

5. Commit your changes and push them to your forked repository.

6. Submit a pull request detailing your changes and explaining their purpose.

We appreciate your contributions!

## License

The Attendance app is open-source software released under the [MIT License](https://opensource.org/licenses/MIT). You are free to use, modify, and distribute the code as per the terms of the license.