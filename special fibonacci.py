def sfib(n):
    if n==0:
        return 1
    if n==1:
        return 1
    return (sfib(n-1)**2 + (n-2)**2)%47
print(sfib(6))