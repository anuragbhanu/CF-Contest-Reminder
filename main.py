import requests
from datetime import datetime
import pytz
from twilio.rest import Client

CF_URL = "https://codeforces.com/api/contest.list"
account_sid = "Your Twilio Account SID "
auth_token = "Your Twilio Auth Token"
twilio_Number = "Your Twilio phone number"
Phone_Number = "Your Phone Number with Country Code"


def get_contest_list():
    try:
        response = requests.get(CF_URL)
        response.raise_for_status()
        contest_data = response.json()
        upcoming_contest_list = []
        if contest_data["status"] == "OK" and "result" in contest_data:
            for contest in contest_data["result"]:
                if "phase" in contest and contest["phase"] == "BEFORE":
                    upcoming_contest_list.append({"id": contest.get("id", ""),
                                                  "name": contest.get("name", ""),
                                                  "type": contest.get("type", ""),
                                                  "durationSeconds": contest.get("durationSeconds", 0),
                                                  "startTimeSeconds": contest.get("startTimeSeconds", 0),
                                                  "relativeTimeSeconds": contest.get("relativeTimeSeconds", 0)})
        return upcoming_contest_list
    except requests.exceptions.RequestException as e:
        print(f"Error fetching contest data: {e}")
        return []
    except KeyError as e:
        print(f"Key error in contest data: {e}")
        return []


def get_time(timestamp):
    tz = pytz.timezone('Asia/Kolkata')
    dt = datetime.fromtimestamp(timestamp, tz=tz)
    hour = dt.hour
    now = "AM"
    if hour > 12:
        hour -= 12
        now = "PM"
    minute = dt.minute
    zero = ""
    if minute < 10:
        zero = "0"
    return f"{hour} : {zero}{minute} {now}"


def send_sms():
    contests_list = get_contest_list()

    for contest in contests_list:
        if "Div." in contest["name"]:
            if contest["relativeTimeSeconds"] * (-1) <= 86400:
                contest_name = contest["name"]
                start_time = get_time(contest["startTimeSeconds"])

                client = Client(account_sid, auth_token)
                message = client.messages \
                    .create(
                    body=f"Codeforces Round Alert:\n Contest Name: {contest_name}\n Start Time: {start_time} \n Make sure to prepare and give it your best shot! 🌟💻🔢 \n Happy Coding! 🚀 ",
                    from_=f"{twilio_Number}",
                    to=f"{Phone_Number}"
                )

send_sms()
