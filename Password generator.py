from random import randint
from string import ascii_letters


class Password:
    def __init__(self, length, collection="0123456789!@#$" + ascii_letters):
        self.length = length
        self.collection = collection

    def generate_password(self):
        return ''.join([self.collection[randint(0, len(self.collection) - 1)] for i in range(self.length)])


psw = Password(10)
for x in range(5):
    print(psw.generate_password())
