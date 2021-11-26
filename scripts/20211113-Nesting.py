# Solution to:
# https://app.codility.com/programmers/lessons/7-stacks_and_queues/nesting/  
# Session report:
# https://app.codility.com/demo/results/trainingBPYZY4-CD9/ # 100%

def solution(S):
    stack = []
    for char in S:
        if char == '(':
            stack.append(char)
        else:
            if len(stack):
                stack.pop()
            else:
                return 0
    
    if len(stack) == 0:
        return 1
    else:
        return 0
