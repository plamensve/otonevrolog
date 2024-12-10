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
otonevrolog/
   otonevrolog_main
      media

---

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any suggestions or improvements.



