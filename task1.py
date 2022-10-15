from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256
import random as r

def get_hash(pt):
    if type(pt) != bytes:
        pt = bytes(pt, 'utf-8')
    h = SHA256.new()
    h.update(pt)
    return h.hexdigest()

def int_to_bytes(val):
    byte_arr_len = (val.bit_length() + 7) // 8
    return val.to_bytes(byte_arr_len, byteorder='big')

# takes in two ints w/ hamming distance of 1
def b(a, b):
    bytes_a = int_to_bytes(a)        # 8 = 1000 in bytes
    bytes_b = int_to_bytes(b)        # 9 = 1001 in bytes (Hamming distance 1)
    print(bytes_a)
    print(bytes_b)
    ct = get_hash(bytes_a)           
    print(ct)
    ct2 = get_hash(bytes_b)           
    print(ct2)

if __name__ == '__main__':
    # part a
    rand_bytes = get_random_bytes(16)   # 16 random bytes
    ct = get_hash(rand_bytes)           # hashed
    print(ct)                           # hex printed

    # part b
    b(8, 9)     # 8 = 1000 in bytes, 9 = 1001 in bytes (Hamming distance 1)
    b(27, 31)     # 27 = 11011 in bytes, 31 = 11111 in bytes (Hamming distance 1)
    b(32, 34)   # 32 = 100000 in bytes, 34 = 100010 in bytes (Hamming distance 1)

    # part c