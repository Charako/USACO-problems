### This looks inefficient but the question dictated a brute force approach. If you need any explanations of the code, just email me.

"""
ID: Christo97
LANG: PYTHON3
TASK: crypt1
"""
fin = open ('crypt1.in', 'r')
fout = open ('crypt1.out', 'w')

N = fin.readline().split()
N = int(N[0])
allowed_digits = list(map(int, fin.readline().split(" ")))
# allowed_digits = list(map(int,input("").split(" ")))
# N = int(input(""))
print(N)
print(allowed_digits)
banned_digits = [x for x in range(10) if x not in allowed_digits]
banned_digits = "".join(map(str, banned_digits))
print(banned_digits)

def generate_combinations(numbers, length, combination='', combinations=[]):
    if length == 0:
        combinations.append(combination)
        return
    for number in numbers:
        generate_combinations(numbers, length-1, combination+str(number), combinations)
combinationstwo = []
combinationsthree = []

generate_combinations(allowed_digits, 2, combinations=combinationstwo)
generate_combinations(allowed_digits, 3, combinations=combinationsthree)

# print(combinationstwo)
# print(combinationsthree)

answer = 0
for i in range(len(combinationstwo)):
    for j in range(len(combinationsthree)):
        no = True
        for digit in list(str((int(list(combinationstwo[i])[0]) * int(combinationsthree[j])))):
                    #print(digit, allowed_digits)
            if str(digit) in banned_digits:
                        #print("hi")
                no = False
        for digit in list(str(int(list(combinationstwo[i])[1]) * int(combinationsthree[j]))):
            if str(digit) in banned_digits:
                        #print("hi")
                no = False
        for digit in list(str(int(combinationsthree[j]) * int(combinationstwo[i]))):
            if str(digit) in banned_digits:
                no = False
        if no == True:
            if len(str(int(list(combinationstwo[i])[0]) * int(combinationsthree[j]))) <=3:
                if len(str(int(list(combinationstwo[i])[1]) * int(combinationsthree[j]))) <= 3:
                    answer +=1
                            # print(combinationsthree[j])
                            # print(combinationstwo[i])
                            #
                            # print(int(list(combinationstwo[i])[0]) * int(combinationsthree[j]))
                            # print(int(list(combinationstwo[i])[1]) * int(combinationsthree[j]))
                            # print(int(combinationsthree[j]) * int(combinationstwo[i]))
# print(answer)
fout.write(str(answer)+ "\n")
fout.close()
