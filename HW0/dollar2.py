
import sys

for line in sys.stdin:
    if sum(ord(letter)-96 for letter in line.strip().lower()) == 100:
        print(line.strip())