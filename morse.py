#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Morse Code Decoder

"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
"""
__author__ = 'Gabrielle, stackoverflow'

from morse_dict import MORSE_2_ASCII


def decode_bits(bits):
    bits = bits.strip("0")
    freq = min([len(bit) for bit in bits.split("1") + bits.split("0") if bit])
    bits_morsecode = bits.replace(
        "111" * freq, "-").replace(
            "1" * freq, ".").replace(
                "0000000" * freq, "   ").replace(
                    "000" * freq, " ").replace(
                        "0" * freq, "")
    return bits_morsecode.strip()


def decode_morse(morse):
    letter = ''
    final_string = ''
    for index, items in enumerate(morse + ' '):
        if items != ' ':
            letter += items
        elif letter:
            final_string += MORSE_2_ASCII[letter]
            letter = ''
            if index < len(morse) - 2:
                if morse[index: (index + 3)] == '   ':
                    final_string += " "
    return final_string


if __name__ == '__main__':
    hey_jude_morse = ".... . -.--   .--- ..- -.. ."
    hey_jude_bits = "11001100110011000000110000001111110011001111110011111100000000000000000000011001111110011111100111111000000110011001111110000001111110011001100000011" # noqa

    # Be sure to run all included unit tests, not just this one.
    print("Morse Code decoder test")
    print("Part A:")
    print(f"'{hey_jude_morse}' -> {decode_morse(hey_jude_morse)}")
    print()
    print("Part B:")
    print(f"'{hey_jude_bits}' -> {decode_morse(decode_bits(hey_jude_bits))}")

    print("\nCompleted.")
