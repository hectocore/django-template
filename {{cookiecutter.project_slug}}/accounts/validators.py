from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class NotEmailUsernameValidator(validators.EmailValidator):
    """
    Makes sure the username is not an email.
    This avoids conflict between username and email values.
    """
    message = _('The username can\'t be an email address.')
    code = 'invalid'

    def __call__(self, value):
        try:
            super(NotEmailUsernameValidator, self).__call__(value)
        except ValidationError:
            return
        raise ValidationError(self.message, code=self.code)
