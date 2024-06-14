def encrypt(x):
    max_digit=0
    original =x
    while x>0:
        digit =x%10
        if digit >max_digit:
            max_digit=digit
        x//=10
    result=0
    multiplier=1
    while original>0:
        result += max_digit * multiplier
        original//=10
        multiplier *=10
    return result
def sum_of_encrypted_elements(nums):
    total_sum=0
    for num in nums:
        total_sum +=encrypt(num)
    return total_sum
nums=[1,2,3]
print(sum_of_encrypted_elements(nums))
nums=[10,21,31]
print(sum_of_encrypted_elements(nums))
