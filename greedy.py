#!/usr/local/bin/python3

"""
@author: Tim Baker
@version: 08/03/2018
greedy.py
"""


K_LENGTH = 3
MOTIF_TEST_LIST = ['GGCGTTCAGGCA', 'AAGAATCAGTCA', 'CAAGGAGTTCGC',
'CACGTCAATCAC', 'CAATAATATTCG']


import pprint
import kmer_generator as kg #stand-alone kmer generation module





def greedy_motif_search(motif_list, k):

    best_motif = []
    for sequence in motif_list:
        best_motif.append(kg.sequence_kmer_generator_list(sequence, K_LENGTH)[0])

    for i in range(len(motif_list[0]) - k + 1):
        motif = [motif_list[0][i:i+k]]
        for n in range(1,len(motif_list)):
            pr



pprint.pprint(greedy_motif_search(MOTIF_TEST_LIST, K_LENGTH))
