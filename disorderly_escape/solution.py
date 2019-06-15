# import numpy as np
# import itertools
# from scipy.linalg import null_space

# def is_equivalent(a, b):
#     det_a = np.linalg.det(a)
#     det_b = np.linalg.det(b)
#     return abs(det_a) == abs(det_b)

# def is_equivalent(a, b):
#     a_list = a.tolist()
#     b_list = b.tolist()
#     a_list.sort()
#     b_list.sort()
#     if a_list == b_list: return True
    
#     a_list = np.transpose(np.array(a_list)).tolist()
#     b_list = np.transpose(np.array(b_list)).tolist()
#     a_list.sort()
#     b_list.sort()
#     return a_list == b_list

# def is_equivalent(a,b):
#     a_row_id = []
#     b_row_id = []
#     for i in range(0, np.size(a, 0)):
#         a_row_id.append(np.bincount(a[i]).tolist())
#         b_row_id.append(np.bincount(b[i]).tolist())
#     a_row_id.sort()
#     b_row_id.sort()
#     if a_row_id != b_row_id: return False

#     a_row_id = []
#     b_row_id = []
#     for i in range(0, np.size(a, 1)):
#         a_row_id.append(np.bincount(np.transpose(a)[i]).tolist())
#         b_row_id.append(np.bincount(np.transpose(b)[i]).tolist())
#     a_row_id.sort()
#     b_row_id.sort()
#     return a_row_id == b_row_id

# a = np.array([[0,0],[1,1]])
# b = np.array([[0,1],[0,1]])
# # print(is_equivalent(a,b))

# def solution(w, h, s):
#     unique = []
#     for i in itertools.product(range(0,s), repeat = w * h):
#         test = np.reshape(np.array(i), (w, h))
#         is_unique = True
#         for u in unique:
#             if is_equivalent(test, u):
#                 is_unique = False
#                 break
#         if is_unique:
#             unique.append(test)
#     return len(unique)

# for i in range(1,13):
#     print(solution(1,i,3))
# print(solution(2,3,2))

from collections import Counter
from math import factorial, gcd

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

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
                superscript = (v1.subscript * v1.superscript * v2.subscript * v2.superscript) / lcm_calc
                variables.append(Variable(superscript, lcm_calc))
        return CycleTerm(coefficient, variables)

    def plug_in(self, s):
        total = 1
        for var in self.variables:
            total *= s**var.superscript
        return total * self.coefficient

class Variable:
    def __init__(self, superscript, subscript):
        self.superscript = superscript
        self.subscript = subscript

def cycle_index(n):
    terms = []
    for j in partitions(n):
        coefficient = 1
        variables = []
        for k in range(1, n + 1): 
            if k in j:
                coefficient *= k**j[k] * factorial(j[k])
                variables.append(Variable(j[k], k))
        coefficient = 1 / coefficient
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
    return str(int(calc_cycle_index_result(comb_cycle_index, s)))

print(solution(2,3,4))