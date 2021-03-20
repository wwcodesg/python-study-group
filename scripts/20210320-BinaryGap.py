def solution(N):
    # write your code in Python 3.6
    binary = bin(N)
    max = 0
    startFlag = False
    count = 0

    for item in binary[2:]:
        if not startFlag:
            if item == '1':
                startFlag = True
        else:
            if item == '1':
                if count > max:
                    max = count
                count = 0
            else:
                count += 1

    return max