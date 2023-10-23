from rest_framework.exceptions import APIException


class UserNotFoundException(APIException):
    status_code = 404
    default_detail = 'User bot found'
    default_code = 'user_not_found'
