def factorial(n: int) -> int:
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(7))

# 1.	Fibonacci Sequence: Define a function to calculate the nth number in the Fibonacci sequence.
# 2.	String Reversal: Write a recursive function to reverse a string. For example, given the input “hello,” the function should return “olleh.”
# 3.	Sum of Numbers: Define a recursive function to calculate the sum of all integers from 1 to n.
# 4.	Greatest Common Divisor (GCD): Write a recursive function to find the greatest common divisor of two integers.
# 5.	Power Calculation: Write a recursive function to calculate x raised to the power of n.
# 6.	Binary Conversion: Write a recursive function to convert an integer into its binary representation.
# 7.	Maximum in a List: Define a recursive function to find the maximum value in a list.
# 8.	Combinations (n Choose k): Write a recursive function to calculate the combination C(n, k), which is the number of ways to choose k elements from a set of n elements.
# 9.	Digit Reversal: Define a recursive function to reverse the digits of an integer. For example, given the input 12345, the function should return 54321.
# 10.	Digit Sum: Write a recursive function to calculate the sum of the digits of an integer. For example, given the input 123, the function should return 1 + 2 + 3 = 6.