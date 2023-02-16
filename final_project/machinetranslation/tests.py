import unittest

from translator import englishToFrench, frenchToEnglish

class TestenglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(englishToFrench("Hello"), "Hello")
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

class TestfrenchToEnglish(unittest.TestCase):
    def test2(self):
        self.assertNotEqual(frenchToEnglish("Bonjour"), "Bonjour")
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

unittest.main()
