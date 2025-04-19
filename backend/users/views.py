# from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import json
from .models import User
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

def create(request: HttpRequest):
    dict_body = json.loads(request.body)
    u = User(
        name=dict_body.get("name"),
        email=dict_body.get("email"),
        password=dict_body.get("password"),
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    u.save()

    return HttpResponse(json.dumps({
        "message": "User created"
    }))

def list(request: HttpRequest):
    users = User.objects.all()
    users_dict = [u.to_json() for u in users]
    return HttpResponse(json.dumps(users_dict))

@csrf_exempt
def index(request: HttpRequest):
    match request.method:
        case "GET":
            return list(request)
        case "POST":
            return create(request)
        case _:
            return HttpResponse(b"Method not mapped")

