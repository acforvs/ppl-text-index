import pymorphy2
morph = pymorphy2.MorphAnalyzer()


def normalize(word):
    '''
    word to the normal form
    '''
    parsed_word = morph.parse(word)[0]
    return parsed_word.normal_form
