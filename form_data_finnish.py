
from collections import OrderedDict

def read_and_form_data():
    list = {}
    # read data and form it to dictionary
    # where key-value pairs
    # (key= length of the word,  value= list of words)
    with open('dict_finnish.txt') as f:
        for line in f:
            line_stripped = line.rstrip('\n')
            if len(line_stripped) not in list.keys():
                list[len(line_stripped)] = []
            list[len(line_stripped)].append(line_stripped)
    f.close()

    # sort list by keys from longest to smallest
    sorted_list = OrderedDict(sorted(list.items(), reverse=True) )

    return sorted_list

