import sys

from sympy import isprime, primerange
import random

from prime_number_gen import PrimeNumberGenerator


def generate_large_prime():
    while True:
        num = int('1' + ''.join(random.choice('0123456789') for _ in range(9999)))
        if isprime(num):
            return num



if __name__ == "__main__":
    sys.set_int_max_str_digits(99999999)
    generator = PrimeNumberGenerator(10000)
    number = generator.generate_prime()
    print(number)
