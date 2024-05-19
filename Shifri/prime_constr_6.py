from prime_number_gen import PrimeNumberGenerator
from tqdm import tqdm
from math_functions import miller_rabin


if __name__ == "__main__":
    generator = PrimeNumberGenerator(500)
    numbers = []
    for i in tqdm(range(1000)):
        number = generator.generate_prime()
        numbers.append(number)
        if miller_rabin(number):
            print(number)
