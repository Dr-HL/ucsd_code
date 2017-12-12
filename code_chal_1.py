#!/usr/bin/env Python

"""
    PatternCount(Text, Pattern)
        count ← 0
        for i ← 0 to |Text| − |Pattern|
            if Text(i, |Pattern|) = Pattern
                count ← count + 1
        return count

Input: Strings Text and Pattern.
Output: Count(Text, Pattern)

 Sample Input:
GCGCG
GCG

Sample Output:
2
"""

import re

def PatternCount(text, pattern):
    matches = []
    for i in range(len(text) - len(pattern)):
        for j in range(0,len(pattern)):
            if text[i+j] == pattern[j]:
                matches.append[i]
        else:
            break
    return matches

print(PatternCount('GCGCG', 'GCG'))
print(PatternCount('ACGTACGTACGT', 'CG'))
