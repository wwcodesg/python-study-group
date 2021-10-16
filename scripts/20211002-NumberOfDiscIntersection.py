# Solution to:
# https://app.codility.com/programmers/lessons/6-sorting/number_of_disc_intersections/
# Session report:
# https://app.codility.com/demo/results/trainingMMFFS9-YD7/ # 50%
# https://app.codility.com/demo/results/trainingYB5YXB-BDN/ # 56%
# https://app.codility.com/demo/results/trainingTRKYR9-A5G/ # 62%
# 2021-10-04 :-
#  https://app.codility.com/demo/results/training994UGY-QS3/ # 87%
#  https://app.codility.com/demo/results/trainingBHBZRD-H6C/ # 93%

def solution(A):
    intersects = 0
    size = len(A)
    discs = {}
    start = 0

    for center, radius in enumerate(A):
        # positive  radius
        additional = min(size-center-1, radius)
        intersects += additional
        
        # get start index of current disc
        if center - radius > 0:
            start = center - radius
        else:
            start =  0
        
        # negative radius
        additional = 0
        for key in range(start,center):
            if key in discs:
                additional += discs[key]
        
        intersects += additional
        if intersects > 10000000:
            return -1
        
        # add the disc's radius to an array
        key = center + radius
        if key in discs:
            discs[key] += 1
        else:
            discs[key] = 1

    return intersects