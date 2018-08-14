import datetime
import string
import random
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from ..user_profile.models import UserProfile
from ..email.models import Codes, Email

User = get_user_model()


class UserRegisterView(APIView):
    """
    This API endpoint handles the registration of a new user.
    """
    permission_classes = []

    def post(self, request, **kwargs):
        data = request.POST
        email = data.get('email')
        code = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(6))
        validation_code = Codes.objects.create(code=code, email=email)
        validation_code.save()

        Email.objects.create(
            to=email,
            subject='Welcome to Family-fun',
            content=f'Your account registration has been successful. Please click the link to activate your account.\n\
             Visit /api/registration/validation/?token={code}'
        )
        return Response(f"A validation email has been sent to {email}")


class UserValidationView(APIView):
    """
    This API endpoint handles the validation of a new user.
    """
    permission_classes = []

    def post(self, request, **kwargs):
        data = request.data
        token = data.get('token')
        username = data.get('username')
        password = data.get('password')

        code = Codes.objects.get(code=token)

        user = User.objects.create(username=username, email=code.email)
        user.set_password(password)
        user.save()

        code.user = user
        code.save()

        user_profile = UserProfile.objects.create(user=user, joined_date=datetime.datetime.now())
        user_profile.save()

        return Response(f"Welcome to Family-fan {user.username}. Your account has been activated.")


class PasswordResetView(APIView):
    """
    This API endpoint handles the password reset.
    """
    permission_classes = []

    def post(self, request):
        data = request.POST
        username = data.get('username')

        code = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(6))
        user = User.objects.get(username=username)

        validation_code = Codes.objects.create(code=code, user=user, email=user.email)
        validation_code.save()

        Email.objects.create(
            to=user.email,
            subject='Family-fun - Password Reset',
            content=f'Remembering passwords is for losers. Here you go with a new validation link.\n\
                    validation code: {code}'
        )
        return Response(f"We have sent a password reset token to your email!")


class PasswordResetValidateView(APIView):
    """
    This API endpoint handles the password reset validation.
    """
    permission_classes = []

    def post(self, request, **kwargs):
        data = request.POST
        code = data.get('code')
        password = data.get('password')

        user = Codes.objects.get(code=code).user
        user.set_password(password)
        user.save()
        return Response(f"Your new password has been set.")
