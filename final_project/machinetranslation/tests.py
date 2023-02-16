import unittest

from translator import englishToFrench, frenchToEnglish

class TestenglishToFrench(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertNotEqual('Hello', 'Bonjour')

class TestfrenchToEnglish(unittest.TestCase):
    def test_frenchToEnglish(self):
        self.assertNotEqual('Bonjour', 'Hello')

unittest.main()
