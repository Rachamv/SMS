# Office of Admin

===Model===

We have a `Event` model with the following fields:

- `title`: Represents the title or name of the event. It is a `CharField` with a maximum length of 100 characters.
- `description`: Represents the description or details of the event. It is a `TextField` that can hold a large amount of text.
- `start_date` and `end_date`: Represent the start and end dates and times of the event. They are `DateTimeField` fields that store both date and time information.
- `location`: Represents the location or venue of the event. It is a `CharField` with a maximum length of 100 characters.
In this updated version, we have added two additional fields:

- `organizer`: Represents the user who organized the event. It is a foreign key to the `User` model provided by Django's authentication system. The `on_delete=models.CASCADE` parameter specifies that if the user is deleted, all associated events will also be deleted.
- `image`: Represents an image related to the event. It is an `ImageField` that allows users to upload an image. The `upload_to` parameter specifies the directory where the uploaded images will be stored. The `blank=True, null=True` parameters allow the field to be optional.

To implement recurring events, introducie additional fields in the `Event` model to handle 

The `is_recurring` field is a boolean flag that indicates whether the event is recurring or not. If it is set to `True`, then the event is considered a recurring event.

The `recurrence_type` field stores the type of recurrence pattern, such as "daily", "weekly", "monthly", etc.

The `recurrence_frequency` field represents the number of times the event should occur based on the recurrence type. For example, if the recurrence type is set to "weekly" and the recurrence frequency is set to 2, the event will occur every 2 weeks.

The `recurrence_interval` field specifies the interval between each occurrence of the event. For example, if the recurrence type is set to "monthly" and the recurrence interval is set to 3, the event will occur every 3 months.

The `recurrence_end_date` field allows you to set an end date for the recurring events. After the end date, the event will no longer recur.

- Attendance fields: `students_attending`, `parents_attending`, and `teachers_attending` are ManyToManyFields that establish relationships between an event and the students, parents, and teachers attending the event.
- Visibility field: The `visibility` field is a CharField with choices to determine the visibility of the event (public, internal, restricted).
- Sponsorship field: The `sponsors` field is a ManyToManyField that relates the Event model with the Sponsor model to track event sponsors.
- EventDocument model: The `EventDocument` model allows attachments of documents related to the event, such as schedules, presentations, or handouts. It has a ForeignKey to the Event model and a FileField to store the document files.
- EventFeedback model: The `EventFeedback` model allows users to provide feedback and ratings for events. It has a ForeignKey to the Event model, a ForeignKey to the User model, and fields for rating and comments.
The `show_sponsor` field is added as a BooleanField with a default value of `True`. This field indicates whether the sponsor should be shown or hidden. 


===Views===
We have created several views:

1. `event_list`: Retrieves all events from the database and renders the `event_list.html` template, passing the events as context.
2. `event_detail`: Retrieves a specific event based on the provided `event_id` and renders the `event_detail.html` template, passing the event as context.
3. `create_event`: Handles both GET and POST requests. For GET requests, it renders the `create_event.html` template with an empty form to create a new event. For POST requests, it processes the submitted form data, creates a new event, and redirects to the event list page.
4. `edit_event`: Handles both GET and POST requests. For GET requests, it retrieves the event based on the provided `event_id` and renders the `edit_event.html` template with a form pre-populated with the event data. For POST requests, it processes the submitted form data, updates the event, and redirects to the event detail page.
5. `delete_event`: Retrieves the event based on the provided `event_id`, handles the deletion of the event, and redirects to the event list page.
6. `form.save_m2m()` method is used to save the many-to-many relationships, including the sponsors.
7.  The view checks if the user's group is either `Director` or `ChiefExecutive` using the `request.user.groups.filter()` method. If the user does not belong to either of these groups, an error message is displayed and they are redirected to the event list page.


===Urls===
The `event/urls.py` file is used to define URL patterns for the Event app:

===Admin===

For the `Event` model, we customize the displayed fields using `list_display` and add filters for `start_date`, `end_date`, and `organizer` using `list_filter`. We also enable search on `title` and `description` using `search_fields`.

For the `Sponsor` model, we define `list_display` to show the sponsor's name and their visibility status (`show_sponsor`). We add a filter for the `show_sponsor` field.

The `EventDocument` and `EventFeedback` models use the default `ModelAdmin` class, so we don't need to customize them further.


===Forms===

In this form, we're using `ModelForm` provided by Django to create a form based on the `Event` model. The `Meta` class specifies the model and fields to include in the form.

The `widgets` attribute is used to customize the rendering of the `start_date` and `end_date` fields. In this example, we're adding a CSS class called `datetime-input` to style the datetime inputs in a custom way. You can modify the widget attributes to suit your specific needs.


===Tests===

A `TestCase` subclass called `EventTests` to perform various tests related to event creation. We set up test users using the `setUp` method, which creates a head teacher, a chief executive, and a normal user.

The `test_event_creation` method tests the event creation functionality. It first logs in as a normal user and checks if accessing the event creation page is forbidden. Then it logs in as the head teacher and checks if the head teacher can access the event creation page. It then creates an event by making a POST request to the event creation view and checks if the event is created successfully and has the correct attributes. Finally, it logs in as the chief executive and performs the same checks for event creation.


```````````````````````````````````````````
Here are some suggestions to enhance the functionality of the event app:

1. RSVP Functionality: Allow users to RSVP for events, indicating their attendance status. This can be implemented by adding a field to the Event model to track the attendees' responses.

2. Event Categories: Implement a feature to categorize events based on different criteria such as academic, sports, cultural, etc. This can help users easily filter and find events of their interest.

3. Event Reminders: Provide the option for users to set reminders for upcoming events. This can be implemented by sending notifications or emails to users a specified time before the event starts.

4. Event Registration: If there are events that require registration or ticketing, add a registration feature where users can sign up and receive event tickets or confirmations.

5. Event Comments/Reviews: Allow users to leave comments or reviews on events they attended. This can help gather feedback and improve future events.

6. Event Sharing: Enable users to share events on social media platforms or via email, allowing them to invite friends and promote the event.

7. Event Analytics: Implement analytics to track event attendance, user engagement, and other metrics. This data can provide insights for event planning and evaluation.

8. Event Notifications: Set up a notification system to inform users about event updates, changes, or cancellations.

9. Event Search and Filtering: Add search functionality to allow users to search for events based on keywords, dates, locations, or other relevant criteria.

10. Event Archives: Create a section to archive past events, making it easy for users to access event details and resources even after the event has ended.


````````````````````````````````````````
To optimize the performance of our Django event app, we can consider the following techniques:

1. Database Optimization:
   - Ensure that your database schema is properly designed with appropriate indexes and relationships.
   - Analyze and optimize database queries using tools like Django Debug Toolbar or database query analyzers.
   - Use database-specific optimizations, such as database query caching, database connection pooling, or database query optimization techniques.

2. Caching:
   - Utilize caching mechanisms to reduce the load on the database and improve response times.
   - Implement Django's caching framework to cache database queries, rendered templates, or expensive function calls.
   - Use cache middleware to cache entire pages or parts of pages to serve them faster to subsequent users.

3. Query Optimization:
   - Avoid unnecessary database queries by using Django's select_related() and prefetch_related() methods to fetch related objects in a single query.
   - Optimize queryset filtering by using appropriate filters, indexing, and database-specific query optimizations.
   - Use Django's queryset methods like values(), only(), or defer() to retrieve only the required fields from the database.

4. Efficient Template Rendering:
   - Minimize the use of complex logic or heavy processing in templates. Preprocess data in views before passing it to templates.
   - Use template fragment caching to cache specific sections of templates that don't change frequently.
   - Implement template compression to reduce the size of HTML/CSS/JS files and improve load times.

5. Pagination:
   - Implement pagination for large datasets to avoid retrieving and rendering all records at once.
   - Use Django's built-in pagination classes and limit the number of records fetched per page.

6. Asynchronous Tasks:
   - Offload time-consuming tasks to asynchronous queues using tools like Celery or Django Channels.
   - Perform tasks like sending emails, processing file uploads, or generating reports in the background.

7. Profiling and Monitoring:
   - Use profiling tools like Django Silk or Django Debug Toolbar to identify performance bottlenecks and optimize critical code paths.
   - Monitor your application's performance using tools like Django Silk, Django Silk Dashboard, or monitoring solutions like New Relic or Datadog.

8. HTTP Caching and Compression:
   - Leverage browser caching by setting appropriate cache headers in HTTP responses.
   - Implement HTTP compression to reduce the size of the transferred data.

9. Load Testing and Scalability:
   - Conduct load testing to identify performance limitations and optimize your application's scalability.
   - Consider scaling your application horizontally by adding more servers or using cloud-based solutions.

Remember to analyze and optimize based on your specific application's requirements and usage patterns. Performance optimization is an iterative process, so monitor and fine-tune your app regularly.

Note that certain optimizations might require trade-offs, so make sure to benchmark and test your application to ensure the optimizations yield the desired performance improvements without compromising functionality.

As always, it's essential to profile and measure the performance impact of each optimization to ensure it provides the desired benefits.
