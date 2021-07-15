# Solution to problem:
# https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/
# Session reports:
# https://app.codility.com/demo/results/trainingX76AA2-MPZ/ # 100%

def solution(A):
    set_array = set(A)
    size = len(A)
    if len(set_array) != size:
        return 0

    for i in range(1,size+1):
        if not i in set_array:
            return 0
    return 1

# https://app.codility.com/demo/results/training4SMMND-EYV/ # 100%

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    set_array = set(A)

    # Expected Result:
    permutation = set(range(1,len(A)+1))

    difference = len(set_array ^ permutation)
    
    if difference == 0:
        return 1
    
    return 0