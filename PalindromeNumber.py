def is_palindrome(n):
    n = str(n)
    if n == n[::-1]:
        return True
    else:
        return False
    
print(is_palindrome(12321))