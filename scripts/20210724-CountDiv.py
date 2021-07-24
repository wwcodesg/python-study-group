# Solution to problem:
# https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/
# Session reports:
# https://app.codility.com/demo/results/trainingEQYCJ8-2PQ/ # 50%
# https://app.codility.com/demo/results/trainingXPEJUN-9M5/ # 50%
# https://app.codility.com/demo/results/trainingSVABJV-6Z6/ #100%

import math

def solution(A, B, K):
    start = math.ceil(A / K)

    return len(range(start * K, B+1, K))

