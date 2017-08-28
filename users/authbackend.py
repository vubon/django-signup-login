from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class EmailCheck(object):

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user
            else:
                return None
        except User.DoesNotExist:
            raise ValidationError("Invalid username or password")

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
