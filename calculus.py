__author__ = 'wing2048'
import os
u = float(input("Initial Velocity: "))
a = float(input("Acceleration: "))
print()
print("Assuming constant values and vacuum:")
while True:
    t = float(input("Time: "))
    v = u + a*t
    s = (v**2 - u**2) / 2*a
    print("At t=%.2f seconds:" % t)
    print("Velocity: %s m/s" % v)
    print("Linear distance from 0: %s m" % s)
    print()
    # print("Velocity vs time:")
    # for y in range(11):
    #     print("%s " % (10 - y), end='')
    #     for x in range(os.get_terminal_size().columns):
    #         x += 1
    #         if x * a + u == 10 - y:
    #             print('X', end='')
    #         else:
    #             print(' ', end='')
    #     print()