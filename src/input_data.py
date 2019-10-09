from os import path
import re
from normalizer import normalize
from strings import WENT_WRONG, NO_SUCH_FILE, rus_pattern, eng_pattern, gen_pattern

LINES_IN_PAGE = 45
def create_pattern(lang):
    '''
    creating a pattern for language
    '''
    if lang == 'r':
            pattern = re.compile(rus_pattern, re.IGNORECASE)
    if lang == 'e':
            pattern = re.compile(eng_pattern, re.IGNORECASE)
    if lang is None:
            pattern = re.compile(gen_pattern, re.IGNORECASE)
    return pattern

def get_data_default(filepath, lang):
    '''
    getting the text from the default file
    '''
    if not path.exists(filepath):
        print(NO_SUCH_FILE)
        return
    freq, word2page_num = dict(), dict() #{frequence : word}, {word : list_of_pages}
    #setting the pattern:
    pattern = create_pattern(lang)
    lines_processed = 0

    with open(filepath, 'r') as input_file:
        lines = input_file.read().splitlines()
        for line in lines:
            #page number calculating
            lines_processed += 1
            page_num = lines_processed // (LINES_IN_PAGE + 1) + 1
            #processing words
            words = pattern.findall(line)
            for word in words:
                if lang is None:
                    if word[0] != '':
                        word = word[0]
                    else:
                        word = word[1]
                word = normalize(word)
                #updating frequence
                if word in freq:
                    freq[word] += 1
                else:
                    freq[word] = 1
                #updating page number list
                if word in word2page_num:
                    if page_num in word2page_num[word]:
                        word2page_num[word][page_num] += 1
                    else:
                        word2page_num[word][page_num] = 1
                else:
                    word2page_num[word] = dict()
                    word2page_num[word] = {page_num : 1}
    sorted_dict = sorted(freq.items(), key=lambda el : el[1], reverse=True)
    return sorted_dict, word2page_num


