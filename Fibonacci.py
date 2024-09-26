#Fibonacci Sequence: Complete the function named fibonacci such that it returns the n-th number in the Fibonacci sequence. 
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
'''
可以使用動態規劃或記憶化技術來避免重複計算
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

print(fibonacci(10))
'''