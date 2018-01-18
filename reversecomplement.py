#!/usr/bin/env python

"""
Find the reverse complement of a string
"""
#template_strand = 'template.txt'

"""
def open_template_strand(template_strand):
    with open(template_strand, 'r') as temp:
        temp = temp.read().rstrip()
        temp = temp.upper()
        return temp
"""
def reverse_complement(dna):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join([complement[base] for base in dna[::-1]])

#print(reverse_complement('AGGTA'))
"""
def reverse_complement(template):
    reverse_template_list = []
    for i in template:
        if i == 'A':
            reverse_template_list.append('T')
        if i == 'C':
            reverse_template_list.append('G')
        if i == 'G':
            reverse_template_list.append('C')
        if i == 'T':
            reverse_template_list.append('A')
    reverse_template = ''.join(reverse_template_list)
    #if len(template) == len(reverse_template):
    return reverse_template[::-1]
"""
#print(reverse_complement(template))
#template = open_template_strand(template_strand)

#print(reverse_complement(template))
