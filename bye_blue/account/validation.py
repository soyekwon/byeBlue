import re
from django.utils.translation import ugettext_lazy as _

def validate_email(value):
    email_reg = r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
    regex = re.compile(email_reg)

    if not regex.match(value):
        return "false_email"

def validate_password(password):
    if len(password) <= 6:
        return "false_pw"