#!/usr/bin/env python3

import numpy as np 

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

def get_score(message) -> (bytes, float):
    score = 0
    for i in message:
        c = chr(i).lower()
        if c in english:
            score += english[c]
    return score

def get_entropy(data):
    #interprets decrypted data as int array
    int_array = np.frombuffer(data, np.uint8)
    #counts number of occurrences of each int value
    count = np.bincount(int_array)
    #computes probability for each int value
    prob = count/float(np.sum(count))
    #throw away zero values
    prob = prob [ np.nonzero(prob) ]
    #Shannon entropy
    entropy = -sum(prob * np.log2(prob))

    return entropy


def break_enc(data):
    candidates = []

    for key in range(256):
        xord_bytes = b''
        for byte in data:
            xord_bytes += (bytes([byte ^ key]))
        candidates.append(xord_bytes)

    max_score = (b'', -1)
    for candidate in candidates:
        score = get_score(candidate)
        #entropy = get_entropy(candidate)
        if score > max_score[1]:
            max_score = (candidate, score)
    return max_score[0]


def main():
    enc = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
    dec = break_enc(enc)
    dec = dec.decode("utf-8")
    assert dec == "Cooking MC's like a pound of bacon"


if __name__ == "__main__":
    main()

