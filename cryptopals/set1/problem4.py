#!/usr/bin/env python3

import numpy as np 
from tqdm import tqdm 
from Crypto.Util.strxor import strxor_c

english = {
    'a': 0.0651738,
    'b': 0.0124248,
    'c': 0.0217339,
    'd': 0.0349835,
    'e': 0.1041442,
    'f': 0.0197881,
    'g': 0.0158610,
    'h': 0.0492888,
    'i': 0.0558094,
    'j': 0.0009033,
    'k': 0.0050529,
    'l': 0.0331490,
    'm': 0.0202124,
    'n': 0.0564513,
    'o': 0.0596302,
    'p': 0.0137645,
    'q': 0.0008606,
    'r': 0.0497563,
    's': 0.0515760,
    't': 0.0729357,
    'u': 0.0225134,
    'v': 0.0082903,
    'w': 0.0171272,
    'x': 0.0013692,
    'y': 0.0145984,
    'z': 0.0007836,
    ' ': 0.1918182 
}

def get_score(message):
    score = 0
    for i in message:
        c = chr(i).lower()
        if c in english:
            score += english[c]
    return score

def get_second(val):
    return val[1]


def break_enc(enc_array):
    candidates = []

    for enc in tqdm(enc_array):
        for key in range(256):
            xord_bytes = strxor_c(enc, key)
            score = get_score(xord_bytes)
            candidates.append((xord_bytes, score))


    candidates.sort(key=get_second, reverse=True)
    return candidates


def main():
    with open("./.src/4.txt", "r") as file:
        enc_array = []
        for line in file.readlines():
            enc = bytes.fromhex(line)
            enc_array.append(enc)
    
    dec_array = break_enc(enc_array)
    dec = dec_array[0][0].decode('utf-8').strip()

    assert dec == "Now that the party is jumping"

if __name__ == "__main__":
    main()

