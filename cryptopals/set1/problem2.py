#!/usr/bin/environ python3

str1 = bytes.fromhex("1c0111001f010100061a024b53535009181c")
str2 = bytes.fromhex("686974207468652062756c6c277320657965")

xord_bytes = b''
for b1, b2 in zip(str1, str2):
	xord_bytes += (bytes([b1 ^ b2]))

assert xord_bytes.hex() == '746865206b696420646f6e277420706c6179'
