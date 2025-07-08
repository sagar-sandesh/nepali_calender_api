from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
from nepali_datetime import date as nepali_date
import json
import os

from utils.converter import to_nepali_digits, get_nepali_weekday, ad_to_bs, bs_to_ad
from utils.auth import is_admin_authenticated

app = Flask(__name__)
CORS(app)

DATA_FILE = 'data/festivals.json'


# Load festivals from JSON
def load_festivals():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


# Save festivals to JSON
def save_festivals(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# -----------------------------
# Routes
# -----------------------------

@app.route('/api/today', methods=['GET'])
def get_today():
    today_ad = datetime.today().date()
    today_bs = nepali_date.today()

    response = {
        "ad": today_ad.strftime("%Y-%m-%d"),
        "bs": to_nepali_digits(today_bs.strftime("%Y-%m-%d")),
        "weekday": get_nepali_weekday(today_bs.strftime('%A'))
    }
    return jsonify(response)


@app.route('/api/convert/ad-to-bs', methods=['GET'])
def convert_ad_to_bs():
    ad_date_str = request.args.get('date')
    try:
        ad_date = datetime.strptime(ad_date_str, "%Y-%m-%d")
        bs_date = ad_to_bs(ad_date)
        return jsonify({
            "ad": ad_date_str,
            "bs": to_nepali_digits(bs_date.strftime("%Y-%m-%d"))
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route('/api/convert/bs-to-ad', methods=['GET'])
def convert_bs_to_ad():
    bs_date_str = request.args.get('date')  # Expects 2079-12-25
    try:
        y, m, d = map(int, bs_date_str.split("-"))
        bs_date = nepali_date(y, m, d)
        ad_date = bs_to_ad(bs_date)
        return jsonify({
            "bs": to_nepali_digits(bs_date.strftime("%Y-%m-%d")),
            "ad": ad_date.strftime("%Y-%m-%d")
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route('/api/festivals', methods=['GET'])
def get_festivals():
    year = request.args.get('year')
    data = load_festivals()
    if year:
        return jsonify(data.get(year, {}))
    return jsonify(data)


@app.route('/api/festivals/<bs_date>', methods=['GET'])
def get_festival_by_date(bs_date):
    data = load_festivals()
    year = bs_date.split('-')[0]
    events = data.get(year, {}).get(bs_date, [])
    return jsonify({
        "date": to_nepali_digits(bs_date),
        "events": events
    })


# -----------------------------
# Admin Route: Add Festival
# -----------------------------
@app.route('/api/admin/festival', methods=['POST'])
def add_festival():
    if not is_admin_authenticated(request):
        return jsonify({"error": "Unauthorized"}), 401

    body = request.get_json()
    bs_date = body.get("date")  
    event = body.get("event")

    if not bs_date or not event:
        return jsonify({"error": "Missing fields"}), 400

    data = load_festivals()
    year = bs_date.split("-")[0]

    if year not in data:
        data[year] = {}
    if bs_date not in data[year]:
        data[year][bs_date] = []

    data[year][bs_date].append(event)
    save_festivals(data)

    return jsonify({"message": "Event added", "date": bs_date, "event": event})

if __name__ == '__main__':
    app.run(debug=True)
