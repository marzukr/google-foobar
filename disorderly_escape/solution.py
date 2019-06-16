from collections import Counter
from math import factorial
from fractions import Fraction, gcd

def lcm(a, b):
    return a*b // gcd(a, b)

def partitions(n, I=1):
    yield Counter({n: 1})
    for i in range(I, n//2 + 1):
        for p in partitions(n-i, i):
            yield Counter({i: 1}) + p

class CycleTerm:
    def __init__(self, coefficient, variables):
        self.coefficient = coefficient
        self.variables = variables

    def combine(self, term):
        coefficient = self.coefficient * term.coefficient
        variables = []
        for v1 in self.variables:
            for v2 in term.variables:
                lcm_calc = lcm(v1.subscript, v2.subscript)
                superscript = (v1.subscript * v1.superscript * v2.subscript * v2.superscript) // lcm_calc
                variables.append(Variable(superscript, lcm_calc))
        return CycleTerm(coefficient, variables)

    def plug_in(self, s):
        total = 1
        for var in self.variables:
            total *= s**var.superscript
        return Fraction(total) * self.coefficient

class Variable:
    def __init__(self, superscript, subscript):
        self.superscript = superscript
        self.subscript = subscript

def cycle_index(n):
    terms = []
    for j in partitions(n):
        denominator = 1
        variables = []
        for k in range(1, n + 1): 
            if k in j:
                denominator *= k**j[k] * factorial(j[k])
                variables.append(Variable(j[k], k))
        coefficient = Fraction(1, denominator)
        terms.append(CycleTerm(coefficient, variables))
    return terms

def combine_cycle_index(c1, c2):
    terms = []
    for term1 in c1:
        for term2 in c2:
            terms.append(term1.combine(term2))
    return terms

def calc_cycle_index_result(cycle_index, s):
    result = 0
    for term in cycle_index:
        result += term.plug_in(s)
    return result


def solution(w, h, s):
    row_cycle_index = cycle_index(h)
    col_cycle_index = cycle_index(w)
    comb_cycle_index = combine_cycle_index(row_cycle_index, col_cycle_index)
    return str(calc_cycle_index_result(comb_cycle_index, s))