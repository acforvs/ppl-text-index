from os import path
from strings import NO_SUCH_FILE, OUTPUT_MESS

def print_data(sorted_dict, topamount):
    res = []
    if topamount is None:
            for word_and_count in sorted_dict:
                res.append(OUTPUT_MESS.format(word_and_count[0], word_and_count[1]))
    else:
        cnt_printed = 0
        for word_and_count in sorted_dict:
            if cnt_printed == topamount:
                return
            res.append(OUTPUT_MESS.format(word_and_count[0], word_and_count[1]))
            cnt_printed += 1
    return res

def process(filepath_out, sorted_dict, topamount):
    if filepath_out is None:
        res = print_data(sorted_dict, topamount)
        for line in res:
            print(line)
    else:
        try: 
            with open(filepath_out, 'w') as f:
                res = print_data(sorted_dict, topamount)
                for line in res:
                    f.write(line + '\n')
        except Exception as e:
            print(e)
