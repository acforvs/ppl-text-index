import pytest
import sys
path = '/src'
sys.path.insert(0, path)
from input_data import get_data_default

def test_1():
    output = get_data_default('/Users/vladislavsavinov/Projects/ppl-text-index-acforvs/src/test_texts/test_freq_dict1.txt', None)
    expected_output = [('дедлайна', 4503), ('нужный', 4503), ('для', 4503), ('тот', 4503), ('чтобы', 4503), ('в', 4503), ('он', 4503), ('не', 4503), ('укладываться', 4503)]
    assert  expected_output == output[0]
def test_2():
    output = get_data_default('/Users/vladislavsavinov/Projects/ppl-text-index-acforvs/src/test_texts/test_page_num1.txt', None)
    expected_output = {'deadline' : {1 : 45, 2 : 1}, 'is' : {1 : 45, 2 : 1}, 'an' : {1 : 45, 2 : 1}, 'amazing' : {1 : 45, 2 : 1}, 'thing' : {1 :45, 2 : 1}}
    assert output[1] == expected_output
def test_3():
    output = output = get_data_default('/Users/vladislavsavinov/Projects/ppl-text-index-acforvs/src/test_texts/test_freq_dict2.txt', 'e')
    expected_output = [('deadline', 45)]
    assert expected_output == output[0]
def test_4():
    output = output = get_data_default('/Users/vladislavsavinov/Projects/ppl-text-index-acforvs/src/test_texts/test_freq_dict2.txt', 'r')
    expected_output = [('здорово', 45)]
    assert expected_output == output[0]
def test_5():
    output = output = get_data_default('/Users/vladislavsavinov/Projects/ppl-text-index-acforvs/src/test_texts/test_freq_dict2.txt', 'e')
    expected_output = {'deadline' : {1 : 45}}
    assert expected_output == output[1]
def test_6():
    output = output = get_data_default('/Users/vladislavsavinov/Projects/ppl-text-index-acforvs/src/test_texts/test_freq_dict2.txt', 'r')
    expected_output = {'здорово' : {1 : 45}}
    assert expected_output == output[1]