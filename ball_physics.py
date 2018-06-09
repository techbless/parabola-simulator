import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D


def where(args):

    try:

        xs = int(args[0])  # position of x
        ys = int(args[1])  # position of y
        zs = int(args[2])  # position of z
        va = int(args[3])  # speed of x axes
        vb = int(args[4])  # speed of y axes
        vc = int(args[5])  # speed of z axes
        g = -1 * float(args[6])  # gravity power
        ti = float(args[7])  #time

        # t stands for time
        t = ti
        x = xs + va * t
        y = ys + vb * t
        z = zs + 1 / 2 * g * pow(t, 2) + vc * t
        v = math.sqrt(pow(va, 2)+pow(vb, 2)+pow(vc+g*t, 2))

        if t >= 0:
            pos = "( %s, %s, %s)" % (x, y, z)
            print("the position of the ball in time ", t, "(s) is ", pos)
            print("the speed of the ball is around", round(v, 2), "m/s")
        else:
            print("Can't show the minus of time.")

    except:
        print("Input should be like : where 10 20 10 40 20 40 10 6")


def draw(args):

    try:
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.set_xlim([-300, 600])
        ax.set_ylim([-300, 600])
        ax.set_zlim([-300, 600])

        # xyz start point, xyz throw speed, power of gravity
        xs = int(args[0])  # position of x
        ys = int(args[1])  # position of y
        zs = int(args[2])  # position of z
        va = int(args[3])  # speed of x axes
        vb = int(args[4])  # speed of y axes
        vc = int(args[5])  # speed of z axes
        g = -1 * float(args[6])  # gravity power

        # t stands for time
        t = np.linspace(0, 25, 80)
        x = xs + va * t
        y = ys + vb * t
        z = zs + 1 / 2 * g * pow(t, 2) + vc * t

        c = x + y
        ax.scatter(x, y, z, c=c)
        plt.show()

    except:
        print("Input should be like : draw 10 20 10 40 20 40 10")
