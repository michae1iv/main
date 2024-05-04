from prime_number_gen import PrimeNumberGenerator


if __name__ == "__main__":
    generator = PrimeNumberGenerator(500)
    numbers = []
    for i in range(1000):
        number = generator.generate_prime()
        numbers.append(number)
        print(number)
