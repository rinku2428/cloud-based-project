# User Guide

This guide provides instructions on setting up and using the Cloud-Based Project web application.

## Setup Instructions

1. **Clone the Repository**: Clone the project repository from GitHub.
    ```bash
    git clone <repository-url>
    ```

2. **Navigate to Project Directory**: Change into the project directory.
    ```bash
    cd cloud-based-project
    ```

3. **Install Dependencies**: Install project dependencies using pip.
    ```bash
    pip install -r src/requirements.txt
    ```

4. **Set Up Environment Variables**: Create a `.env` file in the `src/` directory and add the required environment variables.
    ```plaintext
    SECRET_KEY=<your-secret-key>
    DEBUG=True
    ```

5. **Run Migrations**: Apply database migrations to set up the database schema.
    ```bash
    python src/manage.py migrate
    ```

6. **Start the Development Server**: Launch the Django development server.
    ```bash
    python src/manage.py runserver
    ```

7. **Access the Application**: Open a web browser and navigate to `http://localhost:8000` to access the application.

## Usage

- **Home Page**: The landing page of the web application.
- **About Us Page**: Information about the university.
- **Contact Us Page**: Form to send inquiries to the university.
- **List of Modules Page**: Display of modules available for registration.
- **Module Details Page**: Details of a specific module, including registration options.
- **Registration Page**: Form for student registration.

