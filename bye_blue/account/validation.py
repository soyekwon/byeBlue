import re

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validate_email(value):
    email_reg = r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
    regex = re.compile(email_reg)

    if not regex.match(value):
        raise ValidationError("이메일형식이 옳바르지 않습니다")

def validate_password(password):
    if len(password) <= 1:
        raise ValidationError("비밀번호는 ?자리를 넘겨야합니다")