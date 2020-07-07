from .base import MyError


class BadRequestException(MyError):
    def __init__(self, message):
        super().__init__(message)


class UserAlreadyExistException(MyError):
    def __init__(self, message):
        super().__init__(message)


class UserNotExistException(MyError):
    def __init__(self, message):
        super().__init__(message)


class DatabaseException(MyError):
    def __init__(self, message):
        super().__init__(message)
