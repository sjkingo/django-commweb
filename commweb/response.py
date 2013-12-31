
class CommwebResponse(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v[0])

    def __str__(self):
        return '%s (code %d)' % (self.vpc_Message, self.response_code)

    @property
    def response_code(self):
        # This can either be an int or a str.. thanks CBA
        try:
            return int(self.vpc_TxnResponseCode)
        except ValueError:
            return self.vpc_TxnResponseCode

    @property
    def approved(self):
        return self.response_code == 0

    def pprint(self):
        from pprint import pprint
        pprint(self.__dict__)

class ResponseCode(object):
    APPROVED = 0
    UNSPECIFIED_FAILURE = 1
    DECLINED_E = 'E'
    DECLINED_2 = 2
    NO_REPLY = 3
    CARD_EXPIRED = 4
    INSUFFICIENT_CREDIT = 5
    MESSAGE_DETAIL_ERROR = 7 # invalid values sent
