from prime_number_gen import PrimeNumberGenerator
from math_functions import fast_modular_exponentiation

if __name__ == "__main__":
    generator = PrimeNumberGenerator(100)
    p = generator.generate_single_prime()
    print(p)
    a = int(input('Введите любое число, которое будет возводиться в степень: '))
    n = int(input('Введите степень числа a: '))
    output = pow(a, n, p)
    print(output)
    output = fast_modular_exponentiation(a, n, p)
    print(output)
