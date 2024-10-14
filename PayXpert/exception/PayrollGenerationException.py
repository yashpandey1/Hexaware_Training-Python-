class PayrollGenerationException(Exception):
    def __init__(self, message = "PayrollGenerationException"):
        self.message = message
        super().__init__(self.message)
