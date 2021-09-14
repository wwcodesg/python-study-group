# Solution to problem:
# https://app.codility.com/programmers/lessons/6-sorting/triangle/
# Session reports:
# https://app.codility.com/demo/results/trainingAUVXUB-MGZ/ # 100%

def solution(A):
    if len(A) < 3:
        return 0

    # Sort array to get possible triangular values, 
    # as values closest to each other have highest chance of being triangular
    A.sort()
    p, q, r = A[0], A[1], A[2]

    # check first case
    if len(A) ==  3:
        if (p + q > r) and (q + r > p) and (r + p > q):
            return 1
        else:
            return 0

    # check the rest of the array
    A = A[3:]
    for item in A:
        p = q
        q = r
        r  = item
        if (p + q > r) and (q + r > p) and (r + p > q):
            return 1
    
    return 0
