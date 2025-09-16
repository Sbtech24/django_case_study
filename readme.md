# Case Study – Referral Email Workflow

## Overview

This solution implements the case study requirements:

- **Backend (Django)**:

  - Utility function `send_email_via_automation` ensures all emails go through automation workflow tools.
  - Handles staging vs production environments.
  - Provides a `/send-email/` endpoint to receive form data.
  - Currently posts to `https://httpbin.org/post` as a mock automation service (so no real emails are sent).

- **Frontend (Next.js, App Router)**:
  - A simple form to collect user details required by the workflow.
  - API route forwards form data to the Django backend.
  - Shows success or failure messages to the user.

## Live Demo

- **Backend (Django)**: [Live URL](https://casestudy-backend-30hi.onrender.com/send-email)
- **Frontend (Next.js)**: [Live Sandbox](https://codesandbox.io/p/devbox/case-study-frontend-form-d4xpsh)

## Notes

- Emails are mocked using `httpbin.org`. The payload you submit is echoed back in the response, demonstrating the workflow without sending real emails.
- In a real environment, `AUTOMATION_WORKFLOW_URL` in `settings.py` would point to the actual automation tool.
