from parser import parser, process_parser
from input_data import get_data_default

from process import process
def main():
    resulted_arg = process_parser()
    if resulted_arg[0] is None:
        return
    filepath_in, filepath_out, topamount, lang = resulted_arg[0], resulted_arg[1], resulted_arg[2], resulted_arg[3]
    #proccessing:
    data = get_data_default(filepath_in, lang)
    sorted_freq_dict, word_index = data[0], data[1]
    process(filepath_out, sorted_freq_dict, topamount, word_index)

if __name__ == '__main__':
    main()
