#!/usr/bin/env python

from decimal import Decimal

import commweb.payment

p = commweb.payment.TransactionPayment(
    amount=Decimal('1.00'),
    order_info='test1',
    card_num='5123456789012346',
    card_exp_year='17', card_exp_month='05',
    card_csc='121')

print p.process()
