#10 3 5
n=10
a=3
b=5
a1=n//a
b1=n//b
c=0
for i in range(a1+1):
    for j in range(b1+1):
        if i*a+j*b<10:
            c+=1
print(c)