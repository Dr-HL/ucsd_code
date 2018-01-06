#!/usr/bin/env python3


import frequentwords_2 as fw
import approxpatterncount as apc
import neighbors
import patterntonumber as ptn
import numbertopattern as ntp
import sys

lines = sys.stdin.read().splitlines()
for line in lines:
    genome = lines[0]
    k = int(lines[1])
    d = int(lines[2])

def freq_seq_mismatch_sort(genome, k, d):
    frequent_patterns = set()
    neighborhoods = []
    count = [0]
    pos_index = [0]

    for i in range(len(genome) - k):
        neighborhoods.append(neighbors.recursive_neighbors(genome[i:i+k], d))

    flattened_neighborhood = [i for i in apc.iter_flatten(neighborhoods)]

    for i in range(len(neighborhoods) - 1):
        pattern = flattened_neighborhood[i]
        pos_index.append(ptn.pattern_to_number(pattern))
        count.append(1)

    sorted_index = sorted(pos_index)

    for i in range(len(neighborhoods) - 1):
        if sorted_index[i] == sorted_index[i + 1]:
            count[i + 1] = count[i] + 1
            print(count)

    max_count = max(count)

    for i in range(len(neighborhoods) - 1):
        if count[i] == max_count:
            pattern = ntp.number_to_pattern(sorted_index[i], k)
            frequent_patterns.add(pattern)

    return frequent_patterns

print(freq_seq_mismatch_sort(genome, k, d))
