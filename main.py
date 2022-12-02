import math
from string import ascii_lowercase
import base64
from art import *


class CIPHER():
    def __init__(self, msg, shift_pattern):
        self.msg = msg
        self.shift_pattern = shift_pattern

    def encrypt


class reverse(CIPHER):

    def encrypt_reverse(self):
        message = self.msg
        translated = ''
        i = len(message)

        while i > 0:
            translated += message[i]
            i -= 1
        return translated


class ceaser(CIPHER):

    def encrypt_ceaser_cipher(self, text, s):
        result = ""
        # transverse the plain text
        for i in range(len(text)):
            char = text[i]
            # Encrypt uppercase characters in plain text

            if (char.isupper()):
                result += chr((ord(char) + s - 65) % 26 + 65)
            # Encrypt lowercase characters in plain text
            else:
                result += chr((ord(char) + s - 97) % 26 + 97)
        return result

    # # check the above function
    # text = "CEASER CIPHER DEMO"
    # s = 4
    #
    # print("Plain Text : " + text)
    # print("Shift pattern : " + str(s))
    # print("Cipher: " + ceaser_cipher(text, s))

    def decrypt_ceaser_cipher(self, message, LETTERS):
        for key in range(len(LETTERS)):
            translated = ''
            for symbol in message:
                if symbol in LETTERS:
                    num = LETTERS.find(symbol)
                    num = num - key
                    if num < 0:
                        num = num + len(LETTERS)
                    translated = translated + LETTERS[num]
                else:
                    translated = translated + symbol
            print('Hacking key #%s: %s' % (key, translated))

    # decrypt_ceaser_cipher('GIEWIVrGMTLIVrHIQS','ABCDEFGHIJKLMNOPQRSTUVWXYZ')


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
