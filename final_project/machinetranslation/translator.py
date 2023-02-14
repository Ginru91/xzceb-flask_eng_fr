"""
Language translator with use of IMB Cloud Watson language translator
"""

import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()
"""
Assign main parammeters for IBM Watson Language Translator
"""
apikey = os.environ['apikey']
url = os.environ['url']
version = os.environ['version']
languages = os.environ['languages']

language_model = [] # list translation language models
for i in languages.split(', '):
    language_model.append(i)


authenticator = IAMAuthenticator(apikey) #Authenticate to IBM Watson language translator
language_translator = LanguageTranslatorV3(
    version = version,
    authenticator = authenticator
)

language_translator.set_service_url(url)

# Input text values for translation
# Need to test traslation fuctions
en_text = input('Enter english text: ') 
fr_text = input('Enter french text: ')

if language_model.count('en-fr') == True: # Check for existance of language model English to French
    def tranlate_en_to_fr(en_text): #Translation from english to french
        
        language_model_en_to_fr = language_model[language_model.index('en-fr')]
        translate_to_french = language_translator.translate(
            text = en_text, 
            model_id = language_model_en_to_fr).get_result()
        translated_text = translate_to_french['translations'][0]['translation']
        translated_word_count = translate_to_french['word_count']
        return translated_text, translated_word_count

if language_model.count('fr-en') == True: # Check for existance of language model French to English
    def translate_fr_to_en(fr_text): #Translation from french to english
        language_model_fr_to_en = language_model[language_model.index('fr-en')]
        translate_to_english = language_translator.translate(
            text = fr_text,
            model_id = language_model_fr_to_en).get_result()
        translated_text = translate_to_english['translations'][0]['translation']
        translated_word_count = translate_to_english['word_count']
        return translated_text, translated_word_count

try: # Print French text if no errors occured
    fr_translated_text = tranlate_en_to_fr(en_text)
except NameError:
    print('Currently translation from English to French not availible, try again later')
except:
    print('Something went wrong')
else:
    print('French: ', fr_translated_text[0], '\nWords: ', fr_translated_text[1])

try: # Print English text if no errors occured
    en_translated_text = translate_fr_to_en(fr_text)
except NameError:
    print('Currently translation from French to English not availible, try again later')
except:
    print('Something went wrong')
else:
    print('English: ', en_translated_text[0], '\nWords: ', en_translated_text[1])
