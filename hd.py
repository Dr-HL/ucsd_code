
import operator

def h_d(seq_one, seq_two):
    ne = operator.ne
    return sum(map(ne, seq_one, seq_two))
