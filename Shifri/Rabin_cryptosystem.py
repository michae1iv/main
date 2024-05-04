import random
from math_functions import ReverseEuclideanAlgorithm, EuclideanAlgorithm
from prime_number_gen import PrimeNumberGenerator

class Rabin:
    def __init__(self, min_size):
        self.key_min_size = min_size
        self.p = 0
        self.q = 0
        self.m = 0
        self.public_key = 0
        self.private_key = []

    def CreateKeys(self):
        generator = PrimeNumberGenerator(self.key_min_size)
        while self.p == self.q:
            while self.p % 4 != 3:
                self.p, self.q = generator.generate_p_q()
            while self.q % 4 != 3:
                temp, self.q = generator.generate_p_q()
        self.m = self.p * self.q
        if self.p > self.q:
            self.private_key = [self.p, self.q]
        else:
            self.private_key = [self.q, self.p]
        self.public_key = self.m
        print('закрытый ключ: ', self.private_key)
        print('открытый ключ: ', self.public_key)

    def encrypt_message(self, message):
        encrypted_message = ''
        for char in message:
            m = ord(char)
            encrypted_message += str(pow(m, 2, self.public_key)) + ' '
        encrypted_message = encrypted_message[:-1]
        return encrypted_message

    def decrypt_message(self, encrypted_message):
        decrypted_message = ''
        encrypted = encrypted_message.split(' ')
        encrypted = [int(x) for x in encrypted]
        for number in encrypted:
            m_p = pow(number, (self.private_key[0] + 1) // 4, self.private_key[0])
            m_q = pow(number, (self.private_key[1] + 1) // 4, self.private_key[1])
            y_p, y_q = ReverseEuclideanAlgorithm(self.private_key[0], self.private_key[1])
            r1 = (y_p * self.private_key[0] * m_q + y_q * self.private_key[1] * m_p) % self.public_key
            r2 = self.public_key - r1
            r3 = (y_p * self.private_key[0] * m_q - y_q * self.private_key[1] * m_p) % self.public_key
            r4 = self.public_key - r3
            candidates = [r1, r2, r3, r4]
            decrypted_message += chr(min(candidates))
        return decrypted_message


if __name__ == '__main__':
    rabin_process = Rabin(50)
    rabin_process.CreateKeys()
    message = input('Введите сообщение: ')
    message = rabin_process.encrypt_message(message)
    print(message)
    print(rabin_process.decrypt_message(message))




