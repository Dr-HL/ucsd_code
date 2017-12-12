#!/usr/bin/env python

"""
FrequentWordsProblem(Text,k)
counts ← 0 for all possible kmers
for i ← 0 to |Text| - |Pattern|
kmer ← Text(i,|Pattern|)
counts(kmer) ← counts(kmer) + 1
count ← count + 1
return all kmers where counts(kmer) = max(counts)

    FrequentWords(Text, k)
        FrequentPatterns ← an empty set
        for i ← 0 to |Text| − k
            Pattern ← the k-mer Text(i, k)
            Count(i) ← PatternCount(Text, Pattern)
        maxCount ← maximum value in array Count
        for i ← 0 to |Text| − k
            if Count(i) = maxCount
                add Text(i, k) to FrequentPatterns
        remove duplicates from FrequentPatterns
        return FrequentPatterns
"""

#fw_file = input('Enter file: ')
fw_file = 'fqword.txt'
def open_file(fw_file):
    with open(fw_file, 'r') as f:
        read_file = f.read().rstrip()
        return read_file

def frequent_words(text, k):
    count = {}
    for i in range(len(text)-k+1): #why +1?
        if text[i:i+k] not in count:
            count[text[i:i+k]] = 0
        count[text[i:i+k]] += 1
    m = max(count.values())
    out = []
    for kmer in count:
        if count[kmer] == m:
            out.append(kmer)
    return out

text = 'TAAACGTGAGAGAAACGTGCTGATTACACTTGTTCGTGTGGTAT'
k = 3
print(frequent_words(text, k))
