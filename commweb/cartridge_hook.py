from cartridge.shop.checkout import CheckoutError

from commweb.exc import PaymentDeclinedError
from commweb.purchase import Purchase

def cartridge_payment_handler(request, order_form, order):
    trans_id = 'WFS_%d' % order.id

    p = Purchase(order.total, trans_id,
            order_form.cleaned_data['card_number'],
            order_form.cleaned_data['card_expiry_year'][2:4],
            order_form.cleaned_data['card_expiry_month'],
            order_form.cleaned_data['card_ccv'])

    try:
        p.process()
        return trans_id
    except PaymentDeclinedError, e:
        raise CheckoutError('Payment declined: %s' % str(e))
