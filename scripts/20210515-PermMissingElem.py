# Solution to problem:
# https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/
# Session reports:
# https://app.codility.com/demo/results/trainingTFKDZP-VME/  # 60%
# https://app.codility.com/demo/results/trainingHRNUXS-R2E/  # 100%

def solution(A):
    N = len(A)+1
    a_set = set(A)

    for elem in range(1, N+1):
        if not elem in a_set:  # searching in set is alot faster.
            return elem