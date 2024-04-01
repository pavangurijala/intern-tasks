__author__ = 'k0emt'

import unittest
from Experiment import Greeter

class MyTestCase(unittest.TestCase):
    def test_default_greeting_set(self):
        greeter = Greeter()
        # this test will fail until you change the Greeter to return this expected message
        self.assertEqual(greeter.message, 'Hello world!')

if __name__ == '__main__':
    unittest.main()
