a=input().split()
max=a[0]
ind=0
for i in range(1,len(a)):
    if(a[i]>max):
        max=a[i]
        ind=i
print (max, ind)