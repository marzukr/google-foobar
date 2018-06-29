def answer(n):
    A = [1] + [0] * n
    for k in xrange(1, n+1):
        for i in xrange(n, k-1, -1):
            A[i] += A[i-k]
    return A[n] - 1