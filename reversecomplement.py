#!/usr/bin/env python

"""
Find the reverse complement of a string
"""
template_strand = 'template.txt'

def open_template_strand(template_strand):
    with open(template_strand, 'r') as temp:
        temp = temp.read().rstrip()
        temp = temp.upper()
        return temp

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
    reverse_template_tuple = tuple(reverse_template_list)
    reverse_template = ''.join(reverse_template_tuple)
    if len(template) == len(reverse_template):
        return reverse_template[::-1]

template = open_template_strand(template_strand)

print(reverse_complement(template))
