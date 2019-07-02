from django.contrib.auth.backends import ModelBackend, UserModel
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


class EmailModelBackend(ModelBackend):
    """
    Override of ModelBackend.
    Allows to authenticate using email or username.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        try:
            try:
                validate_email(username)
            except ValidationError:
                user = UserModel._default_manager.get_by_natural_key(username)
            else:
                user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
