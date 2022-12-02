import math
from string import ascii_lowercase
import base64
from art import *


class CIPHER:
    def __init__(self, msg, shift):
        self.msg = msg
        self.shift = shift


class Input(CIPHER):
    def encrypt_input(self):
        if type == 1:
            msg = input("Enter your text to encrypt: ")
            super().__init__(msg.lower(), '')
        elif type == 2:
            with open("input.txt", 'r') as infile:
                temp = []
                for line in infile:
                    if line.startswith('#'):
                        continue
                    else:
                        temp.append(line.strip('\n'))
                        msg = temp[0]
                        super().__init__(msg.lower(), '')
        else:
            error()

    def decrypt_input(self):
        if type == 1:
            msg = input("Enter your cipher to decrypt: ")
            super().__init__(msg.lower(), '')
        elif type == 2:
            with open("input.txt", 'r') as infile:
                temp = []
                for line in infile:
                    if line.startswith('#'):
                        continue
                    else:
                        temp.append(line.strip('\n'))
                        msg = temp[0]
                        super().__init__(msg.lower(), '')
        else:
            error()

    def shift_input(self):
        if type == 1:
            shift = input("Enter the shift/key: ")
            super().__init__(self.msg, int(shift))
        elif type == 2:
            with open("input.txt", 'r') as infile:
                temp = []
                for line in infile:
                    if line.startswith('#'):
                        continue
                    else:
                        temp.append(line.strip('\n'))
                        shift = temp[1]
                        super().__init__(self.msg, int(shift))
        else:
            error()

    def encrypt(self):
        pass

    def decrypt(self):
        pass


class reverse(Input):
    def encrypt(self):
        self.encrypt_input()
        text = self.msg
        encrypted_cipher = ''
        i = len(text) - 1

        while i >= 0:
            encrypted_cipher += text[i]
            i -= 1
        return encrypted_cipher

    def decrypt(self):
        self.decrypt_input()
        text = self.msg
        decrypted_cipher = ''
        i = len(text) - 1

        while i >= 0:
            decrypted_cipher += text[i]
            i -= 1
        return decrypted_cipher


class ceaser(Input):
    def encrypt(self):
        self.encrypt_input()
        self.shift_input()
        text = self.msg
        key = self.shift
        encrypted_cipher = ''
        for char in text:
            if char != ' ':
                encrypted_cipher += chr((ord(char) + key - 97) % 26 + 97)
            else:
                encrypted_cipher += ' '
        return encrypted_cipher

    def decrypt(self):
        self.decrypt_input()
        self.shift_input()
        text = self.msg
        key = self.shift
        decrypted_cipher = ''
        for char in text:
            if char != ' ':
                for t1, t2 in enumerate(ascii_lowercase):
                    temp = (t1 + key) % 26
                    if (ord(char) - 97) == temp:
                        decrypted_cipher += t2
                    else:
                        continue
            else:
                decrypted_cipher += ' '
        return decrypted_cipher


class multiplication(CIPHER):

    def encrypt_multiplicative(self, key, cipher):
        cipher = cipher.lower()
        encrypted_cipher = ''
        for a in cipher:
            if a != ' ':
                temp = ((ord(a) - 97) * key) % 26
                encrypted_cipher += chr(temp + 97)
            else:
                encrypted_cipher += ' '
        return encrypted_cipher

    def decrypt_multiplicative(self, key, cipher):
        cipher = cipher.lower()
        decrypted_cipher = ''

        for a in cipher:
            if a != ' ':
                for t1, t2 in enumerate(ascii_lowercase):
                    temp = (t1 * key) % 26
                    if (ord(a) - 97) == temp:
                        decrypted_cipher += t2
                    else:
                        continue
            else:
                decrypted_cipher += ' '
        return decrypted_cipher


class affine(CIPHER):

    def affine(self):
        class Affine(object):
            DIE = 128
            KEY = (7, 3, 55)

            def __init__(self):
                pass

            def encryptChar(self, char):
                K1, K2, kI = self.KEY
                return chr((K1 * ord(char) + K2) % self.DIE)

            def encrypt(self, string):
                return "".join(map(self.encryptChar, string))

            def decryptChar(self, char):
                K1, K2, KI = self.KEY
                return chr(KI * (ord(char) - K2) % self.DIE)

            def decrypt(self, string):
                return "".join(map(self.decryptChar, string))

        affine = Affine()

        # print(affine.encrypt('Affine Cipher'))
        # print(affine.decrypt('*18?FMT'))


class base64(CIPHER):

    def base64(self):
        import base64

        sample_string = "GeeksForGeeks is the best"
        sample_string_bytes = sample_string.encode("ascii")

        base64_bytes = base64.b64encode(sample_string_bytes)
        base64_string = base64_bytes.decode("ascii")

        print(f"Encoded string: {base64_string}")

        base64_string = " R2Vla3NGb3JHZWVrcyBpcyB0aGUgYmVzdA =="
        base64_bytes = base64_string.encode("ascii")

        sample_string_bytes = base64.b64decode(base64_bytes)
        sample_string = sample_string_bytes.decode("ascii")

        print(f"Decoded string: {sample_string}")


class transposition(CIPHER):

    def encryptMessage(self, key, message):
        ciphertext = [''] * key

        for col in range(key):
            position = col
            while position < len(message):
                ciphertext[col] += message[position]
                position += key
        return ''.join(ciphertext)  # Cipher text

    def decryptMessage(self, key, message):
        numOfColumns = math.ceil(len(message) / key)

        numOfRows = key

        numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

        plaintext = [''] * numOfColumns

        col = 0
        row = 0
        for symbol in message:
            plaintext[col] += symbol
            col += 1  # point to next column
            if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
                col = 0
                row += 1
        return ''.join(plaintext)
