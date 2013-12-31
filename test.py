#!/usr/bin/env python

import unittest
from commweb.test.test_responses import TestResponses
suite = unittest.TestLoader().loadTestsFromTestCase(TestResponses)
unittest.TextTestRunner(verbosity=2).run(suite)
