# Solution to problem:
# https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/
# Session report:
# https://app.codility.com/demo/results/trainingPEZGJA-J6Z/

def solution(A):
    val_dict = {} # empty dictionary
    
    for value in A:
        str_val = str(value) # convert to string to use as key
        
        if str_val in val_dict:
            val_dict.pop(str_val) # value already exist, therefore it is even. Remove
        else:
            val_dict[str_val] = value # value hasn't been added, assume odd. Add {'key':value}
    
    value = list(val_dict.values())[0]

    return value