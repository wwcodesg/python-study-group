# Solution to problem:
# https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/
# Session reports:
# https://app.codility.com/demo/results/trainingNU6J38-JSM/ # 100%

def solution(X, A):
    flags = [False] * X
    steps = 0

    for index, element in enumerate(A):
        flags[element-1] = True
        while flags[steps]:
            steps += 1
            if steps == X:
                return index
    
    return -1