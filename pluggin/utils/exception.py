class InvalidResponseError(Exception):
    """Custom exception for invalid JSON 'response' values."""

    def __init__(self, message="The response field indicates a failure."):
        super().__init__(message)
