## Event App Documentation

The event app is a component of the school management system that allows users to create, manage, and attend various events within the school. This documentation provides an overview of the app's functionality, instructions for usage, and details on the configuration.

### Functionality

The event app offers the following key features:

1. Event Creation: Users with appropriate permissions (HeadTeacher and ChiefExecutive) can create new events, providing details such as title, description, start and end dates, location, organizer, and optional image.

2. Recurring Events: Events can be marked as recurring, allowing users to specify the recurrence type, frequency, interval, and end date.

3. Event Attendance: Students, parents, and teachers can be associated with events through the attendance fields, allowing organizers to track attendee information.

4. Event Visibility: Events can be categorized as public, internal, or restricted, controlling the visibility and access to the event details.

5. Event Documents: Documents related to events, such as schedules, presentations, or handouts, can be attached using the EventDocument model.

6. Event Feedback and Ratings: Users can provide feedback and ratings for events using the EventFeedback model.

7. Event Sponsors: Sponsors can be associated with events, and their visibility can be controlled individually.

### Installation and Configuration

To set up the development environment and run the event app, follow these steps:

#### Prerequisites

- Python 3.x
- Django (version 3.x or above)
- Database (e.g., PostgreSQL, MySQL, SQLite)

#### Installation

1. Clone the repository or download the project files.

2. Create a virtual environment using the command:

   ```
   $ python3 -m venv myenv
   ```

3. Activate the virtual environment:

   - For Windows:
     ```
     $ myenv\Scripts\activate
     ```

   - For Linux/Mac:
     ```
     $ source myenv/bin/activate
     ```

4. Install the project dependencies:

   ```
   $ pip install -r requirements.txt
   ```

5. Configure the Database:
   - Update the database settings in the `settings.py` file, including the database engine, name, user, password, and host.

6. Apply migrations to create the necessary database tables:

   ```
   $ python manage.py migrate
   ```

#### Usage

To run the event app:

1. Start the Django development server:

   ```
   $ python manage.py runserver
   ```

2. Access the event app in a web browser using the provided URL (e.g., `http://localhost:8000/events`).

3. Create an admin account by running the following command:

   ```
   $ python manage.py createsuperuser
   ```

   Follow the prompts to provide a username, email, and password.

4. Log in to the admin interface (`http://localhost:8000/admin`) using the admin account created in the previous step.

5. Create events, manage attendees, attach documents, configure visibility, and perform other administrative tasks through the admin interface.

#### Tests

To run the tests for the event app:

1. Ensure that the virtual environment is activated.

2. Run the following command:

   ```
   $ python manage.py test event
   ```

   The tests will be executed, and the results will be displayed in the console.

### Conclusion

The event app provides a comprehensive solution for managing events within the school management system. By following the installation and usage instructions outlined in this documentation, administrators can create, manage, and track various events, ensuring effective communication and organization within the school community.



