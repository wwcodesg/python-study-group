# Solution to problem:
# https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/
# Session reports:
# https://app.codility.com/demo/results/trainingHRBZS5-283/ # 100%

def solution(A):
    array_set = set(A)

    i = 1
    while(i < 1000001):
        if i in array_set:
            i += 1
        else:
            return i

    return 1000001
