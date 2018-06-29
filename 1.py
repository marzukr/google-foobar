def answer(s):
    length = len(s)
    for i in (x + 1 for x in xrange(0, length) if length % (x + 1) == 0):
        for j in (x for x in xrange(0, length - i, i)):
            if s[j : j + i] != s[j + i : j + i + i]:
                break
        else:
            return int(length/i)
    return 1