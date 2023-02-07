
"""
ID: Chris97
LANG: PYTHON3
TASK: ride
# """
fin = open('ride.in', 'r')
fout = open('ride.out', 'w')
x= fin.readline().strip()
y= fin.readline().strip()
# x = "STARAB"
# y = "USACO"

alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
output_x = 1
output_y = 1

letter_indices_x = [alphabet.index(letter) + 1 for letter in x]
letter_indices_y = [alphabet.index(letter) + 1 for letter in y]

for i in range(len(letter_indices_x)):
    output_x = output_x * letter_indices_x[i]
for i in range(len(letter_indices_y)):
    output_y = output_y * letter_indices_y[i]

print(output_x, output_y)

# for i in range(len(letter_indices_x)):
#     output_x = output_x * letter_indices_x[i]
#     output_y = output_y * letter_indices_y[i]

modfsx = output_x % 47
modfsy = output_y % 47
if modfsy == modfsx:
#    print("GO")
    fout.write("GO" + "\n")
else:
#    print("STAY")
    fout.write("STAY" + "\n")

fout.close()
