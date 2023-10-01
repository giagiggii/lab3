a=input().split()
sum=1
for i in range(1,len(a)):
    if a[i - 1]!=a[i]:
        sum+= 1
print(sum)