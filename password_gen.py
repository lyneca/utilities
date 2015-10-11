__author__ = 'wing2048'
import os
import random
small = [chr(a) for a in range(96, 96 + 27)]
capital = [chr(a) for a in range(65, 65 + 27)]
numbers = [str(a) for a in range(10)]
symbols = [a for a in range(33, 48)] + [a for a in range(58, 65)] + [a for a in range(91, 97)] + [a for a in
                                                                                                  range(123, 127)]
symbols = [chr(a) for a in symbols]


def generate(cap, low, num, sym):
    out = []
    for i in range(cap):
        out.append(random.choice(capital))
    for i in range(low):
        out.append(random.choice(small))
    for i in range(num):
        out.append(random.choice(numbers))
    for i in range(sym):
        out.append(random.choice(symbols))
    random.shuffle(out)
    return out

for i in range(10):
    print(''.join(generate(1, 6, 2, 1)))

os.system('pause>nul')