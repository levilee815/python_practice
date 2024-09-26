def max_digit(n):
    max = 0
    while n > 1:
        i = n % 10
        if i > max:
            max = i
        n = n // 10
    return max
print(max_digit(88219))