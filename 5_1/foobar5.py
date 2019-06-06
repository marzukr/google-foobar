import math

# diffs = []
# prevC = 0
# cSum = 0
# for i in range(1, 201):
#     cSum += math.floor(i*math.sqrt(2))
#     if prevC != 0:
#         # print(cSum - prevC)
#         diffs.append(cSum - prevC)
#     prevC = cSum

# diffs2 = []
# prev = None
# for i in diffs:
#     if prev != None:
#         # print(i - prev)
#         diffs2.append(i - prev)
#     prev = i

# diffs3 = []
# prev2 = None
# for i in diffs2:
#     if prev2 != None:
#         # print(i - prev2)
#         diffs3.append(i - prev2)
#     prev2 = i

# prev3 = None
# for i in diffs3:
#     if prev3 != None:
#         print(i - prev3)
#         # diffs3.append(i - prev2)
#     prev3 = i




# calcs = []
# for i in range(1, 101):
#     num = math.floor( math.sqrt(2) * (i * (i+1)/2) )
#     calcs.append(num)

# diffs = []
# for i in range(0, 100):
#     diffs.append(calcs[i] - sums[i])

# prev = 0
# for i in diffs:
#     if prev != 0:
#         print(i - prev)
#     prev = i


# a = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# for i in range(1, a):
#     a * math.sqrt(2)
#     print(i)

# def solution(n):
#     column = []
#     for i in range(1, n + 1):
#         even = 2 * i

from decimal import *

getcontext().prec = 150

def formula(a, n):
    if n != 0:
        nPrime = int( (a - 1) * n )
        return n*nPrime + n*(n + 1)/2 - nPrime*(nPrime + 1)/2 - formula(a, nPrime)
    return 0

def solution(s):
    a = Decimal(2).sqrt()
    nInt = int(s)
    return str(int(formula(a, nInt)))

# print(brute(50000000))
print(solution(10**100))
