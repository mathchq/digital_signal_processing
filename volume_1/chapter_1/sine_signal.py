# -*- coding:utf8 -*-
import matplotlib.pyplot as plt
import math


# matplotlib.colors
# b : blue.
# g : green.
# r : red.
# c : cyan.
# m : magenta.
# y : yellow.
# k : black.
# w : white.
def main():
    # signal frequency in Hz
    fy = 1
    # signal frequency in rad/s
    wy = 2 * math.pi * fy
    # sampling frequency in Hz
    fs = 60

    # (0 : 1 / 60 : 3 - 1 / 60 ) * 60 due to
    # the function of the range()
    t = [x / fs for x in range(int(3 * fs))]
    y = [math.sin(wy * x) for x in t]
    plt.axis([0, 3, -1.5, 1.5])
    plt.plot(t, y, 'k')
    plt.xlabel("Seconds")
    plt.title("Sine Signal")
    plt.show()


if __name__ == '__main__':
    main()
