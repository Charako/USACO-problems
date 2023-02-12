### Future me (Sun 12 Feb 00:32 rn) is going to wonder why this code is so bad. The last 40 lines can definitely be cut, so can all those list
### comprehensions. This one question took me 5-7 hours over 4.5 day period so it was pretty brutal ngl. 29 attempts before I got it right.

"""
ID: Christo97
LANG: PYTHON3
TASK: transform
"""
fin = open ('transform.in', 'r')
fout = open ('transform.out', 'w')

N = fin.readline().split()
N= int(N[0])
# N = int(input(""))
# list(fin.readline().split())
initial = []
for i in range(N):
    input = fin.readline().split()
    temp = []
    for thing in input[0]:
        temp.append(thing)
    initial.append(temp)
final = []
for i in range(N):
    input = fin.readline().split()
    temp = []
    for thing in input[0]:
        temp.append(thing)
    final.append(temp)
# initial = [list(input("")) for x in range(N)]
# final = [list(input("")) for x in range(N)]


quarter = [["-" for x in range(N)] for x in range(N)]
quarter_vertical = [["-" for x in range(N)] for x in range(N)]
half = [["-" for x in range(N)] for x in range(N)]
half_vertical = [["-" for x in range(N)] for x in range(N)]
threefourths = [["-" for x in range(N)] for x in range(N)]
threefourths_vertical = [["-" for x in range(N)] for x in range(N)]
vertical = [["-" for x in range(N)] for x in range(N)]

"""
The rule for a rotation by 90° about the origin is (x,y)→(y,−x) .
The rule for a rotation by 180° about the origin is  (x,y)→(−x,−y)
The rule for a rotation by 270° about the origin is  (x,y)→(−y,x)
Horizontal flip = (x,y) = (-x,y)
"""

def rotate(list, initial):
    for i in range(len(initial)):
        for j in range(N):
            location = initial[i][j]
            list[j][N-i-1] = location
    return list
def flipVertically(list, initial):
    for i in range(len(initial)):
        for j in range(N):
            location = initial[i][j]
            list[i][N-j-1] = location
    return list

complete = False
output = 7
while complete == False:
    rotate(quarter, initial)
    if quarter == final:
        output = 1
        complete = True
        break
    rotate(half, quarter)
    if half == final:
        output = 2
        complete = True
        break
    rotate(threefourths, half)
    if threefourths == final:
        output = 3
        complete = True
        break
    flipVertically(quarter_vertical, quarter)
    flipVertically(half_vertical, half)
    flipVertically(threefourths_vertical, threefourths)
    if quarter_vertical == final or half_vertical == final or threefourths_vertical == final:
        output = 5
        complete = True
        break
    flipVertically(vertical, initial)
    if vertical == final:
        output = 4
        complete = True
        break
    if initial == final:
        output = 6
        complete = True
        break
    complete = True
    break
fout.write (str(output) + "\n")
fout.close()

