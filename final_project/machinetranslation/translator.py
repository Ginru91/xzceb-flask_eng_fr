"""
Language translator with use of IMB Cloud Watson language translator
"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

# APIKEY = os.environ['apikey']
# URL = os.environ['url']
# VERSION = os.environ['version']
# LANGUAGES = os.environ['languages']

APIKEY = 'z0b60USzr0sR6Svin21m4C6_XvDPOdFn4dWI4wVYUL39'
URL = 'https://api.eu-de.language-translator.watson.cloud.ibm.com/instances/b3e88f57-f1cd-4eaa-9515-bf8aae55a37c'
VERSION = '2018-05-01'
LANGUAGESMODEL = ['en-fr', 'fr-en']

AUTHENTICATOR = IAMAuthenticator(APIKEY) #Authenticate to IBM Watson language translator
LANGUAGE_TRANSLATOR = LanguageTranslatorV3(
    version=VERSION,
    authenticator=AUTHENTICATOR
)

LANGUAGE_TRANSLATOR.set_service_url(URL)

if LANGUAGESMODEL.count('en-fr') == 1: # Check if language model English to French exist
    def english_to_french(english_text):
        """
        Translation from english to french
        """
        language_model_to_french = LANGUAGESMODEL[LANGUAGESMODEL.index('en-fr')]
        translate_to_french = LANGUAGE_TRANSLATOR.translate(
            text=english_text,
            model_id=language_model_to_french).get_result()
        french_text = translate_to_french['translations'][0]['translation']
        #frenchTextWordCount = translateToFrench['word_count']
        return french_text

if LANGUAGESMODEL.count('fr-en') == 1: # Check if language model French to English exist
    def french_to_english(french_text):
        """
        Translation from french to english
        """
        language_model_to_english = LANGUAGESMODEL[LANGUAGESMODEL.index('fr-en')]
        translate_to_english = LANGUAGE_TRANSLATOR.translate(
            text=french_text,
            model_id=language_model_to_english).get_result()
        english_text = translate_to_english['translations'][0]['translation']
        #englishTextCount = translate_to_english['word_count']
        return english_text

