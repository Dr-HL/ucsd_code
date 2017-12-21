#!/usr/bin/env python


def open_file(text_file):
    with open(text_file, 'r') as f:
        f = f.read()
        return f

sequence_one = 'TGACCCGTTATGCTCGAGTTCGGTCAGAGCGTCATTGCGAGTAGTCGTTTGCTTTCTCAAACTCC'
sequence_two = 'GAGCGATTAAGCGTGACAGCCCCAGGGAACCCACAAAACGTGATCGCAGTCCATCCGATCATACA'

def hamming_distance(sequence_one, sequence_two):
    count = 0
    for nucleotide_one, nucleotide_two in zip(sequence_one, sequence_two):
        if nucleotide_one != nucleotide_two:
            count += 1
    return count

print(hamming_distance(sequence_one, sequence_two))
