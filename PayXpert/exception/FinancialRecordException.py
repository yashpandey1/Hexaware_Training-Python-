class FinancialRecordException(Exception):
    def __init__(self, message = "FinancialRecordException"):
        self.message = message
        super().__init__(self.message)