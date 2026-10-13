CAMPUS NOTIFY
Campus Announcement and Emergency Alert System

==================================================
1. PROJECT OVERVIEW
==================================================

Campus Notify is a student project developed using Python and Streamlit. It provides a simple web application for displaying campus announcements and emergency alerts in one place.

The application has a pink-themed interface and allows users to view notifications. Administrators can create routine announcements and emergency notifications.

The main features include:

- Viewing campus announcements and emergency alerts.
- Creating routine notifications.
- Creating emergency notifications.
- Searching for notifications.
- Filtering notifications by type.
- Saving notifications in a local JSON file.
- Recording simulated SMS activity for emergency notifications.

IMPORTANT:
The SMS feature is simulated for demonstration and testing. The application does not send real SMS messages to students or staff.

==================================================
2. PROJECT FILES
==================================================

Keep all the following files together in the same project folder.

1. app.py
   This is the main Python file that runs the Campus Notify application.

2. notifications.json
   This file stores notification records created through the application.

3. sms_log.json
   This file stores records of simulated SMS activity associated with emergency notifications.

4. requirements.txt
   This file lists the Python packages required to run the application.

5. README.txt
   This file explains the project, its features, and how to install and run it.

Do not separate these files from the main application. The application needs its supporting JSON files to work correctly.

==================================================
3. SYSTEM REQUIREMENTS
==================================================

To run Campus Notify, you need:

- A computer running Windows, macOS, or Linux.
- Python installed on the computer.
- A web browser such as Google Chrome or Microsoft Edge.
- Internet access to install the required Python packages, if they are not already installed.
- Visual Studio Code is recommended but is not compulsory.

==================================================
4. INSTALLATION INSTRUCTIONS
==================================================

Follow these steps to install and run Campus Notify.

STEP 1: Download the project.

Download the project ZIP file or copy the project folder to your computer.

STEP 2: Extract the project.

If you downloaded a ZIP file, right-click it and select "Extract All".

STEP 3: Open the project folder.

Open the extracted folder containing app.py, notifications.json, sms_log.json, requirements.txt, and README.txt.

STEP 4: Open a terminal.

You can open the folder in Visual Studio Code and select:

Terminal > New Terminal

Make sure the terminal is working inside the folder containing app.py.

STEP 5: Install the required packages.

Run this command:

python -m pip install -r requirements.txt

Wait for the installation to finish.

STEP 6: Start Campus Notify.

Run this command:

python -m streamlit run app.py

STEP 7: Open the application.

Streamlit will display a local address in the terminal, usually:

http://localhost:8501

Open that address in your web browser to use Campus Notify.

IMPORTANT:
Keep the terminal open while using the application. Closing the terminal stops the running application.

To stop the application, click inside the terminal and press Ctrl+C.

If the "python" command is not recognised on Windows, try using "py" instead:

py -m pip install -r requirements.txt

py -m streamlit run app.py

==================================================
5. HOW TO USE CAMPUS NOTIFY
==================================================

A. STUDENT VIEW

The Student View allows users to view campus announcements and emergency alerts.

Depending on the available options in the application, users can:

- Read notification titles and messages.
- View the notification type.
- Search for notifications.
- Filter notifications by type.
- View saved campus announcements and emergency alerts.

B. ADMINISTRATOR LOGIN

Select "Admin Login" in the application's sidebar to access the administrator section.

The current demonstration login credentials are:

Username: admin
Password: campus123

These credentials are included for classroom demonstration purposes only.

They are not suitable for a real production system. A real deployment should use secure authentication and appropriate access controls.

C. CREATING A NOTIFICATION

After logging in as an administrator:

1. Open the notification creation section.
2. Enter the notification title.
3. Enter the notification message.
4. Select the notification type.
5. Choose either Routine or Emergency.
6. If required, confirm that you want to publish an emergency notification.
7. Click the appropriate button to publish the notification.

The notification should then appear in the application's notification list.

D. EMERGENCY NOTIFICATIONS

Emergency notifications are intended to communicate urgent campus information.

When an emergency notification is created, the application is designed to record simulated SMS activity in sms_log.json.

This is only a simulation. The application does not send actual SMS messages or confirm delivery to any recipient.

E. NOTIFICATION HISTORY

The application stores notification records in notifications.json.

The saved records can be used to display notification history when the application is running.

==================================================
6. DATA STORAGE
==================================================

Campus Notify uses local JSON files to store its data.

The two main data files are:

- notifications.json
- sms_log.json

The application does not require a separate database server for this prototype.

Keep these files in the same folder as app.py.

Make backup copies of important project files before making changes.

If the application is shared publicly, make sure the JSON files do not contain private student information, confidential messages, or real personal phone numbers.

==================================================
7. TESTING
==================================================

The application should be tested before submission to confirm that its features work as expected.

Suggested tests include:

1. Create a routine notification and check whether it appears in the application.
2. Create an emergency notification and check whether it appears.
3. Check whether new notifications are saved in notifications.json.
4. Check whether emergency activity is recorded in sms_log.json.
5. Create multiple notifications and check whether the earlier records remain saved.
6. Restart the application and check whether saved notifications are still available.
7. Test the search and filtering features, if available.

Record the actual result of each test.

Only report a test as successful after performing it and observing the result.

A simulated SMS record is not proof that a real SMS message was sent or delivered.

==================================================
8. KNOWN LIMITATIONS
==================================================

Campus Notify is an educational prototype and has the following limitations:

- SMS activity is simulated; integration with a real SMS gateway is not included.
- Notification data is stored in local JSON files rather than a central database.
- The demonstration administrator credentials are hard-coded.
- The system is not designed to replace an official emergency communication service.
- The local application must be running for users to access it through its local web address.
- Additional security, testing, and reliability improvements would be needed before real-world deployment.

==================================================
9. SOURCE CODE AND GITHUB
==================================================

The project's source code can be stored in a GitHub repository.

GitHub allows users to view and download the source files. However, storing the code on GitHub does not automatically make Campus Notify available as a live website.

To run the application locally, download the project files, extract them if necessary, install the dependencies, and follow the installation instructions in this README.

==================================================
10. FUTURE IMPROVEMENTS
==================================================

Possible future improvements include:

- Integration with a legitimate SMS gateway to send actual messages.
- A central database for storing notifications.
- More secure administrator authentication.
- Different access levels for administrators, staff, and students.
- Improved reporting and notification history.
- More extensive system testing.
- Online deployment so authorised users can access the application through a web browser.

==================================================
11. PROJECT PURPOSE
==================================================

Campus Notify demonstrates how a lightweight web application can help centralise campus announcements and provide a basic emergency-alert workflow.

The project applies programming and web application development concepts to a campus communication scenario.

It provides a foundation that can be extended with additional features, security improvements, and real communication services in the future.

==================================================

CAMPUS NOTIFY
Student Project Prototype