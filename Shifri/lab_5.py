from prime_number_gen import PrimeNumberGenerator
from math_functions import fast_modular_exponentiation

if __name__ == "__main__":
    generator = PrimeNumberGenerator(50)
    p = generator.generate_single_prime()
    print(p)
    a = int(input('Введите число a, которое будет возводиться в степень (2017): '))
    n = int(input('Введите число n последовательности (примерно 2000): '))
    for i in range(n - 1):
        a = fast_modular_exponentiation(a, a, p)
    print(a)
