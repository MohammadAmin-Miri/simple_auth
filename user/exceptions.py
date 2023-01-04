from rest_framework.exceptions import APIException


class PhoneOrEmailNotEntered(APIException):
    status_code = 400
    default_detail = 'An email or a phone number must be entered.'
    default_code = 'invalid_data'


class VerificationCodeExpiredOrInvalid(APIException):
    status_code = 400
    default_detail = 'The verification code entered has expired or the phone number is invalid.'
    default_code = 'invalid_verification_code'


class VerificationCodeInvalid(APIException):
    status_code = 400
    default_detail = 'The verification code entered is invalid.'
    default_code = 'invalid_verification_code'
