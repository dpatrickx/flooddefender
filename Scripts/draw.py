import sys
import matplotlib.pyplot as plt

def main(f1, f11, f2, f12, f3, f13, f4):
    s = 70
    r1 = open(f1).read().split('\n')[0 : s]
    r11 = open(f11).read().split('\n')[0 : s]
    r2 = open(f2).read().split('\n')[0 : s]
    r12 = open(f12).read().split('\n')[0 : s]
    r3 = open(f3).read().split('\n')[0 : s]
    r13 = open(f13).read().split('\n')[0 : s]
    r4 = open(f4).read().split('\n')[0 : s]
    print len(r1)
    print len(r11)


    # draw picture
    x = range(0, s)
    plt.figure(1)
    ax = plt.subplot(111)
    plt.xlabel('x')
    plt.ylabel('y')
    # plt.axis([0, 2100, 0, 10000])
    plt.plot(x, r1, 'r--', label='r1')
    plt.plot(x, r11, 'r-', label='r11')
    plt.plot(x, r2, 'b--', label='r2')
    plt.plot(x, r12, 'b-', label='r12')
    plt.plot(x, r3, 'g--', label='r3')
    plt.plot(x, r13, 'g-', label='r13')
    plt.plot(x, r4, 'y--', label='r4')
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles[::-1], labels[::-1])
    plt.show()


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7])
