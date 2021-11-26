# Solution to:
# https://app.codility.com/programmers/lessons/7-stacks_and_queues/stone_wall/  
# Session report:
# https://app.codility.com/demo/results/trainingHTJWEZ-NPJ/ # 85%
# https://app.codility.com/demo/results/training225EQW-URW/ # 28%

def update_height_memory(previous_height, current_height):    
    updated_height = previous_height.copy()    
    
    for h in reversed(previous_height):    
        if current_height < h:    
            updated_height.pop()      
        else:    
            break                                   
    updated_height.append(current_height)       
    return updated_height           

def solution(H):     
    block_cnt = 0    
    if len(H) == 0:    
        return 0                              
    else:    
        previous_height = []    
        for i, height in enumerate(H):    
            if i == 0:    
                previous_height.append(H[0])                                     
                block_cnt = 1    
            else:    
                if len(previous_height) == 0:          
                    block_cnt += 1                     
                    previous_height.append(height)     
                elif height == previous_height[-1]:    
                    continue    
                elif height > previous_height[-1]:    
                    block_cnt += 1    
                    previous_height.append(height)    
                else:    
                    if height not in previous_height:
                        block_cnt += 1    
                    previous_height = update_height_memory(previous_height, height)    
    return block_cnt  
