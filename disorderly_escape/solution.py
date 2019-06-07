import numpy as np
import itertools
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

def is_equivalent(a,b):
    a_row_id = []
    b_row_id = []
    for i in range(0, np.size(a, 0)):
        a_row_id.append(np.bincount(a[i]).tolist())
        b_row_id.append(np.bincount(b[i]).tolist())
    a_row_id.sort()
    b_row_id.sort()
    if a_row_id != b_row_id: return False

    a_row_id = []
    b_row_id = []
    for i in range(0, np.size(a, 1)):
        a_row_id.append(np.bincount(np.transpose(a)[i]).tolist())
        b_row_id.append(np.bincount(np.transpose(b)[i]).tolist())
    a_row_id.sort()
    b_row_id.sort()
    return a_row_id == b_row_id

a = np.array([[0,0],[1,1]])
b = np.array([[0,1],[0,1]])
# print(is_equivalent(a,b))

def solution(w, h, s):
    unique = []
    for i in itertools.product(range(0,s), repeat = w * h):
        test = np.reshape(np.array(i), (w, h))
        is_unique = True
        for u in unique:
            if is_equivalent(test, u):
                is_unique = False
                break
        if is_unique:
            unique.append(test)
    return len(unique)

for i in range(1,13):
    print(solution(1,i,3))