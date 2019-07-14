from django.core.exceptions import ValidationError

def actor_name_simple(value):
    if (len(value) <= 5):
        raise ValidationError("Sorry, Name is short")
    return value
