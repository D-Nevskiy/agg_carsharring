from django.db import models
from django.utils import timezone

from django.contrib.auth import get_user_model

User = get_user_model()


class Bonus(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="bonuses",
    )
    amount = models.IntegerField(default=0)
    created_at = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.email}'s Bonuses"
