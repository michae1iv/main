import random
from math_functions import miller_rabin
from gmpy2 import mpz, f_div, mpfr


class PrimeNumberGenerator:
    def __init__(self, size):
        self.key_length = size
        self.low_simple_numbers = []
        with open('prime_numbers', "r", encoding='utf-8') as file:
            buff = file.read().split(' ')
            self.low_simple_numbers = [int(x) for x in buff]
            file.close()

    def generate_p_q(self): #Теорема Диемитко
        result = [0, 0]
        for i in range(2):
            f = self.low_simple_numbers[random.randrange(len(self.low_simple_numbers) - 1)]
            while len(str(f)) <= self.key_length:
                r = random.randrange(4 * f + 4)
                n = f * r + 1
                for _ in range(10):
                    a = random.randrange(2, r)
                    if pow(a, n - 1, n) == 1 and pow(a, r, n) != 1:
                        f = n
                        break
            result[i] = f
        return result

    def generate_single_prime(self):
        q = self.low_simple_numbers[random.randrange(len(self.low_simple_numbers) - 1)]
        n = 0
        while len(str(q)) <= self.key_length:
            r = 2 * random.randrange(2 * q + 2)
            n = q * r + 1
            if miller_rabin(n):
                for _ in range(1000000000):
                    a = random.randrange(2, n * 100)
                    if pow(a, n - 1, n) == 1 and pow(a, r, n) != 1:
                        q = n
                        break
        return q

    def generate_prime(self):
        start_prime = self.low_simple_numbers[random.randrange(len(self.low_simple_numbers) - 1)]
        dimension = self.key_length
        current_prime = mpz(start_prime)
        current_dimension = len(str(current_prime))
        while current_dimension < dimension:
            current_dimension = dimension
            repeat_flag = True
            u = 0
            n = 0
            p = current_prime
            while True:
                if repeat_flag:
                    repeat_flag = False
                    n = f_div(mpz(10 ** (current_dimension - 1)), mpz(current_prime)) + \
                        f_div(mpz(10 ** (current_dimension - 1) * mpfr(random.random())),
                              mpz(current_prime))
                    n = n + 1 if n.is_odd() else n
                    u = 0
                p = (n + u) * current_prime + 1
                if pow(2, p - 1, p) == 1 and pow(2, n + u, p) != 1:
                    repeat_flag = True
                    break
                else:
                    u += 2
            current_prime = p
            current_dimension = (len(str(current_prime)))
        return current_prime