# for i in xrange(100, 200):
#     print i ^ (i+1)

def answer(start, length):
    checksum = 0
    cLength = length
    lineStart = start
    while cLength >= 1:
        checksum ^= seqXOR(lineStart, lineStart + cLength - 1)
        # for i in xrange(0, length):
        #     if i < cLength:
        #         checksum ^= lineStart + i
        lineStart += length
        cLength += -1
    return checksum

def seqXOR(start, stop):
    return oneSeqXOR(stop) ^ oneSeqXOR(start - 1)

def oneSeqXOR(n):
    test = n & 3
    if test == 0:
        return n
    elif test == 1:
        return 1
    elif test == 2:
        return n + 1
    elif test == 3:
        return 0