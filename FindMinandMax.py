def find_min_and_max(numbers):
    min = numbers[0]
    max = 0
    for i in numbers:
        if i > max:
            max = i
        if i < min:
            min = i
    print(max, min)

find_min_and_max([2,800,4,6,0,100])