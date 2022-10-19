from scipy.spatial.distance import hamming
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256
import time
import random as r

# from https://www.geeksforgeeks.org/hamming-distance-two-strings/
def hammingDist(str1, str2):
    i = 0
    count = 0
    while(i < len(str1)):
        if(str1[i] != str2[i]):
            count += 1
        i += 1
    return count

def get_hash(b):
    if type(b) != bytes:
        b = bytes(b, 'utf-8')
    h = SHA256.new()
    h.update(b)
    return h.digest()

def int_to_bytes(val):
    byte_arr_len = (val.bit_length() + 7) // 8
    return val.to_bytes(byte_arr_len, byteorder='big')

# takes in two ints w/ hamming distance of 1
def b(a, b):
    bytes_a = int_to_bytes(a)        # 8 = 1000 in bytes
    bytes_b = int_to_bytes(b)        # 9 = 1001 in bytes (Hamming distance 1)
    ct = get_hash(bytes_a)
    print("Hash Pairs:")
    print(ct)
    ct2 = get_hash(bytes_b)           
    print(ct2)
    print(hammingDist(ct, ct2))
    print(len(ct))
    #print(hamming(ct, ct2))

def truncate_bits(b_int, k):
    binary = bin(b_int) # convert to binary string
    binary = binary[2:] # cutoff '0b' header
    end = len(binary)   # set end index
    start = end - k     # set start index
    k_bit_substr = binary[start:end+1]  # get desired bit substring
    return int(k_bit_substr, 2) # convert to int and return

# returns last k bits of hash of input bytes b
def get_hash_modified(b, k):
    if type(b) != bytes:
        b = bytes(b, 'utf-8')
    h = SHA256.new()
    h.update(b)
    b_int = int.from_bytes(h.digest(), "big")
    b_truncated = truncate_bits(b_int, k)
    return b_truncated

# finds collision of input size k
def find_collision(k):
    # initialize time, input ctr, and dict
    start_time = time.time()    # starting time
    ctr = 1  # input ctr
    h = get_hash_modified(get_random_bytes(16), k)  # first hash
    keys = {h: None}    # dict

    # creates new hashes, trying to put them in a dictionary. A collision is found if we do an update and the dict size remains the same
    while True:
        size = len(keys)
        h2 = get_hash_modified(get_random_bytes(16), k) # new hash for comparison
        keys.update({h2: None}) # attempts putting hash in dict
        ctr += 1
        # if dict size remains the same, a key was overwritten and we found a collision
        if len(keys) == size:
            break

    end_time = time.time()
    time_elapsed = end_time-start_time

    print("k: %d, time: %f, inputs: %d, key: %d" % (k, time_elapsed, ctr, h2))

if __name__ == '__main__':
    ## part a
    #rand_bytes = get_random_bytes(16)   # 16 random bytes
    #ct = get_hash(rand_bytes)           # hashed
    #print(ct)                           # hex printed
#
    # part b
    b(8, 9)     # 8 = 1000 in bytes, 9 = 1001 in bytes (Hamming distance 1)
    b(27, 31)   # 27 = 11011 in bytes, 31 = 11111 in bytes (Hamming distance 1)
    b(32, 34)   # 32 = 100000 in bytes, 34 = 100010 in bytes (Hamming distance 1)

    ## part c
    #for i in range(8, 52, 2):
    #    find_collision(i)