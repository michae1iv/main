import random
from math_functions import miller_rabin, ReverseEuclideanAlgorithm, EuclideanAlgorithm
from prime_number_gen import PrimeNumberGenerator

class RSA:
    def __init__(self, key_min_size):
        generator = PrimeNumberGenerator(key_min_size)
        self.p, self.q = generator.generate_p_q()
        self.m = self.p * self.q
        self.eiller = (self.p - 1) * (self.q - 1)
        self.public_key = []
        self.private_key = 0

    def change_pq(self, new_p, new_q):
        if miller_rabin(new_p) and miller_rabin(new_q):
            self.p = new_p
            self.q = new_q
            self.eiller = (new_p - 1) * (new_q - 1)
            self.m = self.p * self.q
            self.CreateKeys()
            return True
        else:
            return False

    def CreateKeys(self):
        e = 0
        while True:
            e = random.randrange(self.eiller - 1)
            if (EuclideanAlgorithm(max(self.p - 1, e), min(self.p - 1, e))
                    == EuclideanAlgorithm(max(self.q - 1, e), min(self.q - 1, e)) == 1):
                self.public_key = [e, self.m]
                break
        self.private_key = ReverseEuclideanAlgorithm(self.eiller, e)[1] % self.eiller

        print('закрытый ключ: ', self.private_key)
        print('открытый ключ: ', self.public_key)

    def encrypt_message(self, message):
        encrypted_message = ''
        for char in message:
            x = ord(char)
            encrypted_message += str(pow(x, self.public_key[0], self.public_key[1])) + ' '
        encrypted_message = encrypted_message[:-1]
        return encrypted_message

    def decrypt_message(self, encrypted_message):
        decrypted_message = ''
        encrypted = encrypted_message.split(' ')
        encrypted = [int(x) for x in encrypted]
        for number in encrypted:
            char = chr(pow(number, self.private_key, self.public_key[1]))
            decrypted_message += char
        return decrypted_message


if __name__ == '__main__':
    rsa_process = RSA(100)
    rsa_process.CreateKeys()
    user_message = input('Введите сообщение которое хотите зашифровать: ')
    user_message = rsa_process.encrypt_message(user_message)
    print(user_message)
    print(rsa_process.decrypt_message(user_message))

