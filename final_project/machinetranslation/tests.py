import unittest

from translator import englishToFrench, frenchToEnglish

class TestenglishToFrench(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertNotEqual(englishToFrench('Hello'), 'Hello')
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

class TestfrenchToEnglish(unittest.TestCase):
    def test_frenchToEnglish(self):
        self.assertNotEqual(frenchToEnglish('Bonjour'), 'Bonjour')
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

unittest.main()
