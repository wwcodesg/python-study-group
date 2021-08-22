# Solution to problem:
# https://app.codility.com/programmers/lessons/5-prefix_sums/min_avg_two_slice/
# Session reports:
# https://app.codility.com/demo/results/training2EPQM7-W2Y/ # 50%
# https://app.codility.com/demo/results/trainingJWEQJQ-HX5/ # 60%

def solution(A):
    p = range(len(A)-1)
    q = range(1,len(A))

    # first case
    min_ave = sum(  A[p[0]:q[0]+1]  ) / (q[0] - p[0] + 1)
    minimal_idx = 0

    # loop through all permutation of p < q
    for item_p in p:
        last_sum = A[item_p]

        for item_q in q[item_p:]:
            last_sum  = last_sum + A[item_q]

            temp_min_ave = last_sum / (item_q - item_p + 1)
            
            if temp_min_ave < min_ave:
                minimal_idx = item_p
                min_ave = temp_min_ave

    return minimal_idx
