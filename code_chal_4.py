#!/usr/bin/env python

"""
Input​: Two strings, Pattern and Genome
Output​: All starting positions where Pattern appears as a substring of Genome
"""

genome_file = 'cholera_ref_genome.txt'

def open_the_file(genome_file):
    with open(genome_file, 'r') as f:
        f = f.read().rstrip()
    return f

def open_pat_file(pattern_file):
    with open(patern_file, 'r') as pf:
        pf = pf.read().rstrip()
    return pf

def match_position(text, pattern):
    t = len(text)
    p = len(pattern)

    match_positions = []

    for i in range(t-p + 1):
        if pattern_match(text,pattern,i):
            match_positions.append(i)
    new_match_positions = ' '.join(str(item) for item in match_positions)
    return new_match_positions

def pattern_match(text, pattern, i):
    for j in range(len(pattern)):
        if pattern[j] != text[i+j]:
            return False
    return True

text = open_the_file(genome_file)
pattern = 'CTTGATCAT'


print(match_position(text, pattern))
