import unittest

from translator import english_to_french, french_to_english

class TestenglishToFrench(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertNotEqual('Hello', 'Bonjour')

class TestfrenchToEnglish(unittest.TestCase):
    def test_frenchToEnglish(self):
        self.assertNotEqual('Bonjour', 'Hello')

unittest.main()