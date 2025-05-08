from django.db import models
from datetime import datetime
import uuid

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    deleted_at = models.DateTimeField(null=True)

    def set_deleted_at(self):
        self.deleted_at = datetime.now()
        self.save()

    def to_json(self):
        return {
            "id": str(self.id),
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at),
            "deleted_at": self.deleted_at
        }

    class Meta:
        abstract=True
