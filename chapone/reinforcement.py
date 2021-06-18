import re

# Write a short Python function, is_multiple(n, m),
# that takes two integer values and returns True if
# n is a multiple of m, that is, n = mi for some integer
# i, and False otherwise.
def is_multiple(n, m):
    if (m == 0):
        return False

    return (n % m == 0)


# Write a short Python function, is_even(k),
# that takes an integer value and returns
# True if k is even, and False otherwise.
# However, your function cannot use the
# multiplication, modulo, or division operators.
def is_even(k):
  k_string = str(k)

  even_num = re.compile('^.*[0,2,4,6,8]$')

  if (even_num.search(k_string)):
    return True
  else:
    return False


# Write a short Python function, minmax(data), that
# takes a sequence of one or more numbers, and returns
# the smallest and largest numbers, in the form of a
# tuple of length two. Do not use the built-in functions
# min or max in implementing your solution.
def minmax(data):
    if len(data):
        small = large = data[0]

        for data_element in data:
            if (data_element < small):
                small = data_element
            elif (data_element > large):
                large = data_element

        return (small, large)


    else:
        return data

# Write a short Python function that takes
# a positive integer n and returns the sum of the
# squares of all the positive integers smaller than n.
def sum_of_squares(limit):
    if (limit < 1):
        raise ValueError

    return sum(i*i for i in range(1, limit))


# Write a short Python function that takes a positive
# integer n and returns the sum of the squares of all
# the odd positive integers smaller than n.
def sum_of_odd_squares(limit):
    if (limit < 1):
        raise ValueError

    return sum(i*i for i in range(1, limit) if i%2==1)

