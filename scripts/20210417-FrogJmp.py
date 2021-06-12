# Solution to problem:
# https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/
# Session report:
# https://app.codility.com/demo/results/trainingX68QYP-MWE/

def solution(X, Y, D):
    # extreme case
    if X == Y:
        return 0

    gap = Y - X 
    jumps = int(gap / D) # get int instead of float

    if jumps * D == gap: # check if we have reached our destination
        return jumps 
    else:
        return jumps + 1