#i/p 8
#o/p 6713

#iteration
n = int(input())
x = [1,1]
for i in range(2,n+1):
    ans = (x[i-1]+7*x[i-2]+i//4)%(10**9+7)
    x.append(ans)
print(x[n])
#recursion
def fel(n):
    if n==0:
        return 1
    if n==1:
        return 1
x=[1,1]
for i in range(2,n+1):
    ans=(x[i-1]**2+(i-2)**2)%47
    x.append(ans)
print(x[n])