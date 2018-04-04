#!/usr/local/bin/python3

"""
@author: Timothy Baker
@version: 20/03/2018
kmer_generator.py
"""


def sequence_kmer_generator_list(sequence, k):
    """ returns a list of kmers with
    values initialized to k length """

    kmer_list = []

    for i in range(len(sequence) - k + 1):
        kmer_list.append(sequence[i:i+k])

    return kmer_list
