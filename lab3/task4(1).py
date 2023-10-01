a = input().split()
for i in range(1,len(a)):
   if int(a[i - 1])*int(a[i])>0:
        print(a[i-1],a[i])
        break