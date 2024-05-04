import sys

from sympy import isprime, primerange
import random

def generate_large_prime():
    while True:
        num = int('1' + ''.join(random.choice('0123456789') for _ in range(9999)))
        if isprime(num):
            return num



if __name__ == "__main__":
    sys.set_int_max_str_digits(10001)
    prime_number = generate_large_prime()
    print("Простое число из 1000 знаков:")
    print(prime_number)
