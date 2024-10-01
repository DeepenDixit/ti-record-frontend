class TIAutpmationException(Exception):
    """Custom exception class for TI Automation"""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
