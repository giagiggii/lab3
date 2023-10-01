a = input().split()
sum=0
for i in range(1,len(a)-1):
   if a[i - 1] < a[i] > a[i + 1]:
        sum+=1
print(sum)