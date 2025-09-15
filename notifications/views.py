from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .utils import send_email_via_automation

@csrf_exempt  # disable CSRF for simplicity (not for production!)
def send_email_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            result = send_email_via_automation("/send-mail", data)

            if result is not None:
                return JsonResponse({"status": "success", "data": result}, status=200)
            else:
                return JsonResponse({"status": "error", "message": "Failed to send email"}, status=400)

        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)

    return JsonResponse({"error": "Only POST allowed"}, status=405)
