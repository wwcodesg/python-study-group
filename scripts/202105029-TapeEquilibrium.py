# Solution to problem:
# https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/
# Session reports:
# https://app.codility.com/demo/results/trainingMGHAZG-7T3/  # 84%
# https://app.codility.com/demo/results/training6CN4XN-NYE/  # 92%
# https://app.codility.com/demo/results/trainingYRDKY9-BNT/  # 100%

def solution(A):
    if(len(A)==1):
        return 0
    elif(len(A)==2):
        return abs(A[0] - A[1])
        
    sumA = A[0]
    sumB = sum(A[1:])
    min_diff = abs(sumA-sumB)

    for i in range(1, len(A)-1):
        sumA += A[i]
        sumB -= A[i]
        tmp_diff = abs(sumA-sumB)
        if tmp_diff < min_diff:
            min_diff = tmp_diff

    return min_diff