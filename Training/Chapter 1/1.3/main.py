"""
ID: Christo97
LANG: PYTHON3
TASK: namenum
"""
fin = open ('namenum.in', 'r')
fout = open ('namenum.out', 'w')

with open("dict.txt", "r") as cow_names:
	lines = cow_names.read().splitlines()


numbers = ["2", "3", "4", "5", "6", "7", "8", "9"]
letters = [["A","B","C"], ["D","E","F"], ["G","H", "I"], ["J","K", "L"], ["M", "N", "O"], ["P", "R","S"], ["T", "U","V"], ["W","X", "Y"]]
#
# the_number = input("")
the_number = fin.readline().split()
the_number = the_number[0]

indices = []
outputs = []
# for i in range(len(the_number)):
# 	indices.append(numbers.index(the_number[i]))
# for i in range(len(indices)):

def generate_combinations(number):
    mapping = {
        '2': ['A', 'B', 'C'],
        '3': ['D', 'E', 'F'],
        '4': ['G', 'H', 'I'],
        '5': ['J', 'K', 'L'],
        '6': ['M', 'N', 'O'],
        '7': ['P', 'R', 'S'],
        '8': ['T', 'U', 'V'],
        '9': ['W', 'X', 'Y'],
    }
    result = []
    def all_combinations(combination, next_digits):
        if len(next_digits) == 0:
            result.append(combination)
        else:
            for letter in mapping[next_digits[0]]:
                # print(next_digits[0],combination, letter, next_digits[1:])
                all_combinations(combination + letter, next_digits[1:])
    all_combinations("", number)
    return result

valid = [word for word in generate_combinations(the_number) if word in lines]

if len(valid) ==0:
    fout.write("NONE" + "\n")
else:
    for word in valid:
        fout.write(word + "\n")

fout.close()