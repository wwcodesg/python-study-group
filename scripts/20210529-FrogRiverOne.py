# Solution to problem:
# https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/
# Session reports:
# https://app.codility.com/demo/results/trainingRDYA9V-PBE/  # 81%
# https://app.codility.com/demo/results/trainingMGWE58-SKF/  # 54%

def solution(X, A):
    flags = [False] * X
    
    for index, element in enumerate(A):
        flags[element-1] = True
        if(all(flags)):
            return index
    
    return -1