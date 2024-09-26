def is_Prime(numbers):
    is_prime = True
    for i in range(2,int(numbers/2+1)):
        if numbers % i == 0:
            is_prime = False
            break
        else: 
            pass
    return is_prime

print(is_Prime(77))
