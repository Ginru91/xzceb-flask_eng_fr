import unittest

class TranslationTest(unittest.TestCase):

    def frenchToEnglish(self):
        self.assertEqual('Bonjour', 'Hello')

    def englishToFrench(self):
        self.assertEqual('Hello', 'Bonjour')

if __name__ == "__main__":
    unittest.main()