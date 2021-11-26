# Solution to:
# https://app.codility.com/programmers/lessons/7-stacks_and_queues/fish/
# Session report:
# https://app.codility.com/demo/results/trainingQ54U52-N4D/ # 37%

from collections import deque

def solution(A, B):
    eaten = 0
    newB = deque(B)
    index = 0
    prev_dir_1 = False
    downstream_idx = -1

    while(len(newB)):
        fish_dir = newB.popleft()

        if fish_dir == 0:
            if prev_dir_1:
                eaten += 1

                if downstream_idx >= 0:
                    if A[downstream_idx] < A[index]:
                        prev_dir_1 = False
        else:
            prev_dir_1 = True
            downstream_idx = index

        index += 1

    return len(A) - eaten
