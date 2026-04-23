#!/usr/bin/env python3

from itertools import product

OUTFILE = "smartlist.txt"

SUFFIXES = ["123", "007", "69"]
SYMBOLS = ["@", "#", "_"]

REPL = {
    'a': ['4', '@'],
    'e': ['3'],
    'i': ['1'],
    'o': ['0'],
    's': ['5', '$']
}


def leet(word):
    chars = []

    for c in word:
        chars.append([c, c.upper()] + REPL.get(c.lower(), []))

    for combo in product(*chars):
        yield ''.join(combo)


def generate(word):
    words = set()

    words.add(word)
    words.add(word.lower())
    words.add(word.upper())
    words.add(word.capitalize())

    for w in leet(word):
        words.add(w)

    final = set()

    for w in words:
        final.add(w)

        for n in SUFFIXES:
            final.add(w + n)
            final.add(n + w)

        for s in SYMBOLS:
            final.add(w + s)
            final.add(s + w)

    return final


word = input("Word: ")

with open(OUTFILE, "a", encoding="utf-8") as f:
    count = 0

    for password in generate(word):
        f.write(password + "\n")
        count += 1

print(f"Added {count} variants to {OUTFILE}")