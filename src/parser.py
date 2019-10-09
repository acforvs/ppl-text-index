import argparse
from strings import SPECIFY_PATH, USAGE, DEFAULT_PATH_IN, DEFAULT_PATH_OUT

def parser():
    parser = argparse.ArgumentParser()

    parser.add_argument('-u', '--usage', action='store_true', help='Usage')
    parser.add_argument('-c', '--count', action='store', nargs=1, type=int, help='limit the amount of output words')

    group_input = parser.add_mutually_exclusive_group()
    group_output = parser.add_mutually_exclusive_group()

    group_input.add_argument('-i', '--input', action='store', nargs=1, type=str, help='Setting path to the input data file')
    group_input.add_argument('-io', '--default_input', action='store_true', help='Read from the default file')

    group_output.add_argument('-o', '--output', action='store', nargs=1, type=str, help='Setting path to the output data file')
    group_output.add_argument('-do', '--default_output', action='store_true', help='Result to the default file')
    
    parser.add_argument('-p', '--pattern', action='store', type=str, help='Setting the language')
    res = parser.parse_args()

    return res

def process_parser():
    res = parser()
    topamount, filepath_out, lang = None, None, None
    #arguments handler:
    if not (res.input or res.output or res.default_input or res.default_output or res.usage or res.pattern):
        print(SPECIFY_PATH, '\n')
        print(USAGE)
        return [None]
    if res.usage:
        print(USAGE)
        return [None]
    #setting the filepath_in and filepath_out:
    if res.input:
        filepath_in = res.input[0]
    elif (not res.input and res.default_input):
        filepath_in = DEFAULT_PATH_IN
    else:
        print(SPECIFY_PATH)
        return [None]

    if res.output:
        filepath_out = res.output[0]
    elif (not res.output and res.default_output):
        filepath_out = DEFAULT_PATH_OUT

    if res.count:
        topamount = res.count[0]

    if res.pattern:
        lang = res.pattern[0]
    return [filepath_in, filepath_out, topamount, lang]