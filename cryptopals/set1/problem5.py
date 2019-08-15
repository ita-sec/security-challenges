#!/usr/bin/env python3

def repeating_key_xor(message, key):
    xord_bytes = b''
    len_key = len(key)
    for i in range(len(message)):
        c = key[i % len_key]
        xord_bytes += (bytes([message[i]^c]))
    return xord_bytes


def main():
    message = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = b"ICE"
    xord_message = repeating_key_xor(message, key).hex()
    flag = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272\
a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"

    assert xord_message == flag

if __name__ == "__main__":
    main()

