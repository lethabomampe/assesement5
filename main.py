from typing import List


def sum_numbers(nums: list[int]) -> int:
    """
    Takes a list of numbers and returns the result of:
    - Adding all positive numbers
    - Subtracting all negative numbers 

    Example:
        sum_numbers([2, -3, 5, -1]) → (2 + 5) - (3 + 1) = 3
    """
    pos = 0
    neg = 0
    for num in nums:
        if num >= 0:
            pos += int(num)
        elif num < 0:
            neg += int(num)
    
    return pos + neg

def is_anagram(str1: str, str2: str) -> bool:
    """
    Check if two strings are anagrams (ignoring case and spaces).
    
    Example:
        Input → str1 = "listen", str2 = "silent"
        Output → True
        
        Input → str1 = "hello", str2 = "world"
        Output → False
    """
    str1 = str1.lower().replace(' ', '')
    str2 = str2.lower().replace(' ', '')

    if sorted(str1) == sorted(str2):
        return True
    else:
        return False

def fibonacci_series(n_terms: int) -> List[int]:
    """
    Generate a Fibonacci series with n_terms.
    
    The series starts with 0, 1 and each subsequent term is the sum of the previous two.

    Example:
        Input → 10
        Output → [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    n = [0, 1]
    if n_terms <= 0:
        return []
    if n_terms == 1:
        return [0]
    if n_terms == 2:
        return n
    
    for x in range(2, n_terms):
        n1 = n[-2]
        n2 = n[-1]
        x = n1 + n2
        n.append(x)
    return n
    
    

def prime_factors(n: int) -> List[int]:
    """
    Return a list of all prime factors of a given number n.
    
    Example:
        Input → 84
        Output → [2, 2, 3, 7]
    """
    # check if the number in the n range can go in n...
    # if number can go through n check if it is a prime number...
    # if number is a prime number append it to a list called factors...
    # use floor division to get what is left of that...
    # get thet to go through a loop...
    # return factor list


def create_pyramid(n):
    """
    Returns a pyramid of '*' as a list of strings.

    Example:
        Input → 3
        Output →['  *  ', ' *** ', '*****']
    """
    pass

def create_number_triangle(n):
    """
    Returns a triangle of numbers as a list of strings.
    Example  :      
        Input → 3
        Output →    ['  1  ', ' 2 2 ', '3 3 3']
    """
    pass

def create_multiplication_square(n: int) -> List[str]:
    """
    Returns a multiplication square as a list of strings.
    Example:
        Input → 3
        Output → ['1 2 3', '2 4 6', '3 6 9']
    """



def create_diamond(n):
    """
    Returns a diamond shape as a list of strings.
    Example:
        Input → 3
        Output →    ['  *  ', ' *** ', '*****', ' *** ', '  *  ']
    """    
    pass

def create_pascals_triangle(n: int) -> List[str]:
    """
    Return Pascal's triangle of height n as a list of strings.
        Example:
        Input → 5
        Output → ['    1    ', '   1 1   ',    '  1 2 1  ', ' 1 3 3 1 ', '1 4 6 4 1']
    """
    pass



if __name__ == '__main__':
    pass