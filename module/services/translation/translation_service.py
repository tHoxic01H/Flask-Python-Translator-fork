# import translators as ts
from googletrans import Translator

def translate_from_google(phrase, from_language, to_language):
    # return ts.google(phrase, from_language, to_language)
    translator = Translator()
    translation = translator.translate(phrase, dest=to_language)
    return translation.text