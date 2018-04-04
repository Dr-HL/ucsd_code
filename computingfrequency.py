#!/usr/bin/env python3


import patterntonumber as ptn
import sys

lines = sys.stdin.read().splitlines()
for line in lines:
    genome = lines[0]
    k = int(lines[1])


def computing_frequencies(text, k):
    frequency_array = [0]

    for i in range(4**k - 1):
        frequency_array.append(0)

    for j in range(len(text) - k + 1):
        kmer = text[j:j+k]
        kmer_index_b4 = ptn.recursive_pattern_to_number(kmer)
        frequency_array[kmer_index_b4] += 1
    beautified_frequency_array = ' '.join(map(str, frequency_array))

    return beautified_frequency_array

import time
start_time = time.time()
