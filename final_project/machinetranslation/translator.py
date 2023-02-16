"""
Language translator with use of IMB Cloud Watson language translator
"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']
VERSION = os.environ['version']
LANGUAGES = os.environ['languages']

LANGUAGESMODEL = [] # list translation language models
for i in LANGUAGES.split(', '):
    LANGUAGESMODEL.append(i)

AUTHENTICATOR = IAMAuthenticator(APIKEY) #Authenticate to IBM Watson language translator
LANGUAGE_TRANSLATOR = LanguageTranslatorV3(
    version=VERSION,
    authenticator=AUTHENTICATOR
)

LANGUAGE_TRANSLATOR.set_service_url(URL)

if LANGUAGESMODEL.count('en-fr') == 1: # Check if language model English to French exist
    def englishToFrench(englishText):
        """
        Translation from english to french
        """
        language_model_to_french = LANGUAGESMODEL[LANGUAGESMODEL.index('en-fr')]
        translate_to_french = LANGUAGE_TRANSLATOR.translate(
            text=englishText,
            model_id=language_model_to_french).get_result()
        frenchText = translate_to_french['translations'][0]['translation']
        #frenchTextWordCount = translateToFrench['word_count']
        return frenchText

if LANGUAGESMODEL.count('fr-en') == 1: # Check if language model French to English exist
    def frenchToEnglish(frenchText):
        """
        Translation from french to english
        """
        language_model_to_english = LANGUAGESMODEL[LANGUAGESMODEL.index('fr-en')]
        translate_to_english = LANGUAGE_TRANSLATOR.translate(
            text=frenchText,
            model_id=language_model_to_english).get_result()
        englishText = translate_to_english['translations'][0]['translation']
        #englishTextCount = translate_to_english['word_count']
        return englishText

# try: # Print French text if no errors occured
#     FRTRANSLATEDTEXT = english_to_french(english_text)
# except NameError:
#     print('Currently translation from English to French not availible, try again later')
# else:
#     print('French: ', FRTRANSLATEDTEXT[0], '\nWords: ', FRTRANSLATEDTEXT[1])

# try: # Print English text if no errors occured
#     ENTRANSLATEDTEXT = french_to_english()
# except NameError:
#     print('Currently translation from French to English not availible, try again later')
# else:
#     print('English: ', ENTRANSLATEDTEXT[0], '\nWords: ', ENTRANSLATEDTEXT[1])
