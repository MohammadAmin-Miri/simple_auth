from rest_framework.exceptions import APIException


class PhoneOrEmailNotEntered(APIException):
    status_code = 400
    default_detail = 'An email or a phone number must be entered.'
    default_code = 'invalid_data'
