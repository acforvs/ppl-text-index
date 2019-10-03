from os import path
import re
from normalizer import normalize
from strings import WENT_WRONG, NO_SUCH_FILE, rus_pattern, eng_pattern

def get_data_default(filepath, lang):
    '''
    getting the text from the default file
    '''
    try:
        if not path.exists(filepath):
            print(NO_SUCH_FILE)
            return
        freq = dict() #dict {frequence : word}
        if lang == 'rus':
            pattern = re.compile(rus_pattern, re.IGNORECASE)
        if lang == 'eng':
            pattern = re.compile(eng_pattern, re.IGNORECASE)
        with open(filepath, 'r') as input_file:
            lines = [line.strip() for line in input_file]
            for line in lines:
                words = pattern.findall(line)
                for word in words:
                    word = normalize(word)
                    if word in freq:
                        freq[word] += 1
                    else:
                        freq[word] = 1
        sorted_dict = sorted(freq.items(), key=lambda el : el[1], reverse=True)
        return sorted_dict

    except:
        print(WENT_WRONG)
