# Nepali Calendar API 🇳🇵

A lightweight Flask API to effortlessly work with Nepali dates.  
Convert between Gregorian (AD) and Nepali Bikram Sambat (BS), get today’s date with Nepali digits & weekday, and manage festivals—all with simple REST endpoints. Easy to use and light weight.

---

## 🚀 Quick Setup

1. **Clone & install dependencies:**

```bash
git clone https://github.com/yourusername/nepali-calendar-api.git
cd nepali-calendar-api
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```
2. **Set your admin API key:**
```bash
ADMIN_API_KEY = "your-secret-admin-key"
```

3. **Run the server:**
 ```bash
flask run
```

## 🌟 Features
**✅ Convert AD ↔ BS dates**

**✅ Get today’s date in both calendars with Nepali weekday & digits**

**✅ Retrieve festivals by year or date**

**✅ Add new festivals via secured admin API**

**✅ Simple JSON-based data storage — no database needed**


## 📬 API Endpoints

| Endpoint                  | Method | Description                  | Parameters                   |
|---------------------------|--------|------------------------------|------------------------------|
| `/api/today`              | GET    | Today’s date (AD, BS, weekday) | —                            |
| `/api/convert/ad-to-bs`   | GET    | Convert AD to BS              | `?date=YYYY-MM-DD`           |
| `/api/convert/bs-to-ad`   | GET    | Convert BS to AD              | `?date=YYYY-MM-DD`           |
| `/api/festivals`          | GET    | Get festivals (all or by year) | Optional `?year=YYYY`        |
| `/api/festivals/<bs_date>`| GET    | Festivals on a specific BS date | Path param: `YYYY-MM-DD` (BS) |
| `/api/admin/festival`     | POST   | Add festival (admin only)     | JSON body + `x-api-key` header |


## 🔐 Admin Authentication
- Protect admin routes with x-api-key header
- Set your key in utils/auth.py

## 📦 Requirements
- Flask
- flask-cors
- nepali-datetime

## 📝 License
This project is licensed under the MIT License.

## 👤 Author
Mr. Sagar Sandesh Oli

📧 olisagarsandesh@gmail.com

📍 Based in Finland 🇫🇮 | Originally from Nepal 🇳🇵
