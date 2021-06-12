# Solution to problem:
# https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/
# Session reports:
# https://app.codility.com/demo/results/trainingG65YTG-HN4/ # 66%
# https://app.codility.com/demo/results/training23CVXN-8BC/ # 22%
# https://app.codility.com/demo/results/training8UWFDV-873/ # 88%
# https://app.codility.com/demo/results/training5V546G-RGW/ # 100%

def solution(N, A):
    array = [0] * N
    max = 0
    flag = False
    for k in A:
        if k <= N:
            array[k-1] += 1
            tmp = array[k-1]
            if tmp > max:
                max = tmp
                flag = True
        else:
            if flag:
                array = [max] * N
            else:
                flag = False
    return array