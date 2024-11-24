<h1>Otonevrolog.bg</h1>
Otonevrolog Main is a Django-based medical application designed to manage patient profiles, appointment scheduling, and user accounts. The application aims to streamline the process of booking and managing medical appointments for both patients and healthcare providers.<br>

![fornt_read_me](https://github.com/user-attachments/assets/4837bbd4-e550-49cc-9aaa-54a236e6a4ef)

<h1>Features</h1>
User Authentication: Secure registration, login, and logout functionality for patients and administrators.
Patient Profiles: Each patient has a personalized dashboard with the ability to view and edit their profile.
Appointment Scheduling: Patients can book appointments, view available slots, and manage their bookings.
Responsive Design: The application includes a user-friendly interface with CSS and JavaScript enhancements for mobile and desktop users.

![register](https://github.com/user-attachments/assets/41db56f7-5829-4fe1-8bbe-d60bd395be41)

<h1>Installation</h1>
Clone the repository:


git clone https://github.com/yourusername/otonevrolog_main.git
cd otonevrolog_main
Create a virtual environment:


python3 -m venv .venv
source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
Install dependencies:


pip install -r requirements.txt
Apply migrations:


python manage.py migrate
Run the server:


python manage.py runserver
Access the application: Open your browser and navigate to http://127.0.0.1:8000.

<h1>Directory Structure</h1>
accounts/: Manages user registration, authentication, and profile details.
patient_profile/: Manages patient-specific data and functionalities like dashboard and profile updates.
web/: Core application functionalities, including appointment booking and slot management.
static/: Contains CSS, JavaScript, and image assets for front-end styling and interaction.
templates/: HTML templates organized by feature (e.g., registration, profiles, dashboard).

<h1>Configuration</h1>
To configure this project, edit the settings in settings.py, including database configuration, static files, and other Django settings.


<h1>Contribution</h1>
Feel free to submit pull requests or report issues to help improve the application. All contributions are welcome!
