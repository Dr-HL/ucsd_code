#!/usr/bin/env python3


"""
@author: Timothy Baker
@version: 17/2/2018

 Find a Profile-most probable k-mer in a string.
     Input: A string Text, an integer k, and a 4 × k matrix Profile.
     Output: A Profile-most probable k-mer in Text.

"""

import numbertopattern as ntp
import sys
import operator
import motif_score_brute as msb
import pprint
import numpy as np
import functools
import re


PROFILE_MATRIX_DICT = {}


"""
lines = sys.stdin.read().splitlines()
for line in lines:
    sequence = lines[0]
    k_length = int(lines[1])
    PROFILE_MATRIX_DICT['A'] = [float(s) for s in lines[2].split(' ')]
    PROFILE_MATRIX_DICT['C'] = [float(s) for s in lines[3].split(' ')]
    PROFILE_MATRIX_DICT['G'] = [float(s) for s in lines[4].split(' ')]
    PROFILE_MATRIX_DICT['T'] = [float(s) for s in lines[5].split(' ')]
"""


TEST_SEQUENCE = 'ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT'
K_LENGTH = 5
INITIAL_PROFILE_MATRIX_DICT = {'A':[0.2, 0.2, 0.3, 0.2, 0.3], 'C':[0.4, 0.3, 0.1, 0.5, 0.1],
'G':[0.3, 0.3, 0.5, 0.2, 0.4], 'T':[0.1, 0.2, 0.1, 0.1, 0.2]}





def prod(factors):
    return functools.reduce(operator.mul, factors, 1)





def sequence_kmer_generator_dict(sequence, k):
    """generates and returns a dictionary of kmers with values initialized
    to k length"""

    kmer_dict = {}

    for i in range(len(sequence) - k + 1):
        kmer_dict[sequence[i:i+k]] = [0] * k
    return kmer_dict

#print(sequence_kmer_generator_dict(TEST_SEQUENCE, K_LENGTH))





def sequence_kmer_generator_list(sequence, k):
    """generates and returns a dictionary of kmers with values initialized
    to k length"""

    kmer_list = []

    for i in range(len(sequence) - k + 1):
        kmer_list.append(sequence[i:i+k])
    return kmer_list

#print(sequence_kmer_generator_list(TEST_SEQUENCE, K_LENGTH))





def generate_numpy_matrix(list_list):
    """converts a python list of lists to a numpy nd-array"""

    initial_matrix = np.array(list_list)
    return initial_matrix





def calc_kmer_prob(kmer_list, prob_mat):
    return {
        kmer: prod(
            prob_mat[base][i]
            for i, base in enumerate(kmer)
        )
        for kmer in kmer_list
    }

#print(calc_kmer_prob(sequence_kmer_generator_list(TEST_SEQUENCE, K_LENGTH), INITIAL_PROFILE_MATRIX_DICT))





def kmer_probability_dict_generator(kmer_dict, initial_matrix_dict):
    """ Input is a dictionary with kmers as a key, and an initialized
    list of k elements as the value and replaces zero values with that of the
    matrix values """

    #kmer_prob_dict = {}

    for kmer, values in kmer_dict.items():
        for i in range(len(values)):
            for base in kmer:
                kmer_dict[kmer][i] = initial_matrix_dict[base][i]
        #kmer_dict[kmer] = prod(kmer_dict[kmer])

    return kmer_dict

pprint.pprint(
    kmer_probability_dict_generator(
        sequence_kmer_generator_dict(TEST_SEQUENCE, K_LENGTH),
        INITIAL_PROFILE_MATRIX_DICT,
    )
)






def max_kmer_dict_values(kmer_dict):
    """ Multiples the values list of each kmer and returns the maximum probability """

    kmer_prob_prod_dict = {}

    for kmer, values in kmer_dict.items():
        kmer_prob_prod_dict[kmer] = np.prod(values)

    max_kmer = max(kmer_prob_prod_dict.items(), key=operator.itemgetter(1))[0]

    return max_kmer


#pprint.pprint(max_kmer_dict_values(calc_kmer_prob(sequence_kmer_generator_list(TEST_SEQUENCE, K_LENGTH), INITIAL_PROFILE_MATRIX_DICT)))




def find_consensus_v3(frequency_matrix):
    """generates a consensus sequence given a frequency dictionary of lists"""

    consensus = ''
    dna_length = len(frequency_matrix['A'])

    for i in range(dna_length):  # loop over positions in string
        max_freq = -1            # holds the max freq. for this i
        max_freq_base = None     # holds the corresponding base

        for base in 'ACGT':
            if frequency_matrix[base][i] >= max_freq:
                max_freq = frequency_matrix[base][i]
                max_freq_base = base
            elif frequency_matrix[base][i] == max_freq:
                max_freq_base = '-' # more than one base as max

        consensus += max_freq_base  # add new base with max freq
    return consensus





def generate_initial_profile(kmer_list):
    """generates a dictionary of nucleotide probability based on a sequence list"""

    profile_dict = {}

    for i in range(len(kmer_list)):
        for kmer in kmer_list:
            profile_dict[kmer] = msb.generate_matrix(kmer)
    return profile_dict





def main():
    print(max_kmer_dict_values(
    calc_kmer_prob(
    sequence_kmer_generator_list(sequence, k_length), PROFILE_MATRIX_DICT)))
#use logging module python3



"""
if __name__ == '__main__':
    main()
"""
