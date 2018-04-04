#!/usr/bin/env python3

"""
motif_score_brute.py
@author = Tim Baker
@date = 2/06/2018
"""

#TEST_MOTIF_LIST = ["TCGGGGGTTTTT", "CCGGTGACTTAC", "ACGGGGATTTTC", "TTGGGGACTTTT", "AAGGGGACTTCC",
#"TTGGGGACTTCC", "TCGGGGATTCAT", "TCGGGGATTCCT", "TAGGGGAACTAC", "TCGGGTATAACC"]

#TEST_MOTIF_LIST_2 = ['AAATTGACGCAT', 'GACGACCACGTT', 'CGTCAGCGCCTG', 'GCTGAGCACCGG',
#'AGTTCGGGACAG']

def generate_matrix(motif_list):
    """ generates a dictionary with frequency values at each position """

    k = len(motif_list[0])
    profile = {'A':[0]*k, 'C':[0]*k, 'G':[0]*k, 'T':[0]*k}
    div = float(len(motif_list))
    for i in range(k):
        for motif in motif_list:
            profile[motif[i]][i] += 1
        for key in profile:
            profile[key][i] /= div
    return profile


def construct_sequence(profile):
    """ constructs the sequence from the profile frequency dictionary """

    consensus = []
    length_of_value = len(profile['A'])


    for key,value in profile.items():
        if key == 'A':
            count_A = profile[key]
        elif key == 'C':
            count_C = profile[key]
        elif key == 'G':
            count_G = profile[key]
        elif key == 'T':
            count_T = profile[key]

    for i in range(length_of_value):
        if count_A[i] > max(count_C[i],count_G[i],count_T[i]):
            consensus.append('A')
        elif count_C[i] > max(count_A[i],count_G[i],count_T[i]):
            consensus.append('C')
        elif count_G[i] > max(count_A[i],count_C[i],count_T[i]):
            consensus.append('G')
        elif count_T[i] > max(count_A[i],count_C[i],count_G[i]):
            consensus.append('T')


    pretty_consensus = ''.join(i for i in consensus)

    return pretty_consensus


def main():
    return construct_sequence(generate_matrix(TEST_MOTIF_LIST_2))



if __name__ == '__main__':
    print(main())
