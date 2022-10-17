from nltk.corpus import words
from bcrypt import *
import time
import csv


def read_shadow():
    file = open("shadow.txt", "r")
    data = file.read()
    file.close()
    return data


def write_data(data):
    file = open("cracked_pw.csv", "w")
    writer = csv.writer(file)
    for i in data:
        writer.writerow(i)
    file.close()


def parse_shadow(data):
    lines = data.split('\n')
    new_data = []
    for i in lines:
        iSplit = i.split(":")
        line_data = [iSplit[0], iSplit[1]]
        new_data.append(line_data)
    return new_data


def generate_nltk_words():
    nltk_words = words.words()
    file = open("nltk.txt", "w")
    for i in nltk_words:
        if len(i) >= 6 and len(i) <= 10:
            file.write(i + '\n')
    file.close()


def get_hashes(data):
    cracked_pw = []
    for i in data:
        print(f"cracking {i[0]}'s password")
        hashed_pw = i[1]
        byte_hash = bytes(hashed_pw, 'utf-8')
        with open('nltk.txt') as nltk:
            start = time.time()
            for line in nltk:
                byte_word = bytes(line[:-1], 'utf-8')
                check = checkpw(byte_word, byte_hash)
                if check:
                    end = time.time()
                    print(f"password for {i[0]} cracked")
                    print(f"it is {byte_word}")
                    cracked_pw.append([i[0], i[1], byte_word, end - start])
                    break
            if check == False:
                print(f"No password found for {i}")
    nltk.close()
    return cracked_pw


if __name__ == '__main__':
    data = read_shadow()
    lines = parse_shadow(data)
    print(lines[0])
    cracked = get_hashes(lines)
    print(cracked)
    write_data(cracked)
