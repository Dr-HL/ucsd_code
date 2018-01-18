#!/usr/bin/env python3

sequence = 'GATACACTTCCCGAGTAGGTACTG'

def gc_count_skew(sequence):
    skew = [0]
    for i in range(len(sequence)):
        skew.append(skew[-1])
        if sequence[i] == 'G':
            skew[i + 1] = skew[i] + 1
        if sequence[i] == 'C':
            skew[i + 1] = skew[i] - 1
    max_skew = max(skew)
    final_count = ' '.join(map(str, skew))

    return max_skew


print(gc_count_skew(sequence))
