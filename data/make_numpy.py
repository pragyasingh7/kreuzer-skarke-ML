import numpy as np
import os
import re
from collections import Counter


def single_matrix_from_string(matstringlist) -> np.array:
    fullmatrix = []
    for line in matstringlist:
        fullmatrix += [[float(x) for x in line.split()]]
    #print(np.array(fullmatrix).shape)
    assert np.array(fullmatrix).shape == (4, 26)
    return np.array(fullmatrix)

def single_matrix_from_string2(matstringlist) -> np.array:
    fullmatrix = []
    for line in matstringlist:
        fullmatrix += [[float(x) for x in line.split()]]
    fullmatrix = np.array(fullmatrix)
    if fullmatrix.shape == (4, 26):
        return fullmatrix
    elif fullmatrix.shape == (26, 4):
        return fullmatrix.transpose()
    else:
        E_msg = "Dimensions are invalid. Required (4, 26) or (26, 4), found " + str(fullmatrix.shape)
        raise ValueError(E_msg)

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
                #print(counter)
                #print(reading_buffer)
                try:
                    new_y = extract_hodge_number_from_string(reading_buffer[0])
                    new_X = single_matrix_from_string(reading_buffer[1:5])
                except AssertionError as e:
                    break
                y += [new_y]
                X += [new_X]
                reading_buffer = []

    dist = Counter(y)
    dist = sorted(dist.items(), key=lambda pair: pair[0])
    print("Distribution of first Hodge numbers: ", dist)
    return np.array(X), np.array(y)

def parse_txt_file2():
    dirpath = os.path.dirname(os.path.realpath(__file__))
    rawpath = os.path.join(dirpath, 'raw/v26')
    X = []
    y = []
    malformed_entries = 0
    with open(rawpath) as file:
        reading_buffer = []
        for line in file:
            l = line.rstrip()
            if re.search('H:(.*)', l):
                if reading_buffer:
                    try:
                        new_Y = extract_hodge_number_from_string(reading_buffer[0])
                        new_X = single_matrix_from_string2(reading_buffer[1:])
                    except ValueError as e:
                        print(e)
                        malformed_entries += 1
                        break
                    X.append(new_X)
                    y.append(new_Y)
                reading_buffer = [l]
                continue
            else:
                reading_buffer += [l]

    print("Number of malformed entries: ", malformed_entries)
    dist = Counter(y)
    dist = sorted(dist.items(), key=lambda pair: pair[0])
    print("Distribution of first Hodge numbers: ", dist)
    return np.array(X), np.array(y)


if __name__ == '__main__':
    X, y = parse_txt_file2()
    print(np.array(X).shape)
    print(np.array(y).shape)
