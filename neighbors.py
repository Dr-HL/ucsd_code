#!/usr/bin/env python3

import approxpatterncount as apc
import reversecomplement as rc
import sys

"""
Suffix function returns the suffix for each sequence
that is passed through.
"""
def suffix(sequence):
    return sequence[1:]


def reverse_complement(dna):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join([complement[base] for base in dna[::-1]])


def recursive_neighbors(sequence, d):
    if d == 0:
        return sequence
    if len(sequence) == 1:
        return ['A', 'C', 'G', 'T']
    list_w_rc = []
    suffix_neighbors = recursive_neighbors(suffix(sequence), d)
    for text in suffix_neighbors:
        if apc.h_d(suffix(sequence), text) <= d:
            for x in ['A', 'C', 'G', 'T']:
                list_w_rc.append(''.join([x, text]))
        else:
            list_w_rc.append(''.join([sequence[0], text]))
    return list_w_rc

#print(recursive_neighbors('GGCCCAGAG', 3))

def immediate_neighbors(pattern):
    neighborhood = [pattern]
    #neighborhood.add(pattern)

    nucleotide_list = list('ACGT')

    for i in range(0, len(pattern)):
        symbol = pattern[i]
        for n in nucleotide_list:
            if symbol != n:
                neighbor = pattern.replace(pattern[i], n)
                neighborhood.append(neighbor)

    return neighborhood


def iterative_neighbors(pattern, d):
    new_neighborhood = set()
    new_neighborhood.add(pattern)
    for j in range(d):
        for prime_pattern in new_neighborhood:
            new_neighbor = immediate_neighbors(prime_pattern)
            print(new_neighbor)

    return new_neighborhood

sequence = 'GTACCTCGAAC'
d = 3

"""
with open('testwrite.txt', 'wt') as w:
    w.write('\n'.join(map(str, recursive_neighbors(sequence, d))) + '\n')
"""
