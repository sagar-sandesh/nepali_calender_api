from flask import request

# Set your admin key here (change this before deploying!)
ADMIN_API_KEY = "your-secret-admin-key"

def is_admin_authenticated(req: request):
    key = req.headers.get("x-api-key")
    return key == ADMIN_API_KEY
