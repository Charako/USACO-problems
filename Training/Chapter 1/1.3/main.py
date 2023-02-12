"""
ID: Christo97
LANG: PYTHON3
TASK: dualpal
"""
fin = open ('dualpal.in', 'r')
fout = open ('dualpal.out', 'w')

N, S = map(int, fin.readline().split())
# N, S = map(int, input("").split(" "))
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
total_valid = 0
num_being_guessed = S + 1
output = []
while total_valid != N:
    occurence = 0
    for i in range(2,11):
        numberin_base_squared = numberToBase(num_being_guessed, i)
        if numberin_base_squared[:] == numberin_base_squared[::-1]:
            occurence += 1
            if occurence == 2:
                total_valid +=1
                output.append(num_being_guessed)
                break
    num_being_guessed += 1
for item in output:
    fout.write(str(item) + "\n")
fout.close()
