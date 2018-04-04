#!/usr/bin/env python3


import neighbors
import sys
import hd
import approxpatterncount as apc
from collections import Counter

#use all caps ; when writing test names be as explicit as possible. don't use single letter variables.
#Dna = ['TACCGTAGTCGTCGTCACACCAGGC', 'CTCTGGTCACTTTCGCGGATAAAAC', 'ACACGTTATTCATACTTAGGGGCTA', 'TATACGGGCAGGTAACGCGTTACTT', 'CCAACGAGACGCCACAGCATCAGGG', 'GAAGTACCCACACACAGTGGGCAGA']
#k = 5
#d = 2



def generate_kmers_w_neighbors(sequence, k, d):
    """
    Generates and returns a list of k_mers for a given sequence with at most d-mismatches
    """
    list_of_neighbors_from_kmers = []
    for i in range(len(sequence) - k + 1): #
        list_of_neighbors_from_kmers.append(recursive_neighbors(sequence[i:i+k],d))
    return list_of_neighbors_from_kmers




def recursive_neighbors(sequence, d):
    """
    Generates the possible SNPs given a sequence with at most d-mismatches
    """

    if d == 0:
        return sequence
    if len(sequence) == 1:
        return ['A', 'C', 'G', 'T']
    list_w_rc = []
    suffix_neighbors = recursive_neighbors(sequence[1:], d)
    for text in suffix_neighbors:
        if apc.hamming_distance_v2(sequence[1:], text) < d:
            for x in ['A', 'C', 'G', 'T']:
                list_w_rc.append(''.join([x, text]))
        else:
            list_w_rc.append(''.join([sequence[0], text]))
    return list_w_rc



def motif_enumeration(Dna, k, d):
    """
    Generates motifs common between multiple sequence strings
    with d-mismatches (SNPs) of their k-mers.
    """

    k_mer_list = []
    new_kmer_list_w_neighbors = []

    for i in range(len(Dna)):
        k_mer_list.append(generate_kmers_w_neighbors(Dna[i], k, d))

    for i in range(len(k_mer_list)):
        new_kmer_list_w_neighbors.append([lst for lst in apc.iter_flatten(k_mer_list[i])])

    intersection = set.intersection(*map(set, new_kmer_list_w_neighbors))

    pretty_new_intersection = ' '.join(str(item) for item in intersection)

    return pretty_new_intersection
