# Solution to problem:
# https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/

def solution(A, K):
    # Check for edge cases:
    if len(A) == 0 or K == 0 or K == len(A):
        return A
    
    # Remove need for extra rotations
    index = K % len(A)

    # For cyclic rotation of array, 
    # we count the number of elements from the back.
    split_at = len(A) - index

    # Split array
    front_array = A[:split_at]
    back_array = A[split_at:]

    # Swap the order of the two split arrays
    return back_array + front_array