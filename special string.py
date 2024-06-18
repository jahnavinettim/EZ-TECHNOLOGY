def minimum_total_ascii_distance(A, S):
    if all(char in S for char in A):
        return 0   
    total_distance = 0
    for char_A in A:
        min_distance = float('inf')
        for char_S in S:
            distance = abs(ord(char_A) - ord(char_S))
            if distance < min_distance:
                min_distance = distance
        total_distance += min_distance  
    return total_distance
A="abcd"
S="xyz"
print(minimum_total_ascii_distance(A, S))