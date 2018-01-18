#!/usr/bin/env python


#fw_file = input('Enter file: ')
fw_file = 'fqword.txt'
def open_file(fw_file):
    with open(fw_file, 'r') as f:
        read_file = f.read().rstrip()
        return read_file

def frequent_words(text, k):
    count = {}
    all_kmers = []
    for i in range(len(text) - k + 1):
        all_kmers.append(text[i:i+k])
        if text[i:i+k] not in count:
            count[text[i:i+k]] = 0
        count[text[i:i+k]] += 1
    m = max(count.values())
    out = []
    for kmer in count:
        if count[kmer] == m:
            out.append(kmer)
    return count

#text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
#k = 4
#print(frequent_words(text, k))
