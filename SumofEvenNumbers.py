def sum_of_even_numbers(numbers):
    sum = 0
    for i in numbers:
        if i % 2 == 0:
            sum += i
    print(sum)

sum_of_even_numbers([1,2,3,4,5,6,7,8])