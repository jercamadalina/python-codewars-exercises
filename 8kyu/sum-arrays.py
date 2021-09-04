def sum_array(a):
    return sum(a)


print(sum_array([]), 0)
print(sum_array([1, 2, 3]), 6)
print(sum_array([1.1, 2.2, 3.3]), 6.6)
print(sum_array([4, 5, 6]), 15)
print(sum_array(range(101)), 5050)


'''
# Details
    Write a method sum (sum_array in python, sumarray in julia, SumArray in C#) that takes an array of
    numbers and returns the sum of the numbers. These may be integers or decimals for Ruby and any
    instance of Num for Haskell. The numbers can also be negative. If the array does not contain any
    numbers then you should return 0.
        Examples
        print sum_array([1 2 3])
        > 6
        print sum_array([])
        > 0
    Assumptions
    You can assume that you are only given numbers.
    You cannot assume the size of the array.
    You can assume that you do get an array and if the array is empty, return 0.
'''
