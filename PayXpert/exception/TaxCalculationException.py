class TaxCalculationException(Exception):
    def __init__(self, message = "TaxCalculationException"):
        self.message = message
        super().__init__(self.message)