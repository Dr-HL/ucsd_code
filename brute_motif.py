#!/usr/bin/env python3


import neighbors
import sys
import hd
import approxpatterncount as apc


#dna = 'ATTTGGC'
#k = 3
#d = 1




"""
the function generate_kmers returns a list of all kmers for a given
dna sequence with zero mismatches
"""


"""
the function generate_neighborhoods returns a list of all kmers
for a given dna sequence with at most d mismatches
"""




def brute_force_motif_enum(dna, k, d):
    set_of_patterns = set()
    kmer_list = generate_kmers(dna, k)
    kmer_neighborhood = generate_neighborhoods(dna, k, d)

    for kmer in kmer_list:
        for n_kmer in kmer_neighborhood:
            if hd.h_d(kmer, n_kmer) < d:
                set_of_patterns.add(n_kmer)

    return set_of_patterns


def main():
    dna_list = ['ATTTGGC', 'TGCCTTA', 'CGGTATC', 'GAAAATT']
    k = 3
    d = 1

    list_of_kmers_from_dna = []
    list_of_nkmers_from_dna = []
    set_of_patterns = set()

    for dna in dna_list:
        list_of_kmers_from_dna.append(generate_kmers(dna, k))

    for list_of_kmers in list_of_kmers_from_dna:
        for dna in list_of_kmers:
            list_of_nkmers_from_dna.append(generate_neighborhoods(dna, k, d))

    return list_of_nkmers_from_dna

print(main())
