
class InputError(Exception):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input given by the user
        message -- explanation of the error

    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
