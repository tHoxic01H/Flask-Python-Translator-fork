from multiprocessing.dummy import Array
import re
from module.services.translation.translation_service import translate_from_google
from module.models.translation.TranslationModelV1 import TranslationModelV1
from module.models.translation.TranslationModelV2 import TranslationModelV2
from module.services.utils.utils import set_first_letter_upper_and_remove_spaces

# V2
def translate_v2(translation_body_v2: TranslationModelV2):
    # The texts to translate
    texts = translation_body_v2.texts

    # The base language (ex: en, fr, es)
    from_lang = translation_body_v2.from_language

    # The language to translate the texts to (ex: en, fr, es)
    to_lang = translation_body_v2.to_language

    # Function to insert every strings in an object into an array
    def insert_strings_to_text_arr(texts_dict,tab):
        for attr in texts_dict:
            field = texts_dict[attr]
            if(type(field) is str):
                tab.append(field.replace("||",""))
            elif(type(field) is dict):
                insert_strings_to_text_arr(field,tab)
        return 1
        
    # Function to replace all texts of an object into strings passed to the tab
    def insert_translated_texts(texts_dict,tab, index):
        for attr in texts_dict:
            if(type(texts_dict[attr]) is str):
                texts_dict[attr] = set_first_letter_upper_and_remove_spaces(tab[index])
                index+=1
            elif(type(texts_dict[attr] is dict)):
                insert_translated_texts(texts_dict[attr], tab, index)
        return 1
    # An array that will contain the values of the texts to translate
    arr_to_translate = []
    insert_strings_to_text_arr(texts,arr_to_translate)
    # Contains the texts combined in one text separated with a separator |||
    text_concatened = " || ".join(arr_to_translate) + " || "
    # Translate the text
    translated_text = translate_from_google(text_concatened, from_language=from_lang, to_language=to_lang)
    # Replacing unexpected behaviours like | | or ||| and much more
    pattern = re.compile(r'\|(\W+)\|')
    translated_text = re.sub(pattern,'||',translated_text)
    # An array with the translated_text splited with ||
    translated_arr = translated_text.split("||")
    insert_translated_texts(texts, translated_arr, 0)
    # Payload of the response
    res = {
        "from_language": from_lang,
        "to_language":to_lang,
        "translated": texts,
    }
    return res

# V2
def translate_v2_0(translation_body_v2: TranslationModelV2):
    # The texts to translate
    texts = translation_body_v2.texts

    # The base language (ex: en, fr, es)
    from_lang = translation_body_v2.from_language

    # The language to translate the texts to (ex: en, fr, es)
    to_lang = translation_body_v2.to_language
    # Just return if it's the same language
    if(from_lang == to_lang):
        res = {
            "from_language": from_lang,
            "to_language":to_lang,
            "translated": texts
        }
        return res
    # An array that will contain the values of the texts
    text_arr = []
    for attr in texts:
        text_arr.append(str(texts[attr]).replace('||',''))
    # Contains the texts combined in one text separated with a separator |||
    text_concatened = " || ".join(text_arr) + " || "

    # Translate the text
    translated_text = translate_from_google(text_concatened, from_language=from_lang, to_language=to_lang)
    # Replacing unexpected behaviours like | | or ||| and much more
    pattern = re.compile(r'\|(\W+)\|')
    translated_text = re.sub(pattern,'||',translated_text)
    # An array with the translated_text splited with ||
    translated_arr = translated_text.split("||")
    # Change the fields values to become the translated ones
    i = 0
    for attr in texts:
        try:
            texts[attr] = set_first_letter_upper_and_remove_spaces(translated_arr[i])
        except:
            print('y')
        i += 1

    # Payload of the response
    res = {
        "from_language": from_lang,
        "to_language":to_lang,
        "translated": texts,
    }
    return res

# V1
def translate_v1(translation_body_v1: TranslationModelV1):
    fromLang = "auto"
    text = translation_body_v1.text
    to_lang = translation_body_v1.to_language
    res = {
        "from_language": fromLang,
        "to_language": to_lang,
        "translated": translate_from_google(text, from_language=fromLang, to_language=to_lang)
    }
    return res