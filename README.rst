==============
django-commweb
==============

django-commweb is a Django module for interfacing with the CommWeb_ merchant gateway, the Commonwealth Bank of Australia's merchant payment facility.

Source is available on GitHub_, as is the Changelog_.

.. _CommWeb: https://www.commbank.com.au/business/merchant-services/accept-online-payments/commweb.html
.. _GitHub: https://github.com/sjkingo/django-commweb
.. _Changelog: https://github.com/sjkingo/django-commweb/blob/master/CHANGELOG.md

Supported functions
-------------------

* Purchase (one-step transaction)

Dependencies
------------

* Python 2.7 or 3.4+
* Django_ (tested with 1.5 through 1.8)
* requests_

.. _Django: https://www.djangoproject.com/
.. _requests: http://docs.python-requests.org/en/latest/

Installation
------------

0. Install using pip::

    $ pip install django-commweb

1. Add the 'commweb' app to the bottom of your INSTALLED_APPS setting::
    
    INSTALLED_APPS = (
        ...
        'commweb',
    )

2. Add the required settings (provided by the CommWeb Support Line) for the **test** merchant to your project's ``settings.py``::

    COMMWEB_ACCESS_CODE = 'FOO'
    COMMWEB_MERCHANT = 'TESTMERCHANT'

3. Run the tests to ensure your merchant details are set up correctly by running a Django shell as follows::

    $ python manage.py shell
    >>> import unittest
    >>> from commweb.test.test_responses import TestResponses
    >>> suite = unittest.TestLoader().loadTestsFromTestCase(TestResponses)
    >>> unittest.TextTestRunner(verbosity=2).run(suite)
    test_approved (commweb.test.test_responses.TestResponses) ... ok
    test_card_expired (commweb.test.test_responses.TestResponses) ... ok
    test_declined_2 (commweb.test.test_responses.TestResponses) ... ok
    test_declined_E (commweb.test.test_responses.TestResponses) ... ok
    test_failed (commweb.test.test_responses.TestResponses) ... ok
    test_insufficient_credit (commweb.test.test_responses.TestResponses) ... ok
    test_no_reply (commweb.test.test_responses.TestResponses) ... ok

    ----------------------------------------------------------------------
    Ran 7 tests in 2.593s

    OK
    <unittest.runner.TextTestResult run=7 errors=0 failures=0>

Intergration
------------

Two options are available for intergrating django-commweb into your Django app.

Cartridge
~~~~~~~~~

A payment handler for Cartridge_ is provided by ``commweb.cartridge.cartridge_payment_handler``. You only need to set ``SHOP_HANDLER_PAYMENT`` in your project's settings file to activate this functionality::

     SHOP_HANDLER_PAYMENT = 'commweb.cartridge_hook.cartridge_payment_handler'

.. _Cartridge: http://cartridge.jupo.org/overview.html

Using the API directly
~~~~~~~~~~~~~~~~~~~~~~

See ``commweb.test.test_responses.py`` for an example of how to call the API directly. The API module is located at ``commweb.purchase``.
