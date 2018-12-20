"""Component that is responsible for handing Language related logic"""

from langdetect import detect
from google.cloud import translate

class Language:
    translate_client = translate.Client()

    @staticmethod
    def detect_language(text):
       return detect(text)

    @classmethod
    def translate_text(cls, text, source_language=None, target_language='en'):
        return cls.translate_client.translate(
            text, 
            target_language=target_language,
            source_language=source_language
        )
