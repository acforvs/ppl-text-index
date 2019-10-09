USAGE = '''USAGE:
[-i] 'path/to/inputfile'    : read data from the inputfile.
Example:
python3 main.py -i 'Users/user/Documents/in.txt'

[-io]   : read data from the defaul file ('/src/in.txt'). 
Examples:
1. python3 main.py -io

[-o] 'path/to/outputfile'   : print tht result to the outputfile.
Examples:
1. python3 main.py -o 'Users/user/Documents/out.txt'
2. python3 main.py -io -o 'Users/user/Documents/out.txt'

[-do]   : print the result to the defaul file ('/src/out.txt'). 
Examples:
1. python3 main.py -do
2. python3 main.py -io -do

[-c] amount   : in order to print only top-[amount] words
Examples:
1. python3 main.py -io -c 239
2. python3 main.py -io -do -c  30

[-u]    : usage 

[-p] [lang]   : specify language of the resulted words
[lang] in {'rus', 'eng'}
Examples:
1. python3 main.py -io -do -p eng
2. python3 main.py -io -p rus
'''

SPECIFY_PATH = '''Please, specify the path to the input data file or choose the default one 
and try again...
You can do this using one of the following options:
'''

WENT_WRONG = 'Something went wrong. Please try again...'

DEFAULT_PATH_IN = '/Users/vladislavsavinov/Projects/ppl-text-index-acforvs/src/in.txt'

DEFAULT_PATH_OUT = '/Users/vladislavsavinov/Projects/ppl-text-index-acforvs/src/out.txt'

NO_SUCH_FILE = 'Please, check the corectness of the submitted filepath and try again...'

OUTPUT_MESS = '{}   : {} time(s) on pages'

PAGE_DESCR = "page {} : {} times\n"

SEPARATOR = '__________________________________________________________________________'

rus_pattern = "((?:[а-я]+[-']?)*[а-я]+)"

eng_pattern = "((?:[a-z]+[-']?)*[a-z]+)"

gen_pattern = "((?:[а-я]+[-']?)*[а-я]+)|((?:[a-z]+[-']?)*[a-z]+)"