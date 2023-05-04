def partitions(n):
    if n==0:
        return [[1]]
    return [[n]] + [[n-j]+p for j in range(1,n) for p in partitions(j) if n-j>=max(p)]

print(partitions(5))