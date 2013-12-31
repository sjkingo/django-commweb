==============
django-commweb
==============

Django module for interfacing with the CommWeb merchant gateway.

Supported functions
-------------------

* Purchase (one-step transaction)

Installation
------------

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

django-commweb can be intergrated directly as a Cartridge payment processor through the ``commweb.cartridge`` module, or by
accessing the API directly through ``commweb.purchase``.

Cartridge
~~~~~~~~~

Using the API directly
~~~~~~~~~~~~~~~~~~~~~~

See ``commweb.test.test_responses.py`` for an example of how to call the API directly.