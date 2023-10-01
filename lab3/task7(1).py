a=input().split()
x = int(input())
pos = 0
while pos<len(a) and int(a[pos])>= x:
    pos += 1
print(pos + 1)