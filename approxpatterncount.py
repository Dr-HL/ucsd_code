 #!/usr/bin/env python

"""
approxpatterncount.py
Section 1.4 of Week 2
@author: Timothy Baker
@version: 12-19-2017
"""

import patternmatching
import sys
import itertools
import operator


def iter_flatten(iterable):
  it = iter(iterable)
  for e in it:
    if isinstance(e, (list, tuple)):
      for f in iter_flatten(e):
        yield f
    else:
      yield e


def hamming_distance(sequence_one, sequence_two):
    distance = 0
    for nucleotide_one, nucleotide_two in zip(sequence_one, sequence_two):
        if nucleotide_one != nucleotide_two:
            distance += 1
    return distance

def hamming_distance_v2(seq_one, seq_two):
    #assert len(seq_one) == len(seq_two)
    ne = operator.ne
    return sum(map(ne, seq_one, seq_two))

def approx_pattern_count(sequence, kmer, d):
    list_of_kmers =[]
    count = 0
    for the_index in range(len(sequence) - len(kmer) + 1):
        new_kmer = sequence[the_index:the_index+len(kmer)]
        if h_d(kmer, new_kmer) <= d:
            list_of_kmers.append(new_kmer)
            count += 1
    return count

#print(approx_pattern_count('TACGCATTACAAAGCACA', 'AA', 1))

def get_position(array_of_kmers):
    array_of_positions = []
    for kmer in array_of_kmers:
        start_pos = patternmatching.match_position(sequence, kmer)
        array_of_positions.append(start_pos)
    flattened_array = [i for i in iter_flatten(array_of_positions)]
    sorted_set_list = sorted(set(flattened_array))
    new_set_of_positions = ' '.join(str(item) for item in sorted_set_list)
    return new_set_of_positions
