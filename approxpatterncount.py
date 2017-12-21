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

lines = sys.stdin.read().splitlines()
for line in lines:
    kmer = lines[0]
    sequence = lines[1]
    d = int(lines[2])


def hamming_distance(sequence_one, sequence_two):
    distance = 0
    for nucleotide_one, nucleotide_two in zip(sequence_one, sequence_two):
        if nucleotide_one != nucleotide_two:
            distance += 1
    return distance

def h_d(seq_one, seq_two):
    assert len(seq_one) == len(seq_two)
    ne = operator.ne
    return sum(map(ne, seq_one, seq_two))

def approx_pattern_count(sequence, kmer, d):

    list_of_kmers =[]

    for the_index in range(len(sequence) - len(kmer) + 1):
        new_kmer = sequence[the_index:the_index+len(kmer)]
        if h_d(kmer, new_kmer) <= d:
            list_of_kmers.append(new_kmer)
    return list_of_kmers

print(approx_pattern_count(sequence, kmer, d))

def get_position(array_of_kmers):
    array_of_positions = []
    for kmer in array_of_kmers:
        start_pos = patternmatching.match_position(sequence, kmer)
        array_of_positions.append(start_pos)
    beautied_matched_positions = ' '.join(str(item) for item in array_of_positions)
    return beautied_matched_positions


print(get_position(approx_pattern_count(sequence, kmer, d)))
