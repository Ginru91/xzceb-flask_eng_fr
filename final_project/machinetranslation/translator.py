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

languageModel = [] # list translation language models
for i in languages.split(', '):
    languageModel.append(i)


authenticator = IAMAuthenticator(apikey) #Authenticate to IBM Watson language translator
language_translator = LanguageTranslatorV3(
    version = version,
    authenticator = authenticator
)

language_translator.set_service_url(url)

# Input text values for translation
# Need to test traslation fuctions
enText = input('Enter english text: ') 
frText = input('Enter french text: ')

if languageModel.count('en-fr') == True: # Check if language model English to French exist
    def englishToFrench(englishText): #Translation from english to french
        languageModelToFrench = languageModel[languageModel.index('en-fr')]
        translateToFrench = language_translator.translate(
            text = englishText, 
            model_id = languageModelToFrench).get_result()
        frenchText = translateToFrench['translations'][0]['translation']
        #frenchTextWordCount = translateToFrench['word_count']
        return frenchText

if languageModel.count('fr-en') == True: # Check if language model French to English exist
    def frenchToEnglish(frenchText): #Translation from french to english
        languageModelToEnglish = languageModel[languageModel.index('fr-en')]
        translateToEnglish = language_translator.translate(
            text = frenchText,
            model_id = languageModelToEnglish).get_result()
        englishText = translateToEnglish['translations'][0]['translation']
        #englishTextCount = translate_to_english['word_count']
        return englishText

try: # Print French text if no errors occured
    frTranslatedText = englishToFrench(enText)
except NameError:
    print('Currently translation from English to French not availible, try again later')
except:
    print('Something went wrong')
else:
    print('French: ', frTranslatedText[0], '\nWords: ', frTranslatedText[1])

try: # Print English text if no errors occured
    enTranslatedText = frenchToEnglish(frText)
except NameError:
    print('Currently translation from French to English not availible, try again later')
except:
    print('Something went wrong')
else:
    print('English: ', enTranslatedText[0], '\nWords: ', enTranslatedText[1])
