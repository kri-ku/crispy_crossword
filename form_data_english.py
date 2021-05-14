
from collections import OrderedDict

def read_and_form_data():
    list = {}
    # reads data from Ubuntu's word list
    # similar than form_data_finnish.py
    with open('/usr/share/dict/american-english') as f:
        for line in f:
            line_stripped = line.rstrip('\n')
            if len(line_stripped) not in list.keys():
                list[len(line_stripped)] = []
            list[len(line_stripped)].append(line_stripped)
    f.close()

    sorted_list = OrderedDict(sorted(list.items(), reverse=True) )
    return sorted_list

