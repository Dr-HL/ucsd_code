#!/usr/bin/env python

"""
Input​: Two strings, Pattern and Genome
Output​: All starting positions where Pattern appears as a substring of Genome
"""

def match_position(text, pattern):
    t = len(text)
    p = len(pattern)

    match_positions = []

    for i in range(t-p + 1):
        if pattern_match(text,pattern,i):
            match_positions.append(i)
    #new_match_positions = ' '.join(str(item) for item in match_positions)
    return match_positions

def pattern_match(text, pattern, i):
    for j in range(len(pattern)):
        if pattern[j] != text[i+j]:
            return False
    return True
