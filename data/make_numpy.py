import numpy as np
import os
import re
from collections import Counter


def single_matrix_from_string(matstringlist) -> np.array:
    fullmatrix = []
    for line in matstringlist:
        fullmatrix += [[float(x) for x in line.split()]]
    print(np.array(fullmatrix).shape)
    assert np.array(fullmatrix).shape == (4, 26)
    return np.array(fullmatrix)

def extract_hodge_number_from_string(metastring) -> int:
    hodge_search = re.search('H:(.*),', metastring)
    if hodge_search:
        hodgestring = hodge_search.group(1)
        return int(hodgestring)

def parse_txt_file():
    dirpath = os.path.dirname(os.path.realpath(__file__))
    rawpath = os.path.join(dirpath, 'raw/v26')
    X = []
    y = []
    with open(rawpath) as file:
        counter = 0
        reading_buffer = []
        for line in file:
            counter += 1
            reading_buffer += [line.rstrip()]
            if counter % 5 == 0:
                print(counter)
                print(reading_buffer)
                try:
                    new_y = extract_hodge_number_from_string(reading_buffer[0])
                    new_X = single_matrix_from_string(reading_buffer[1:5])
                except AssertionError as e:
                    break
                y += [new_y]
                X += [new_X]
                reading_buffer = []
    print(Counter(y))
    return np.array(X), np.array(y)


if __name__ == '__main__':
    X, y = parse_txt_file()
    print(np.array(X).shape)
    print(np.array(y).shape)
