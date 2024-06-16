#i/p 48 18
#o/p 6
x=int(input())
y=int(input())
while y>0:
    if x<y:
        temp=x
        x=y
        y=temp
    t=x-y
    x=y
    y=t
print(x)