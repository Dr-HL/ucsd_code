#!/usr/bin/env python3

"""
code_chal_5.py
(L,t) - clump problem
@author: Timothy Baker
@version: 12/12/2017
"""


genome_file = 'genome.txt'

def open_genome(genome_file):
    with open(genome_file, 'r') as f:
        f = f.read().rstrip()
        return f

def generate_count_dict(text, start, end, k):
    count = {}
    for j in range(start, end):
        kmer = text[j:j+k]
        if kmer not in count:
            count[kmer] = 0
        count[kmer] += 1
    return count

def add_out(count, t):
    output = set()
    for key, value in count.items():
        if value >= t:
            output.add(key)
    return output


def frequent_words(text, k, L, t):
    output = set()
    for i in range(0,len(text) - L):
        count = generate_count_dict(text, i, L-k+i, k)
        output = output.union(add_out(count, t))
    return output


text = open_genome(genome_file)

print(frequent_words(text, 11, 566, 18))
