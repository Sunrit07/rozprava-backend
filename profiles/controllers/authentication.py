import random

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q

from verification.models import OTPVerification


class Authenticator:

    @staticmethod
    def register(**kwargs):
        first_name = kwargs.get('first_name')
        last_name = f"{kwargs.get('middle_name')} {kwargs.get('last_name')}".strip()
        username = kwargs.get('username')
        password = kwargs.get('password')
        email = kwargs.get('email')
        phone_number = kwargs.get('phone_number')
        user = User.objects.filter(Q(username=username) | Q(email=email))

        if user:
            raise AssertionError('User Already Exists !')

        User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user = authenticate(username=username, password=password)

        user.profile.mobile_number = phone_number
        user.profile.save()

        if not user:
            return None, {'error': 'Username/Password is incorrect.'}
        return user, {}

    @staticmethod
    def initiate_reset_password(email: str):
        user = User.objects.get(email=email)
        if not user:
            raise ValueError(f'No user with email: [{email}]')
        otp = str(random.randint(100000, 999999))
        # Step 1: Check if existing OTP Verification object exists.
        otp_object = OTPVerification.objects.get(
            profile=user.profile,
            verifier_tag=OTPVerification.VerifierTag.PASSWORD_RESET,
            is_verified=False
        )
        if otp_object:
            otp_object.otp = otp
            otp_object.save()
        # Step 2: Create a new OTP Verification object and send mail.
        OTPVerification.objects.create(
            profile=user.profile,
            otp=otp,
            verifier_tag=OTPVerification.VerifierTag.PASSWORD_RESET
        )

    @staticmethod
    def verify_otp(username: str, otp: int) -> bool:
        user = User.objects.get(username=username)
        otp_object = OTPVerification.objects.get(
            profile=user.profile,
            verifier_tag=OTPVerification.VerifierTag.PASSWORD_RESET,
            is_verified=False
        )
        if otp_object.otp == otp:
            otp_object.is_verified = True
            otp_object.save()
            return True

    @staticmethod
    def reset_password(username: str, password: str):
        user = User.objects.get(username=username)
        user.set_password(raw_password=password)
        user.save()
        return True
