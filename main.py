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


class multiplicative(Input):
    def encrypt(self):
        self.encrypt_input()
        self.shift_input()
        text = self.msg
        key = self.shift
        encrypted_cipher = ''
        for char in text:
            if char != ' ':
                encrypted_cipher += chr(((ord(char) - 97) * key) % 26 + 97)
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
                    temp = (t1 * key) % 26
                    if (ord(char) - 97) == temp:
                        decrypted_cipher += t2
                    else:
                        continue
            else:
                decrypted_cipher += ' '
        return decrypted_cipher


class affine(Input):
    def shift_input(self):
        shift = int(input("Enter the first key: "))
        return shift

    def two_shift_input(self):
        shift = int(input("Enter the second key: "))
        return shift

    def encrypt(self):
        self.encrypt_input()
        text = self.msg
        key1 = self.shift_input()
        key2 = self.two_shift_input()
        encrypted_cipher = ''

        for char in text:
            if char != ' ':
                encrypted_cipher += chr((key1 * ord(char) + key2) % 26)
            else:
                encrypted_cipher += ' '
        return encrypted_cipher

    def decrypt(self):
        self.decrypt_input()
        text = self.msg
        key2 = self.two_shift_input()
        key3 = pow(key2, -1, 26)
        decrypted_cipher = ''

        for char in text:
            if char != ' ':
                decrypted_cipher += chr((key3 * ord(char) - key2) % 26)
            else:
                decrypted_cipher += ' '
        return decrypted_cipher


class basesixfour(Input):
    def encrypt(self):
        self.encrypt_input()
        text = self.msg

        sample_string_bytes = text.encode("ascii")
        base64_bytes = base64.b64encode(sample_string_bytes)
        encrypted_cipher = base64_bytes.decode("ascii")
        return encrypted_cipher

    def decrypt(self):
        self.decrypt_input()
        text = self.msg

        sample_string_bytes = base64.b64decode(text)
        decrypted_cipher = sample_string_bytes.decode("ascii")
        return decrypted_cipher


class transposition(Input):
    def encrypt(self):
        self.encrypt_input()
        self.shift_input()
        text = self.msg
        key = self.shift
        encrypted_cipher = [''] * key
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_cipher[col] += text[pointer]
                pointer += key
        return ''.join(encrypted_cipher)

    def decrypt(self):
        self.decrypt_input()
        self.shift_input()
        text = self.msg
        key = self.shift

        numCols = math.ceil(len(text) / key)
        numRows = key
        numShadedBoxes = (numCols * numRows) - len(text)
        decrypted_cipher = [""] * numCols
        col = 0
        row = 0

        for symbol in text:
            decrypted_cipher[col] += symbol
            col += 1

            if (
                    (col == numCols)
                    or (col == numCols - 1)
                    and (row >= numRows - numShadedBoxes)
            ):
                col = 0
                row += 1

        return ''.join(decrypted_cipher)
