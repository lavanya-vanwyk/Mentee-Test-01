import math 
def add_numbers(a, b):
    """
    Problem 1:
    Write a function that takes two numbers (a and b)
    and returns their sum.

    Example:
    >>> add_numbers(2, 3)
    5
    """
    return (a + b)


def is_even(n):
    """
    Problem 2:
    Return True if the given number 'n' is even, otherwise return False.

    Example:
    >>> is_even(4)
    True
    >>> is_even(5)
    False
    """
    if n % 2 == 0:
        return True
    else:
        return False


def count_vowels(word):
    """
    Problem 3:
    Write a function that counts how many vowels are in a given string.

    Vowels are: a, e, i, o, u (both uppercase and lowercase).

    Example:
    >>> count_vowels("Hello")
    2
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for c in word:
        if c.lower() in vowels:
            count += 1
    return count


def find_max(numbers):
    """
    Problem 4:
    Given a list of numbers, return the largest number.

    Example:
    >>> find_max([1, 4, 2, 10])
    10
    """
    return max(numbers)


def reverse_string(s):
    """
    Problem 5:
    Write a function that returns the reverse of the input string.

    Example:
    >>> reverse_string("cat")
    'tac'
    """
    return s[::-1]


def average(numbers):
    """
    Problem 6:
    Given a list of numbers, return their average.
    If the list is empty, return 0.

    Example:
    >>> average([2, 4, 6])
    4.0
    >>> average([])
    0
    """
    
    if numbers:
        average = sum(numbers)/len(numbers)
        return average
    else:
        return 0


def word_in_sentence(word, sentence):
    """
    Problem 7:
    Return True if the given word appears in the sentence, otherwise False.

    Example:
    >>> word_in_sentence("cat", "The cat is sleeping")
    True
    >>> word_in_sentence("dog", "The cat is sleeping")
    False
    """
    if word in sentence:
        return True
    else:
        return False


def factorial(n):
    """
    Problem 8:
    Write a function that returns the factorial of a non-negative integer n.
    The factorial of n (written as n!) is the product of all positive integers up to n.
    If n is 0, return 1.

    Example:
    >>> factorial(5)
    120
    >>> factorial(0)
    1
    """
    
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(1, n + 1):
            m = n
            m *= m * i
            print(m)
    return m


def remove_duplicates(numbers):
    """
    Problem 9:
    Given a list of numbers, return a new list with duplicates removed.
    The order of the first occurrence of each element should be preserved.

    Example:
    >>> remove_duplicates([1, 2, 2, 3, 1])
    [1, 2, 3]
    """
    unique_n = []
    for n in numbers:
        if n not in unique_n:
            unique_n.append(n)
    return unique_n


def fizzbuzz(n):
    """
    Problem 10:
    Write a function that returns a list of numbers from 1 to n,
    but replace:
    - multiples of 3 with "Fizz"
    - multiples of 5 with "Buzz"
    - multiples of both 3 and 5 with "FizzBuzz"

    Example:
    >>> fizzbuzz(5)
    [1, 2, 'Fizz', 4, 'Buzz']
    """
    l_nums = []
    count = 1
    while count < n + 1:
        # l_nums.append(count)
        if count % 3 == 0 and count % 5 == 0:
            l_nums.append("FizzBuzz")
            count += 1
        elif count % 3 == 0:
            l_nums.append("Fizz")
            count += 1
        elif count % 5 == 0:
            l_nums.append("Buzz")
            count += 1
        else:
            l_nums.append(count)
            count += 1
    return l_nums

factorial(5)