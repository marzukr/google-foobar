import operator as op
import itertools

def answer(num_buns, num_required):
    for buns_per_key in xrange(0, num_buns + 1):
        num_keys = ncr(num_buns, buns_per_key)
        # keys_per_bun = int(num_keys * (buns_per_key*1.0/num_buns))
        
        key_assignments = [["0"] * num_buns for i in xrange(0, num_keys)]
        key_i = 0
        for assignment in itertools.combinations(range(0, num_buns), buns_per_key):
            for bun in assignment:
                key_assignments[key_i][bun] = "1"
            key_i += 1
        
        bunnies = []
        for bun in xrange(0, num_buns):
            bunny = ""
            for key in xrange(0, num_keys):
                bunny += key_assignments[key][bun]
            bunnies.append(bunny)
        # solutions.append(bunnies)
        if isValid(bunnies, num_buns, num_required):
            return reformat(bunnies)
    return [[]] * num_buns

def isValid(solution, num_buns, num_required):
    for bun_combo in itertools.combinations(range(0, num_buns), num_required):
        result = 0
        for bun in bun_combo:
            result |= int(solution[bun], 2)
        if result != int("1" * len(solution[0]), 2):
            return False
    for bun_combo in itertools.combinations(range(0, num_buns), num_required - 1):
        result = 0
        for bun in bun_combo:
            result |= int(solution[bun], 2)
        if result == int("1" * len(solution[0]), 2):
            return False
    return True

def reformat(solution):
    formatSoln = []
    for bun in solution:
        formatBun = []
        for i in xrange(0, len(bun)):
            if bun[i] == "1":
                formatBun.append(i)
        formatSoln.append(formatBun)
    return formatSoln
    
def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, xrange(n, n-r, -1), 1)
    denom = reduce(op.mul, xrange(1, r+1), 1)
    return numer//denom