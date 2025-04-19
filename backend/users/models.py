from base.models import BaseModel
from django.db import models

class User(BaseModel):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    password = models.CharField(max_length=128)

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Password: {self.password}"

    def to_json(self):
        base_json = super().to_json()
        base_json.update({
            "name": self.name,
            "email": self.email,
            "password": self.password,
        })
        return base_json
