import requests
import urlparse

from commweb import settings
from commweb.exc import PaymentDeclinedError
from commweb.response import CommwebResponse

class TransactionPayment(object):
    VPC_COMMAND = 'pay'

    attempt = 1 #: number of payment requests sent for this transaction

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
        d = {'vpc_Version': settings.COMMWEB_VPC_VERSION,
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

        r = requests.post(settings.COMMWEB_VPC_ENDPOINT, data=d)
        resp = CommwebResponse(**urlparse.parse_qs(r.text))
        self.attempt += 1
        
        if resp.approved:
            return (resp.vpc_Message, resp.vpc_ReceiptNo)
        else:
            raise PaymentDeclinedError(resp)
