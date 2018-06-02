class UnsolvableConfigurationError(Exception):
    """Exception raised for errors in the input state.

    Attributes:
        expression -- input state that can't be solved
        message -- explanation of the error

    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
