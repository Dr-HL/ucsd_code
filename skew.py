#!/usr/bin/env python3

sequence = 'GAGCCACCGCGATA'

def gc_count_skew(sequence):
    skew = [0]
    for i in range(len(sequence)):
        skew.append(skew[-1])
        if sequence[i] == 'G':
            skew[i + 1] = skew[i] + 1
        if sequence[i] == 'C':
            skew[i + 1] = skew[i] - 1
    final_count = ' '.join(map(str, skew))
    return final_count


print(gc_skew(sequence))
