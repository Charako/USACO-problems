### Takes input "base" to determine which base number to check if the square of the that number is a palindromic square.

"""
ID: Christo97
LANG: PYTHON3
TASK: palsquare
"""
fin = open ('palsquare.in', 'r')
fout = open ('palsquare.out', 'w')

# base = int(input(""))
base = fin.readline().split()
base = int(base[0])
output = []
def numberToBase(n, b):
    spillover = ["A","B","C","D","E","F","G","H","I","J"]
    if n == 0:
        return [0]
    digits = []
    while n != 0:
        if int(n%b) >9:
            digits.append(spillover[int(n%b) - 10])
            n //= b
        else:
            digits.append(str(n % b))
            n //= b
    return "".join(map(str, digits[::-1]))
for i in range(1,301):
    numberin_base_squared = numberToBase(i**2, base)
    if numberin_base_squared[:] == numberin_base_squared[::-1]:
        original = numberToBase(i, base)
        output.append([original, numberin_base_squared])
for list in output:
    fout.write(str(list[0]) + " " + str(list[1]) + "\n")
fout.close()
