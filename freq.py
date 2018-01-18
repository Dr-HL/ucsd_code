#!/usr/bin/env python3

import neighbors
import patterntonumber as ptn
import approxpatterncount as apc
import numbertopattern as ntp
import sys
import reversecomplement as rc


lines = sys.stdin.read().splitlines()
for line in lines:
    text = lines[0]
    k = int(lines[1])
    d = int(lines[2])


def freq_words_w_mismatches(text, k, d):
    freq_patterns = set()

    freq_patterns_w_reversecomp = []

    close_array = [0]
    freq_array = [0]

    neighborhood = []

    for i in range(4**k - 1):
        close_array.append(0)
        freq_array.append(0)

    for i in range(len(text) - k):
        neighborhood.append(neighbors.recursive_neighbors(text[i:i+k], d))

    flat_neighborhood = [i for i in apc.iter_flatten(neighborhood)]

    for pattern in flat_neighborhood:
        the_index = ptn.pattern_to_number(pattern)
        close_array[the_index] = 1


    for i in range(4**k - 1):
        if close_array[i] == 1:
            generated_pattern = ntp.number_to_pattern(i, k)
            freq_array[i] = apc.approx_pattern_count(text, generated_pattern, d)
            rc_pattern = rc.reverse_complement(generated_pattern)
            freq_patterns_w_reversecomp.append(rc_pattern)

    the_max_count = max(freq_array)

    for i in range(4**k -  1):
        if freq_array[i] == the_max_count:
            generated_kmer = ntp.number_to_pattern(i, k)
            freq_patterns.add(generated_kmer)

    return freq_patterns


print(freq_words_w_mismatches(text, k, d))
