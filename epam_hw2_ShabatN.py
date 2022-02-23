# Task 1  For a given integer n calculate the value which is equal to a:
# squared number, if its value is strictly positive;
# modulus of a number, if its value is strictly negative;
# zero, if the integer n is zero.
# Example: n=4 result= 16; n=-5 result= 5; n=0 result=0

n = float(input("Please, enter n for calculation:"))
if n > 0:
    print((n**2))
elif n < 0:
    print(abs(n))
else:
    print('0')
print('------------ TASK2')
# Task 2.
# Find the maximum integer, that can be obtained by permutation of numbers of an arbitrary three-digit
# positive integer n (100<=n<=999).  Example: n =165 result = 651

n = input("Please, enter n for finding the maximum:")
n = (sorted(n, reverse=True))
print([int(x) for x in n])


print('------------ TASK3')
# Task 3.
# For a positive integer n calculate the result value, which is equal to the sum of the odd numbers of n.
# Example: n = 1234 result = 4, n = 246 result = 0

n = input("Please, enter n for calculation the sum of odd numbers:")
count_odd = 0
for i in n:
    if int(i) % 2 != 0:
        count_odd+=1
print('The sum of odd numbers:', count_odd)

print('------------ TASK4')
# Task 4. For a positive integer n calculate the result value, which is equal to the sum of the “1” in the
# binary representation of n.  Example: n = 1410 = 11102 result = 3, n = 12810 = 1000 00002 result = 1

n = input("Please, enter n for calculation of '1s': ")
n = int(n)
n = (bin(n) [2:])
print(n)
count_1_in_bin_format = 0
for i in n:
    if int(i) == 1:
        count_1_in_bin_format+=1
print('The count of "1" on binary format is:', count_1_in_bin_format)

print('------------ TASK5')
# Task 5. Create function Fibonacci for a positive integer n, calculate the result value, which is equal to the sum
# of the first n Fibonacci numbers.  Note. Fibonacci numbers are a series of numbers in which each next number is equal
# to the sum of the two preceding ones: 0, 1, 1, 2, 3, 5, 8, 13... (F0=0, F1=F2=1, then F(n)=F(n-1)+F(n-2) for n>2)
#  Example: n=8 result=33,  n = 11 result = 143

def fibinocci(n):
    if n == 1 or n == 2:
        return 1
    return fibinocci(n - 1) + fibinocci(n - 2)

x = fibinocci(8)
print('sum_of_n_Fibonacci', x)

print('------------ TASK6')
