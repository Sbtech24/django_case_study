import requests
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def send_email_via_automation(payload):
    """
    Sends email requests through the automation workflow,
    differentiating between staging and production environments.
    """
    try:
        print("Payload received:", payload) 
        # For demo/mock, we’ll just use httpbin
        
        workflow_url = f"{settings.AUTOMATION_WORKFLOW_URL}"
       
          
        
        response = requests.post(workflow_url, json=payload, timeout=5)

        print("URL:", workflow_url)  # debug
        print("Status code:", response.status_code)  # debug
        print("Response text:", response.text)  # debug

        if response.status_code == 200:
            return {
                "workflow_response": response.json(),
                "original_payload": payload  
            }
        else:
            logger.error(
                "Failed to send email via automation workflow",
                extra={"status_code": response.status_code, "payload": payload}
            )
            return None
    except requests.RequestException as e:
        logger.exception(f"Exception occurred while sending email: {e}")
        return None
