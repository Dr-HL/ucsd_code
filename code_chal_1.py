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
AGCCTTTAG
"""

def PatternCount(text, pattern):
    t = len(text) #sets t to the length of the text
    p = len(pattern) #sets p to the length of the pattern
    count = 0
    for i in range(t-p + 1):
        if PatternMatch(text, pattern, i):
            count += 1
    return count

def PatternMatch(text, pattern, i):
    for j in range(len(pattern)):
        if pattern[j] != text[i+j]:
            return False
    return True

#print(PatternCount('GCGCG', 'GCG'))
#print(PatternCount('ACGTACGTACGT', 'CG'))
#print(PatternCount('AAAGAGTGTCTGATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAATTAAATTTTATTGACTTAGGTCACTAAATACTTTAACCAATATAGGCATAGCGCACAGACAGATAATAATTACAGAGTACACAACATCCAT', 'AAA'))
#print(PatternCount('AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT', 'TTT'))
#print(PatternCount(Readfile, 'GACCTCAGA'))
