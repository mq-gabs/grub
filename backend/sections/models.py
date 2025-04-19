from django.db import models
from base.models import BaseModel
from users.models import User

class Section(BaseModel):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=64)
    active = models.BooleanField()

    def __str__(self):
        return f"Name: {self.name}, Active: {self.active}"

class Item(BaseModel):
    section = models.ForeignKey(Section, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    price = models.PositiveIntegerField()
    image_src = models.CharField(max_length=512)
    active = models.BooleanField()

    def __str__(self):
        return f"Name: {self.name}, Description: {self.description}, Price: {self.price}, Active: {self.active}"
