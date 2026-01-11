import colorama
from colorama import Fore


def handle_exception(format_func, E: Exception):
    print(f'{format_func(E.__str__())}')


class TimeLimitExceededException(Exception):
    """Called when the program exceeded the configured time limit"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class RuntimeErrorException(Exception):
    """Called when the program caught a runtime error or have not returned the code 0"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class MemoryLimitExceededException(Exception):
    """Called when the program exceeded the configured time limit"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class RequestTimeoutException(Exception):
    """Called when the request exceeded the configured time limit"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class RequestConnectionErrorException(Exception):
    """Called when user lost connection during(before) the request"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class InternalAPIErrorException(Exception):
    """Called when CF API is experiencing some issues"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class HandleNotSetException(Exception):
    """Called when user has called a method that requires the handle, but the handle was not set"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class UndefinedAPIErrorException(Exception):
    """Called when something unexpected happened during the request"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class ConfigAttributeNotFoundException(Exception):
    """Called when user tries to modify a non-existing attribute"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class WrongAttributeTypeException(Exception):
    """Called when user tries to modify an attribute, but the new value's type is incorrect"""

    def __init__(self, *args: object):
        super().__init__(*args)


class FileNotFoundException(Exception):
    """Called when the program cannot find the file that the user tries to access"""

    def __init__(self, *args: object):
        super().__init__(*args)


class OutputFileTooLargeException(Exception):
    """Called when the output file size exceeded the set limit"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class ConfigNotFoundException(Exception):
    """Called when user tries to access an undefined config option"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class CannotLeaveEmptyConfigListException(Exception):
    """Called when user tries to delete last config option"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class InvalidAttributeValue(Exception):
    """Called when the new config attribute value is invalid"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)