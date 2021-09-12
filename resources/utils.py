from datetime import datetime

from django.utils import timezone
from django.utils.crypto import get_random_string
from django.utils.dateparse import parse_datetime
from tokens.models import Token


def add_token(model, data):
    print(data)

    exp_date = data.get("token-enabled_to")
    if exp_date:
        exp_date = datetime.strptime(exp_date, "%m/%d/%Y %I:%M %p")
        exp_date = timezone.make_aware(exp_date)

    exp_count = int(data.get("token-enabled_count", 0))

    new_token = Token(
        token=get_random_string(length=32),
        enabled_count=exp_count,
        enabled_to=exp_date,
    )
    new_token.save()
    model.token.add(new_token)
    return new_token
