"""
ID: Christo97
LANG: PYTHON3
TASK: barn1
"""
fin = open('barn1.in', 'r')
fout = open('barn1.out', 'w')
# M, S, C = map(int,input("").split(" "))
M, S, C = map(int, fin.readline().split())
output = S
stalls_occupied = []
for i in range(C):
    # stall = int(input(""))
    stall = fin.readline().split()
    stall = int(stall[0])
    stalls_occupied.append(stall)
stalls_occupied = sorted(stalls_occupied)
gap_between_stalls = [stalls_occupied[i+1] -stalls_occupied[i] - 1 for i in range(len(stalls_occupied) -1)]
gap_between_stalls = sorted(gap_between_stalls, reverse=True)
if M < C:
    for i in range(M-1):
        output -= gap_between_stalls[i]
    output -= (stalls_occupied[0] - 1) + (S- stalls_occupied[-1])
else:
    output = C
fout.write (str(output) + '\n')
fout.close()
