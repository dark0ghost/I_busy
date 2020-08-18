from tortoise.models import Model
from tortoise import fields


class User(Model):
    id = fields.IntField(pk=True)
    login_key = fields.TextField

    def __str__(self):
        return self.id
