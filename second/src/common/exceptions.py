class DrawingException(Exception):
    """Actually, exception is not needed here but let's imagine that something could go wrong"""

    def __init__(self, message: str = "Galaxy is in danger!1"):
        self.message = message
