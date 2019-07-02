from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from .validators import NotEmailUsernameValidator


# Create your models here.
class User(AbstractUser):
    """
    Override of the Django default User.
    Custom User model with unique email address, allowing for both username and email authentication.
    Also applies a custom validator to the username in order for it not to conflict with the emails.
    """

    username_validator = UnicodeUsernameValidator()
    username_email_validator = NotEmailUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator, username_email_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(
        _('email address'),
        blank=False,
        unique=True,
        error_messages={
            'unique': _("A user with that email address already exists."),
        },
    )
