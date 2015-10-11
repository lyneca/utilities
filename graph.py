__author__ = 'wing2048'
from math import *
import os

def display(array):
    for y in array:
        for x in y:
            if x == 0:
                print(' ', end='')
            elif x == 1:
                print('.', end='')
            else:
                print('+', end='')
        print()


while True:
    function = input('f(x) = ')
    graph = []
    for i in range(30):
        line = []
        if i == 15:
            for j in range(30):
                line.append(2)
        else:
            for j in range(30):
                if j == 15:
                    line.append(2)
                else:
                    line.append(0)
        graph.append(line)
    for x in range(30):
        x -= 15
        try:
            y = eval(function)
            print(y)
        except:
            print('There was an error.')
            os.system('pause')
            break
        if len(graph) >= y + 15:
            if len(graph[y + 15]) >= x + 15:
                if x + 15 >= 0 and y + 15 >= 0:
                    graph[29 - (y + 15)][x + 15] = 1
    display(graph)
    # print(graph)
    os.system('pause')
    os.system('cls')