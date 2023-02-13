import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = os.environ['version']1

authenticator = IAMAuthenticator('{apikey}')
language_translator = LanguageTranslatorV3(
    version = '{version}',
    authenticator = authenticator
)

language_translator.set_service_url('{url}')