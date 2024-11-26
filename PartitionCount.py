# Write a function that counts the number of ways you can partition n objects using parts up to m (assuming m >= 0)
def partition_count(n,m):
    if m == 0 or n < 0:
        return 0
    if n == 0:
        return 1
    else:
        return partition_count(n-m,m) + partition_count(n,m-1)
    
print(partition_count(7,3))