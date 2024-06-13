
'''
def count_return_to_origin(A):
    position=0
    return_count=0
    for move in A:
        position +=move
        if position ==0:
            return_count +=0
    return return_count
A=[1,-1,1,-1,1]
print(count_return_to_origin(A))
---------------------------------------------------
def ans():
step=int(input())
a=list(map(int,input().split()))
    sp=0
    ans=0
    for i in a:
        sp=sp+i
        if sp==0:
            ans=ans+1
print(ans)
------------------------------------------------------
def choclates_reminder(A):
    total_choclates=sum(A)
    return total_choclates
A=[10,20,30]
print(choclates_reminder(A))
------------------------------------------------------
CHOCLATE JAR

jars=list(map(int,input().split()))
n=int(input())
a=0
for i in jars:
    a=a+(i//3)
    print(a)
    if i%3!=0:
        a=a+1
    else:
        a=a+0
print(a)
-----------------------------------------------------
DOG 

def dog_to_human_years(dog_years):
    human_years=dog_years*7
    return human_years
N=4
print(dog_to_human_years(N))
-----------------------------------------------------
MAX

probs=int(input())
tot=int(input())
c=0
s=0
rt=4*60 - tot
for i in range(1,probs+1):
    s=s+5*i
    if s>rt:
        break
    c=c+1
print(c)
----------------------------------------------------

inp1=int(input())
inp2=int(input())
arr=list(map(int,input().split()))
mx=-1
for i in range(0,len(arr)-inp2+1):
    temp=arr[i:i+inp2]
    k,s=1,0
for j in temp:
    s+=(j*k)
    k +=1
    if s>mx:
        mx=s
print(mx)
------------------------------------------------------------
SPACE COUNTER

s=input()
c=0
for i in s:
    if i==" ":
        c=c+1
print(c)
h=s.split()
print(h)
print(len(h)-1)
-----------------------------------------------------------
ENCODE THE NUMBER
167 I/P
13649 O/P

n=167
def sod(n):
    c=0
    while n>0:
        c=c+1
        n=n//10
        return c
def rev(n):
    ans=0
    while n>0:
        digit=n%10
        sq=digit**2
        sod_sq=sod(sq)
        ans=ans*(10**sod_sq)+sq
        n=n//10
    return ans
print(rev(n))
ans=rev(n)
def rev2(n):
    ans2=0
    while n>0:
        digit=n%10
        ans2=ans2*10+digit
        n=n//10
    return ans2
print(rev2(ans))
--------------------------------------------------
 
a=list(map(int,input().split()))
maxie=-1
s=0
for i in a:
    s=s+i
    if s>maxie:
        max=s
print(maxie)
----------------------------------------------------
'''