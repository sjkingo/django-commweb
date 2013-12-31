from django.conf import settings
import requests
import urlparse

from commweb.exc import *
from commweb.response import CommwebResponse

class Purchase(object):
    VPC_ENDPOINT = 'https://migs.mastercard.com.au/vpcdps'
    VPC_VERSION = 1
    VPC_COMMAND = 'pay'

    attempt = 1 #: number of payment requests sent for this transaction
    _last_resp = None #: the last CommwebResponse object, or None

    def __init__(self, amount, order_info, card_num, card_exp_year, card_exp_month, card_csc):
        self.str_amount = str(amount).replace('.', '')
        self.order_info = str(order_info)
        self.card_num = str(card_num).strip(' ')
        self.card_exp_year = str(card_exp_year)
        self.card_exp_month = str(card_exp_month)
        self.card_csc = str(card_csc)

    @property
    def txn_ref(self):
        return '%s/%d' % (self.order_info, self.attempt)

    def process(self):
        d = {'vpc_Version': self.VPC_VERSION,
             'vpc_Command': self.VPC_COMMAND,
             'vpc_Merchant': settings.COMMWEB_MERCHANT,
             'vpc_AccessCode': settings.COMMWEB_ACCESS_CODE,
             'vpc_MerchTxnRef': self.txn_ref,
             'vpc_OrderInfo': self.order_info,
             'vpc_Amount': self.str_amount,
             'vpc_CardNum': self.card_num,
             'vpc_CardExp': '%s%s' % (self.card_exp_year, self.card_exp_month),
             'vpc_CardSecurityCode': self.card_csc,
        }

        r = requests.post(self.VPC_ENDPOINT, data=d)
        self._last_resp = CommwebResponse(**urlparse.parse_qs(r.text))
        self.attempt += 1

        if self._last_resp.vpc_Merchant != settings.COMMWEB_MERCHANT:
            raise InvalidResponseError('Merchant IDs do not match')
        
        if self._last_resp.approved:
            return (self._last_resp.vpc_Message, self._last_resp.vpc_ReceiptNo)
        else:
            raise PaymentDeclinedError(self._last_resp)
