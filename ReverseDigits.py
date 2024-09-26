# Solution 1
def reverse_number(n):
    answer = 0
    while n > 0:
        answer = answer*10 + n%10
        n = n//10
    print(answer)

# Solution 2
def reverse_number(n):
    answer = 0
    i = n
    len = 0
    while i > 1:
        i = i/10
        len += 1
    print(len)
    while n > 1:
        len = len - 1
        m = int(n % 10)
        answer += m * 10**len
        n = n//10
        
    print(answer)

reverse_number(54321)

