
class CommwebResponse(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v[0])

    def __str__(self):
        return '%s (code %d)' % (self.vpc_Message, self.response_code)

    @property
    def response_code(self):
        return int(self.vpc_TxnResponseCode)

    @property
    def approved(self):
        return self.response_code == 0

    def pprint(self):
        from pprint import pprint
        pprint(self.__dict__)

