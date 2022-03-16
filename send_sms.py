import requests

from get_name import name
from get_last_name import last_name
from get_email import email
from get_phone import phone_number


url = "https://fatsms.com/send-sms"
message = f"Hej {name} {last_name}, din email er {email}"
payload = {
    "message": message,
    "api_key": "ed39def1-9d29-4855-abdf-ff023dc3d7a7",
    "to_phone": phone_number,
}

req = requests.post(url, data=payload)
print(req)
print(message)
