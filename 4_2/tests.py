# def next_turn(a,b):
#     if a<b: 
#         return 2*a,b-a
#     elif a>b: 
#         return a-b, 2*b
#     else: 
#         return a,b

# for i in xrange(1, 15):
#     a,b = 4-i,i
#     for i in xrange(50):
#         # print a,b
#         a,b = next_turn(a,b)
#     print a,b
    # if a == b:
    #     print i

# a,b = 1005,915
# for i in xrange(50):
#     print a,b
#     a,b = next_turn(a,b)
# print a,b

# def answer(banana_list):
#     for i in xrange(len(banana_list)):
#         for j in 

# for i in xrange(80):
#     if (2**i * 25) % 80 == -55 % 80:
#         print i

# def equalizes_brute(a,b):
#     i = 0
#     # states = [(a,b)]
#     while a != b and i < 10000:
#         a,b = next_turn(a,b)
#         # if (a,b) not in states:
#         #     states.append((a,b))
#         # else:
#         #     break
#         i += 1
#     # if i > 10000:
#     #     print "hello"
#     return a == b

# for j in xrange(1,200):
#     for i in xrange(1,j):
#         if equalizes_brute(j-i, i):
#             print j,i

def equalizes(a,b):
    if (a+b) & 1 == 0:
        multiple = a+b
        while multiple & 1 == 0:
            multiple /= 2
        test = multiple
        while test < a+b:
            if test == a or test == b:
                return True
            test += multiple
    return False

# for a in xrange(1, 100):
#     for b in xrange(1, 100):
#         if does_equalize(a,b):
#             print a,b

# def pow_two_test(a):
#     i = 0
#     while True:
#         yield 2**i - a
#         i += 1

# def a068156(a):
#     i = 1
#     while True:
#         yield a * (2**i - 1)
#         i += 1

# def odd_test(a, start):
#     result = start
#     i = 0
#     yield result
#     while True:
#         result += (a+start)*2**i
#         yield result
#         i += 1

# def equalizes(a,b):
#     smallers = []
#     for i in pow_two_test(a):
#         if i > b:
#             break
#         if i == b:
#             return True
#         if i < b:
#             smallers.append(i)
#     for i in a068156(a):
#         if i > b:
#             break
#         if i == b:
#             return True
#         if i < b:
#             smallers.append(i)
#     # return equalizes_brute(a,b)
#     # for start in smallers:
#     #     for i in odd_test(a, start):
#     #         if i > b:
#     #             break
#     #         if i == b:
#     #             return True
#     # for i in xrange(1, b):
#     #     if i not in smallers:
#     #         for i in odd_test(a, start):
#     #             if i > b:
#     #                 break
#     #             if i == b and equalizes_brute(a,i):
#     #                 return True
#     return False

# a = 2**30 - 1012421412
# for b in xrange(1, 10000):
#     if test_equalizes(a,b):
#         # print max(a,b) // min(a,b)
#         # print a // b
#         print b

# for i in xrange(1,143):
#     print does_equalize(144, 144-i)

# equalizers = [i.split(" ") for i in open("equalizers.txt", "r").read().split("\n")]
# equalizers = [(int(i[0]), int(i[1])) for i in equalizers]
# for e in equalizers:
#     print e[0] * e[1]

# def a068156(a, n):
#     if n == 1:
#         return a
#     else:
#         return a068156(a, n-1) + a*2**(n-1)

# def a068156(a, n):
#     return a * (2**n - 1)

# for i in xrange(25):
#     print 2**i - 55
