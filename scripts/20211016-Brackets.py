# Solution to:
# https://app.codility.com/programmers/lessons/7-stacks_and_queues/brackets/
# Session report:
# https://app.codility.com/demo/results/trainingMMY4EQ-QDC/ # 100%

def solution(S):
    # write your code in Python 3.6
    stack = []
    open_bracs = ['{', '[', '(']
    close_bracs = ['}', ']', ')']

    for char in S:
        if char in open_bracs:
            stack.append(char)
        elif char in close_bracs:
            if len(stack) == 0:
                return 0
            else:
                check_char = stack.pop()

                try:
                    if open_bracs.index(check_char) != close_bracs.index(char):
                        return 0
                    else:
                        continue

                except ValueError:
                    return 0
    if len(stack) == 0:
        return 1
    else:
        return 0
