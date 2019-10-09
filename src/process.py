from os import path
from strings import NO_SUCH_FILE, OUTPUT_MESS, SEPARATOR, PAGE_DESCR

def data_to_output(sorted_dict, topamount, word_index):
    '''
    data -> output form
    '''
    res = []
    if topamount is None:
        for word_and_count in sorted_dict:
            word, count = word_and_count[0], word_and_count[1]
            index = word_index[word]
            pages = []
            for key, value in index.items():
                pages.append(PAGE_DESCR.format(key, value))
            res.append([OUTPUT_MESS.format(word, count), pages])
    else:
        cnt_printed = 0
        for word_and_count in sorted_dict:
            if cnt_printed == topamount:
                return res
            word, count = word_and_count[0], word_and_count[1]
            index = word_index[word]
            pages = []
            for key, value in index.items():
                pages.append(PAGE_DESCR.format(key, index[key]))
            res.append([OUTPUT_MESS.format(word, count), pages])
            cnt_printed += 1
    return res

def process(filepath_out, sorted_dict, topamount, word_index):
    '''
    console or file output
    '''
    if filepath_out is None:
        res = data_to_output(sorted_dict, topamount, word_index)
        for line in res:
            print(line[0])
            for page_info in line[1]:
                print(page_info)
            print(SEPARATOR)
    else:

            with open(filepath_out, 'w') as f:
                res = data_to_output(sorted_dict, topamount, word_index)
                for line in res:
                    f.write(line[0] + '\n')
                    for page_info in line[1]:
                        f.write(page_info)
                    f.write(SEPARATOR + '\n')
       
