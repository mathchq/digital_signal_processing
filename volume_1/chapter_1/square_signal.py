# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt


def main():
    A = ([1] * 5 + [0] * 5) * 3
    fs = 10
    t = [x / fs for x in range(len(A))]
    plt.plot(t, A, "r*")
    plt.axis([0, 3, -0.5, 1.5])
    plt.xlabel("sec.")
    plt.title('square wave samples')
    plt.show()


if __name__ == '__main__':
    main()
