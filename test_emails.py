import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "casestudy.settings")
django.setup()

from notifications.utils import send_email_via_automation

payload = {
    "to": "test@example.com",
    "from": "Medbuddy <info@medbuddyafrica.com>",
    "context": {
        "user_first_name": "John",
        "referred_user_name": "Jane",
        "course_name": "Python Basics",
        "currency": "NGN",
        "referral_value": 5000,
        "referral_tracking_page_url": "https://medbuddyafrica.com/app/referrals",
        "recipient": "test@example.com",
    },
    "template": "medbuddy_referral_followup",
}

result = send_email_via_automation("/send-mail", payload)
print(result)
