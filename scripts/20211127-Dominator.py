# Solution to:
# https://app.codility.com/programmers/lessons/8-leader/dominator/
# Session report:
# https://app.codility.com/demo/results/trainingPNZTQE-QBJ/ # 100%
# https://app.codility.com/demo/results/trainingMZ6UZD-PJS/ # 66%

import collections

def solution(A):
    if len(A) == 0:
        return -1

    counts = collections.Counter(A)

    tmp_list = counts.most_common( 1 )

    if tmp_list[0][1] > (len(A)/2):
        return A.index(tmp_list[0][0])
    else:
        return -1
