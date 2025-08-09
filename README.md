# Logistics Dashboard

This repository contains a simple dashboard website for a logistics firm. The app is built using [Flask](https://flask.palletsprojects.com/) and provides a basic overview of key shipment metrics and a sample chart. A basic login form is included to demonstrate user authentication.

## Features
- Displays total shipments processed, shipments currently in transit, and average delivery time.
- Bar chart showing sample data of shipments processed throughout the week.
- Responsive layout using plain CSS.
- Login page with simple credential check.

## Running the Application
1. Install dependencies:
   ```bash
   pip install flask
   ```
2. Start the development server:
   ```bash
   python app.py
   ```
3. Open your browser and navigate to `http://127.0.0.1:5000/` to view the dashboard. Click the **Login** button to sign in with username `admin` and password `password123`.

## Project Structure
```
.
├── app.py              # Flask application
├── templates/
│   ├── index.html      # Dashboard template
│   └── login.html      # Login template
└── static/
    └── style.css       # Basic styling
```

This is an initial prototype and can be expanded with real data integrations and authentication as needed.
