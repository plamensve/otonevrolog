# Otonevrolog.bg

## Overview

The **Otonevrolog** project is a web application designed for managing patient data and appointments for otoneurology specialists. It is built using the Django framework and provides robust features for scheduling, managing records, and generating reports.

---

## Features

- Patient profile management
- Appointment scheduling and notifications
- PDF generation for reports
- QR code integration for quick access
- Secure storage of sensitive data
- Multi-language support (if applicable)
- Admin dashboard for managing all activities

---

## Requirements

Make sure you have the following installed on your machine:

- Python 3.8 or higher
- Django 5.1.2
- PostgreSQL (or any other supported database)
- Other dependencies listed in `requirements.txt`

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/plamensve/otonevrolog.git
   cd otonevrolog

## Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows

## Install the required dependencies:
pip install -r requirements.txt

---

## Configure the environment variables:
Copy the .env.example to .env and update the database credentials and other configurations.

---

## Run the migrations:
python manage.py migrate

---

## Start the development server:
python manage.py runserver

---

## Usage
Access the application via http://127.0.0.1:8000/.
Log in with the default admin credentials or create a new user.

---

## Testing
python manage.py test

---

## Directory Structure
otonevrolog/<br>
1. otonevrolog_main/<br>
1.2 accounts <br>
1.3 blog <br>
1.4 patient_profile <br>
1.5 web <br>
2. static/             ->  # Static files (CSS, JS, Images)<br>
2.1 css <br>
2.2 images <br>
2.3 js <br>
3. templates/          ->  # HTML Templates<br>
3.1 blog <br>
3.2 doctor_profile <br>
3.3 partials <br>
3.4 patient_profile <br>
3.5 pdf_template <br>
3.6 registration <br>
4. tests/              ->  # Unit Tests<br>
4.1 accounts <br>
4.2 blog <br>
4.3 patient_profile <br>
4.4 web <br>
5. settings.py         ->  # Project Settings<br>
6. media/                  ->  # Uploaded Files<br>
7. manage.py               ->  # Project Management Script<br>
8. requirements.txt        ->  # Dependencies<br>
9. README.md               ->  # Project Documentation<br>

---

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any suggestions or improvements.



