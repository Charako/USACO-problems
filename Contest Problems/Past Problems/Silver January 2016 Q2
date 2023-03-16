import sys
sys.stdin = open('div7.in', 'r')
sys.stdout = open('div7.out', 'w')


def psum(a):
    psum_list = [0]
    for i in a:
        psum_list.append(psum_list[-1] + i)
    return psum_list


N = int(input(""))
a = []

for i in range(N):
    number = int(input(""))
    a.append(number)

p = psum(a)
options = []
modulo = [p[n] % 7 for n in range(1, len(p))]
maximum = 0

for i in range(7):
    number_i = [modulo[j] for j in range(len(modulo)) if modulo[j] == i]
    if len(number_i) <= 1:
        continue
    else:
        first = modulo.index(i) + 1
        last = N - modulo[::-1].index(i)
        if last - first > maximum:
            maximum = last - first

print(maximum)






