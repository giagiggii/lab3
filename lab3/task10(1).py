a=input().split()
max=a.index(max(a))
min=a.index(min(a))
a[max],a[min] = a[min],a[max]
print(' '.join(str(i) for i in a))