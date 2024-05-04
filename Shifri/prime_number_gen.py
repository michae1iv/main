import random
from math_functions import miller_rabin

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
        f = self.low_simple_numbers[random.randrange(len(self.low_simple_numbers) - 1)]
        while len(str(f)) <= self.key_length:
            r = random.randrange(4 * f + 4)
            n = f * r + 1
            if miller_rabin(n):
                for _ in range(10000):
                    a = random.randrange(2, r*100)
                    if pow(a, n - 1, n) == 1 and pow(a, r, n) != 1:
                        f = n
                        break
        return f

    def generate_prime(self):
        while True:
            num = int('1' + ''.join(random.choice('0123456789') for _ in range(self.key_length - 1)))
            if miller_rabin(num):
                return num
