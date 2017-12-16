#!/usr/bin/env Python

"""
    PatternCount(Text, Pattern)
        count ← 0
        for i ← 0 to |Text| − |Pattern|
            if Text(i, |Pattern|) = Pattern
                count ← count + 1
        return count
"""

ref_file = 'cholera_ref_genome.txt'
ori_file = 'cholera_ori_seq.txt'

def open_ref_genome(ref_file):
    with open(ref_file, 'r') as ref:
        ref = ref.read().rstrip()
        ref = ref.upper()
        #return ref
        print(ref)

def open_ori_seq(ori_file):
    with open(ori_file, 'r') as ori:
        ori = ori.read().rstrip()
        ori = ori.upper()
        #return ori
        print(ori)

def pattern_count(text, pattern):
    t = len(text) #sets t to the length of the text
    p = len(pattern) #sets p to the length of the pattern
    count = 0
    for i in range(t-p + 1):
        if pattern_match(text, pattern, i):
            count += 1
    return count

def pattern_match(text, pattern, i):
    for j in range(len(pattern)):
        if pattern[j] != text[i+j]:
            return False
    return True

open_ref_genome(ref_file)
open_ori_seq(ori_file)
#text = open_ref_genome(ref_file)
#pattern = open_ori_seq(ori_file)


#print(pattern_count(text,pattern))
