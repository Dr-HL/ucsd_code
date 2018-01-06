#!/usr/bin/env python3


import operator

def open_file(sequence):
    with open('genomedata.txt', 'r') as f:
        f = f.read()
        return f

def gc_count_skew(sequence):
    skew = [0]
    for i in range(len(sequence)):
        skew.append(skew[-1])
        if sequence[i] == 'G':
            skew[i + 1] = skew[i] + 1
        if sequence[i] == 'C':
            skew[i + 1] = skew[i] - 1
    return skew

def min_skew(skew_list):

    min_value = min(skew_list)

    indices = [i for i, v in enumerate(skew_list) if v == min_value]

    final_indices = ' '.join(map(str, indices))

    return final_indices

sequence = 'GATACACTTCCCGAGTAGGTACTG'

print(min_skew(gc_count_skew(sequence)))
