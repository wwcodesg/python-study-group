# Solution to problem:
# https://app.codility.com/programmers/lessons/5-prefix_sums/genomic_range_query/
# Session reports:
# https://app.codility.com/demo/results/trainingD8SWK8-YRB/ # 62%
# https://app.codility.com/demo/results/trainingFPFX8S-A4N/ # 62%
# https://app.codility.com/demo/results/trainingTCW2Y7-W4D/ # 62%

import math

def solution(A, B, K):
    dna = {"A":1, "C":2,  "G":3, "T":4}

    ans = [min(set(S[p:q+1])) for p, q in zip(P,Q)]

    ret = [dna[letter] for letter in ans]
    
    return ret
