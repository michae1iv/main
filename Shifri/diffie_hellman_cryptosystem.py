from cipher import encrypt_ceaser
from prime_number_gen import PrimeNumberGenerator


class Diffie_Hellman_client():
    def __init__(self, name):
        self.client_name = name
        self.public_key = 0                 # Открытый ключ клиента
        self.private_key = 0                # Закрытый ключ клиента
        self.p_local = 0                    # Часть p shared_key
        self.g_local = 0                    # Часть g shared_key
        self.intermediate_key = 0           # Промежуточный ключ
        self.foreign_intermediate_key = 0   # Промежуточный ключ другого клиента
        self.shared_secret_key = 0          # Конечный закрытый ключ

    def generate_keys(self):
        generator = PrimeNumberGenerator(50)
        self.public_key, self.private_key = generator.generate_p_q()

    def send_pubkey(self):
        return self.public_key

    def get_full_pubkey(self, p, g):
        self.p_local = p
        self.g_local = g

        self.init_intermediate_key()

    def init_intermediate_key(self):
        self.intermediate_key = pow(self.g_local, self.private_key, self.p_local)

    def send_intermediate_key(self):
        return self.intermediate_key
    
    def get_foreign_intermediate_key(self, foreign_key):
        self.foreign_intermediate_key = foreign_key
        self.create_shared_secret_key()

    def create_shared_secret_key(self):
        self.shared_secret_key = pow(self.foreign_intermediate_key, self.private_key, self.p_local)
        print(self.shared_secret_key)

    def send_message(self):
        message = 'hello my name is ' + self.client_name
        encrypted_message = encrypt_ceaser(message, self.shared_secret_key)
        print(self.client_name + ' отправил сообщение: ' + encrypted_message)
        return encrypted_message

    def get_message(self, message):
        decrypted_message = encrypt_ceaser(message, -self.shared_secret_key)
        print(self.client_name + ' получил сообщение: ' + decrypted_message)

if __name__ == '__main__':
    Client1 = Diffie_Hellman_client('Susen')
    Client2 = Diffie_Hellman_client('Paul')
    Client1.generate_keys()
    Client2.generate_keys()

    pubkey1 = Client1.send_pubkey()
    pubkey2 = Client2.send_pubkey()
    Client1.get_full_pubkey(pubkey1, pubkey2)
    Client2.get_full_pubkey(pubkey1, pubkey2)

    int_key1 = Client1.send_intermediate_key()
    int_key2 = Client2.send_intermediate_key()

    Client1.get_foreign_intermediate_key(int_key2)
    Client2.get_foreign_intermediate_key(int_key1)

    message = Client1.send_message()
    Client2.get_message(message)

    message = Client2.send_message()
    Client1.get_message(message)
