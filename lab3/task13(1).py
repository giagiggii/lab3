a=input().split()
sum=0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            sum+= 1
print(sum)