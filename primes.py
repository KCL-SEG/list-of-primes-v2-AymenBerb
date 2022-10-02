"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise(ValueError('test'))
    list = []
    i = 0
    while len(list) != number_of_primes:
        if isPrime(i):
            list.append(i)
        i += 1
    return list

def isPrime(num):
    # prime numbers are greater than 1
    if num > 1:
        flag = True
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to False
                flag = False
                # break out of loop
                break
        return flag
    else:
        return False