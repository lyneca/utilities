__author__ = 'wing2048'
import os
total = 0
for dir in os.listdir('.'):
    if dir[-3:] == '.py':
        print(dir)
        with open(dir) as file:
            for line in file:
                total += 1
print(total)
os.system('pause')
