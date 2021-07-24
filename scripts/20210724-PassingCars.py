# Solution to problem:
# https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/
# Session reports:
# https://app.codility.com/demo/results/trainingE68DU6-P4F/ # 50%
# https://app.codility.com/demo/results/trainingDGV3DU-9JD/ # 50%
# https://app.codility.com/demo/results/trainingYR6G9U-NNK/ #100%

import math

def solution(A, B, K):
    passing = 0
    sumA = sum(A)

    for item in A:
        if item == 0:
            passing += sumA
        else:
            sumA -= 1
    
        if passing > 1000000000:
            return -1

    return passing
