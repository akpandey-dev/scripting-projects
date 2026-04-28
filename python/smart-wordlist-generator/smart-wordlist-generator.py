#!/usr/bin/env python3
import sys, json, argparse
from itertools import product, combinations

OUTFILE = "smartlist.txt"
HISTORY = "history.json"

SUFFIXES = ["123","321","007","69","420","786","143","111","01","10"]
SYMBOLS = ["@", "#", "$", "_", "!", "!!"]
MIDS = ["@", "_", ".", "-", "!"]
REPL = {'a':['4','@'],'e':['3'],'i':['1','!'],'o':['0'],'s':['$','5'],'t':['7']}

def load_history():
    try:
        with open(HISTORY,'r',encoding='utf-8') as f:
            return json.load(f)
    except:
        return {}

def save_history(hist):
    with open(HISTORY,'w',encoding='utf-8') as f:
        json.dump(hist,f,indent=2)

def leet_all_combos(word):
    options = []
    for c in word:
        lower = c.lower()
        subs = [c, c.upper()] + REPL.get(lower,[])
        options.append(subs)
    return (''.join(p) for p in product(*options))

def middle_inserts(word):
    out = set()
    n = len(word)
    for pos in range(1,n):
        for s in MIDS: out.add(word[:pos]+s+word[pos:])
    for pos1 in range(1,n):
        for pos2 in range(pos1+1,n+1):
            for s1 in MIDS:
                for s2 in MIDS:
                    out.add(word[:pos1]+s1+word[pos1:pos2]+s2+word[pos2:])
    return out

def number_symbol_mix(word):
    out = set()
    for suf in SUFFIXES:
        out.add(word+suf)
        out.add(suf+word)
        for s in SYMBOLS:
            out.add(word+s+suf)
            out.add(s+word+suf)
            out.add(suf+s+word)
    return out

def base_variants(word):
    variants = set([word.lower(), word.upper(), word.capitalize()])
    variants.update(leet_all_combos(word))
    variants.update(number_symbol_mix(word))
    variants.update(middle_inserts(word))
    # reverse
    variants.update({v[::-1] for v in variants})
    return variants

def generate(words):
    # stream generator
    seen = set()
    base_list = [base_variants(w) for w in words]
    for bl in base_list:
        for v in bl:
            if v not in seen:
                seen.add(v)
                yield v
    # combine pairs
    if len(words)>=2:
        for a,b in combinations(words,2):
            for combo in [a+b, b+a]:
                for v in base_variants(combo):
                    if v not in seen:
                        seen.add(v)
                        yield v

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('words', nargs='+')
    args = parser.parse_args()
    words = args.words

    hist = load_history()
    key = ','.join(sorted(words))
    if key in hist:
        print(f"[INFO] Input already processed: {words}")
        print(f"[ULTRA] Skipping generation, showing previous count: {hist[key]}")
        return

    print("[ULTRA] Streaming generator mode enabled")
    count = 0
    with open(OUTFILE,'a',encoding='utf-8') as f:
        for pw in generate(words):
            f.write(pw+'\n')
            count +=1

    print(f"[OK] Added ~{count} new variants")
    hist[key]=count
    save_history(hist)
    print(f"[INFO] History updated in {HISTORY}")

