import random
from string import ascii_letters, digits, punctuation

def randomGen(length=8):
    chars = ascii_letters + digits + punctuation
    return ''.join(random.choice(chars) for _ in range(length))

# print(randomGen(12))
