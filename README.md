# Nepali Calendar API

A Flask-based API for Nepali calendar features including date conversion (AD ↔ BS), fetching today's date in both calendars, and managing Nepali festivals. Admin routes are secured by API key authentication, and data is stored in JSON files.

---

## Features

- Convert Gregorian (AD) dates to Nepali Bikram Sambat (BS) and vice versa
- Get today's date in AD and BS with Nepali weekday and digits
- Retrieve festivals for specific years or dates
- Admin API to add festivals (secured with API key authentication)
- Uses JSON files for data persistence — no database required

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/nepali-calendar-api.git
   cd nepali-calendar-api
2. Create and activate a virtual environment:
   python3 -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
3. Install dependencies:
   pip install -r requirements.txt
4. Set your admin API key in utils/auth.py:
   ADMIN_API_KEY = "your-secret-admin-key"
5. Run the Flask app:
   flask run
