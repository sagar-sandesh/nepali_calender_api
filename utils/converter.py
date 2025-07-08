from nepali_datetime import date as nepali_date
from datetime import datetime

# Convert English digits to Nepali digits
def to_nepali_digits(number_str):
    english = '0123456789'
    nepali = '०१२३४५६७८९'
    return ''.join([nepali[english.index(ch)] if ch in english else ch for ch in str(number_str)])


# Convert weekday (in English) to Nepali
def get_nepali_weekday(english_weekday):
    weekdays_np = {
        "Sunday": "आइतबार",
        "Monday": "सोमबार",
        "Tuesday": "मङ्गलबार",
        "Wednesday": "बुधबार",
        "Thursday": "बिहीबार",
        "Friday": "शुक्रबार",
        "Saturday": "शनिबार"
    }
    return weekdays_np.get(english_weekday, english_weekday)


# Convert AD to BS using nepali_datetime
def ad_to_bs(ad_date):
    return nepali_date.from_datetime(ad_date)


# Convert BS to AD using nepali_datetime
def bs_to_ad(bs_date):
    return bs_date.to_datetime_date()
