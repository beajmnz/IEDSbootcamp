#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 17:38:06 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""


MORSE_CODE = {
    "....": "H",
    ".": "E",
    "-.--": "Y",
    ".---": "J",
    "..-": "U",
    "-..": "D",
}


def decodeMorse(morse_code):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    words = morse_code.split("   ")
    for word_index in range(len(words)):
        answer = words[word_index].split()
        for i in range(len(answer)):
            if answer[i] == "":
                continue
            answer[i] = MORSE_CODE[answer[i]]
        words[word_index] = "".join(answer)
    morse_code = " ".join(words)
    return morse_code.replace(" ", "")


print(decodeMorse(".... . -.--   .--- ..- -.. ."))


""" CODEWARS SOLUTION

def decodeMorse(morseCode):
    return ' '.join(''.join(MORSE_CODE[letter] for letter in word.split(' ')) for word in morseCode.strip().split('   '))
    
"""