#!/usr/bin/env python3

import numpy as np
import math
import approxpatterncount as apc


MOTIF_TEST_LIST = ["TCGGGGGTTTTT", "CCGGTGACTTAC", "ACGGGGATTTTC", "TTGGGGACTTTT",
"AAGGGGACTTCC", "TTGGGGACTTCC", "TCGGGGATTCAT", "TCGGGGATTCCT","TAGGGGAACTAC",
"TCGGGTATAACC"]

def score_motif(motif_list):

    array_list = []

    for i in range(len(motif_list)):
        array_list.append([motif_list[i]])
    motif_matrix = np.matrix(array_list)


    return motif_matrix[2]



print(score_motif(MOTIF_TEST_LIST))
