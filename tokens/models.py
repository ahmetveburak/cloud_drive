from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string


class Token(models.Model):
    token = models.CharField(max_length=32, default=get_random_string(length=32), verbose_name="Token")
    counter = models.SmallIntegerField(default=0)

    enabled_count = models.SmallIntegerField(default=0)
    enabled_to = models.DateTimeField(blank=True, null=True)
    is_enabled = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.id} | {self.token[:10]}"

    def is_accessible(self) -> bool:
        if self.is_enabled:
            if self.counter < self.enabled_count:
                self.counter += 1
                if self.counter == self.enabled_count:
                    self.is_enabled = False
                self.save()

                return True

            elif self.enabled_to:
                if (self.enabled_to - timezone.now()).days >= 0:
                    return True

                self.is_enabled = False
                self.save()

            elif self.enabled_count == 0 and not self.enabled_to:
                return True

        return False
