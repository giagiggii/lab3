a=input().split()
for i in range(len(a)):
    num=a.count(a[i])
    if num==1:
        print(a[i])