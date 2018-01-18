#!/usr/bin/env python3

def pattern_to_number(Pattern): #Returns the number of k-mer from the k-mer list
    i = 0
    Number = 0
    while i < len(Pattern):
        if Pattern[i] == 'C':
            Number = Number + 1 * 4 ** (len(Pattern) - i - 1)
        elif Pattern[i] == 'G':
            Number = Number + 2 * 4 ** (len(Pattern) - i - 1)
        elif Pattern[i] == 'T':
            Number = Number + 3 * 4 ** (len(Pattern) - i - 1)
        i += 1
    return Number

def symbol_to_number(symbol):
    if symbol == 'A':
        return 0
    if symbol == 'C':
        return 1
    if symbol == 'G':
        return 2
    if symbol == 'T':
        return 3


def recursive_pattern_to_number(pattern):
    if len(pattern) == 0:
        return 0
    symbol = pattern[-1]
    prefix = pattern[:-1]
    return 4 * recursive_pattern_to_number(prefix) + symbol_to_number(symbol)
