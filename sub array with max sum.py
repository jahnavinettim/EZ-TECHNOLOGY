#2 4 6 -13 9 8 2
a=list(map(int,input().split())) #cadense algorithm
c_sum=0
mx_sum=0
for i in a:
   c_sum +=i
   if c_sum<0:
       c_sum=0
   if c_sum>mx_sum:
       mx_sum=c_sum
print(mx_sum)