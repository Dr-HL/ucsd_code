#!/usr/bin/env python3


def get_quotient(index, k):
    list_of_quotients = []
    list_of_quotients.append(index)
    quotient = index
    for q in range(k):
        quotient = quotient / 4
        quotient = int(quotient)
        list_of_quotients.append(quotient)
        k = k - 1
    return list_of_quotients

def get_remainder(q_list): #returns a list of remainders from the list of list_of_quotients
    list_of_remainders = []
    for q in q_list:
        q = q % 4
        list_of_remainders.append(q)
    return list_of_remainders[::-1]

def make_base_four(index, k): #converts the base ten index to base four
    base_four_list = get_remainder(get_quotient(index, k))
    return base_four_list

def number_to_symbol(base_ten_index, k):
        sequence = make_base_four(base_ten_index, k)
        sequence_list = [sequence]
        symbol_list = []
        for number in list(sequence):
            if number == 0:
                symbol_list.append('A')
            if number == 1:
                symbol_list.append('C')
            if number == 2:
                symbol_list.append('G')
            if number == 3:
                symbol_list.append('T')
        return symbol_list

def number_to_pattern(index, k):
    symbol = ''.join(number_to_symbol(index, k))
    return symbol[-k:]
