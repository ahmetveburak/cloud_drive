from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _


class Token(models.Model):
    token = models.CharField(_("Token"), max_length=32, unique=True)
    counter = models.SmallIntegerField(_("View Count"), default=0)

    enabled_count = models.SmallIntegerField(_("View Limit"), default=0)
    enabled_to = models.DateTimeField(_("Expiration Date"), blank=True, null=True)
    is_enabled = models.BooleanField(_("Active Status"), default=True)

    created = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.id} | {self.token[:10]}"

    def is_accessible(self) -> bool:
        if not self.is_enabled:
            return False

        if self.enabled_count == 0 and not self.enabled_to:
            return True

        if self.counter < self.enabled_count:
            self.counter += 1
            if self.counter == self.enabled_count:
                self.is_enabled = False
            self.save()
            return True

        if self.enabled_to:
            if (self.enabled_to - timezone.now()).days >= 0:
                return True
            self.is_enabled = False
            self.save()

        return False
