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
import kmer_generator as kg
import profile_prob as pp
import logging


def generate_prob_matrix(k_mer_list):
    """ generates a probability matrix for k_mer """

    profile_list = []

    for nucleotide in enumerate(k_mer_list):
        



def greedy_motif_search(motif_list, k):


    best_motif = []
    for sequence in motif_list:
        best_motif.append(kg.sequence_kmer_generator_list(sequence, K_LENGTH)[0])
        #keeps a list of the first k-mer of each sequence

    for i in range(len(motif_list[0]) - k + 1):
        motif = [motif_list[0][i:i+k]]
        for n in range(1,len(motif_list)): #n = sequence index of motif list
            motif_kmer = motif_list[n][i:i+k]
            print(motif_kmer)



#pprint.pprint(greedy_motif_search(MOTIF_TEST_LIST, K_LENGTH))
