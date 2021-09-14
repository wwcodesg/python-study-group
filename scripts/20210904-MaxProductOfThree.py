# Solution to problem:
# https://app.codility.com/programmers/lessons/6-sorting/max_product_of_three/
# Session reports:
# https://app.codility.com/demo/results/trainingJSYPFJ-ED3/ # 60%
# https://app.codility.com/demo/results/trainingXGCDAV-CKA/ # 100%

def solution(A):
    if len(A) == 3:
        return A[0] * A[1] * A[2]

    tmp_A = A.copy()

    p = tmp_A.pop(tmp_A.index(max(tmp_A)))
    q = tmp_A.pop(tmp_A.index(max(tmp_A)))
    r = tmp_A.pop(tmp_A.index(max(tmp_A)))

    maximum = p*q*r

    q = A.pop(A.index(min(A)))
    r = A.pop(A.index(min(A)))
    if p*q*r > maximum:
        maximum = p*q*r

    return maximum
