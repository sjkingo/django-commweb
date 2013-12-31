
class PaymentDeclinedError(BaseException):
    def __init__(self, response):
        self.response = response

    def __str__(self):
        return str(self.response)

class InvalidResponseError(BaseException):
    pass
