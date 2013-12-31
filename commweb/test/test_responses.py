from decimal import Decimal
import unittest

from commweb.exc import PaymentDeclinedError
from commweb.purchase import Purchase
from commweb.response import ResponseCode

class TestResponses(unittest.TestCase):
    # Test data for card: ('card_num', 'expiry_yy', 'expiry_mm', 'csc')
    TEST_CARD_DATA = ('5123456789012346', '17', '05', '121')

    def purchase(self, amount, order_info):
        p = Purchase(amount=amount, order_info=order_info,
                card_num=self.TEST_CARD_DATA[0], card_exp_year=self.TEST_CARD_DATA[1],
                card_exp_month=self.TEST_CARD_DATA[2], card_csc=self.TEST_CARD_DATA[3])
        return p

    def test_approved(self):
        t = self.purchase(Decimal('1.00'), 'test_approved')
        r = t.process()
        self.assertTrue(t._last_resp.approved)
        self.assertEquals(t._last_resp.response_code, ResponseCode.APPROVED)
        self.assertEquals(r[0], 'Approved')
        self.assertIsNotNone(r[1])
        self.assertNotEqual(r[1], '')

    def test_failed(self):
        t = self.purchase(Decimal('1.10'), 'test_failed')
        try:
            r = t.process()
        except PaymentDeclinedError, e:
            self.assertEquals(e.response.response_code, ResponseCode.UNSPECIFIED_FAILURE)
        else:
            self.fail(msg='PaymentDeclinedError should have been raised')

    def test_declined_E(self):
        t = self.purchase(Decimal('1.01'), 'test_declined_E')
        try:
            r = t.process()
        except PaymentDeclinedError, e:
            self.assertEquals(e.response.response_code, ResponseCode.DECLINED_E)
        else:
            self.fail(msg='PaymentDeclinedError should have been raised')

    def test_declined_2(self):
        t = self.purchase(Decimal('1.05'), 'test_declined_2')
        try:
            r = t.process()
        except PaymentDeclinedError, e:
            self.assertEquals(e.response.response_code, ResponseCode.DECLINED_2)
        else:
            self.fail(msg='PaymentDeclinedError should have been raised')

    def test_no_reply(self):
        t = self.purchase(Decimal('1.68'), 'test_no_reply')
        try:
            r = t.process()
        except PaymentDeclinedError, e:
            self.assertEquals(e.response.response_code, ResponseCode.NO_REPLY)
        else:
            self.fail(msg='PaymentDeclinedError should have been raised')

    def test_card_expired(self):
        t = self.purchase(Decimal('1.54'), 'test_card_expired')
        try:
            r = t.process()
        except PaymentDeclinedError, e:
            self.assertEquals(e.response.response_code, ResponseCode.CARD_EXPIRED)
        else:
            self.fail(msg='PaymentDeclinedError should have been raised')

    def test_insufficient_credit(self):
        t = self.purchase(Decimal('1.51'), 'test_insufficient_credit')
        try:
            r = t.process()
        except PaymentDeclinedError, e:
            self.assertEquals(e.response.response_code, ResponseCode.INSUFFICIENT_CREDIT)
        else:
            self.fail(msg='PaymentDeclinedError should have been raised')
