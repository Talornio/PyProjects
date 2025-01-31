import random

for n in range(1, 3001):
    print(f"{n}; {random.randrange(1, 10000)}", file=open('output.txt', 'a'))