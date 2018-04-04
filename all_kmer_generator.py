#!/usr/bin/env python3

"""

all_kmer_generator.py

@author: Timothy Baker
@version: 02/03/2018

"""




import pprint
import numbertopattern as ntp





def all_kmer_generator(KMER_LENGTH):
    """ Generates a set of all possible kmers given the input KMER_LENGTH """

    kmer_set = set()

    for i in range(4 ** KMER_LENGTH - 1):
        kmer_set.add(ntp.number_to_pattern(i, KMER_LENGTH))

    return kmer_set
