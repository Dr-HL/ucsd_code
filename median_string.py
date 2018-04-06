#!/usr/bin/env python3



import numbertopattern as ntp
import approxpatterncount as apc
import bf_motif as bm
import operator
import sys
import pprint as pprint
import logging





DNA_LIST = []






lines = sys.stdin.read().splitlines()
for line in lines:
    K_LENGTH = int(lines[0])
    DNA_LIST = lines[1:]






def k_mer_generator(k):
    """returns a set of all 4^k k-mers"""

    k_mer_list = []
    for i in range(4**k - 1):
        k_mer_list.append(ntp.number_to_pattern(i, k))
    return set(k_mer_list)





def generate_kmer(sequence, k):
    """generates and returns a list of kmers for a given sequence and k"""

    kmer_list = []
    for i in range(len(sequence) - k + 1):
        kmer_list.append(sequence[i:i+k])
    return kmer_list





def minimum_hamming_distance(seq_one, value_kmer_list):
    """returns the minimum hamming distance from a list of kmers"""

    ne = operator.ne
    min_list = []
    for seq_two in value_kmer_list:
        min_list.append(sum(map(ne, seq_one, seq_two)))
    return min(min_list)





def distance_pattern_string(k_mer, dna_list):
    """returns the minimum distance between a possible k_mer
        and the kmers generated within the dna list; find the minimum
        hamming distance between the k_mer and each sequence in
        dna_list"""

    k = len(k_mer)

    distance = 0

    sequence_kmer_dict = {}

    for sequence in dna_list:
        sequence_kmer_dict[sequence] = generate_kmer(sequence, k)

    for key, value in sequence_kmer_dict.items():
        distance += minimum_hamming_distance(k_mer, value)


    return distance



def median_string(dna_list, k):
    """generates the median string that has the minimum distance"""

    median_list = []

    distance = k * (len(dna_list) - 1)

    for i in range(4**k - 1):
        k_mer = ntp.number_to_pattern(i,k)
        distance_pattern = distance_pattern_string(k_mer,dna_list)

        if distance > distance_pattern:
            distance = distance_pattern
            median = k_mer
            median_list = []

        if distance == distance_pattern:
            median_list.append(k_mer)

    return median_list





def main():
    print(median_string(DNA_LIST, K_LENGTH))





if __name__ == '__main__':
    main()
