"""
ID: Christo97
LANG: PYTHON3
TASK: milk
"""
fin = open ('milk.in', 'r')
fout = open ('milk.out', 'w')
# N, M = map(int, input("").split(" "))
N, M = map(int, fin.readline().split())
total_needed = N
cost = 0
farmers = []

for i in range(M):
    # farmer = list(map(int, input("").split(" ")))
    farmer = list(map(int,fin.readline().split(" ")))
    farmers.append(farmer)
farmers = sorted(farmers)
while total_needed > 0:
    for list in farmers:
        if total_needed - list[1] < 0:
            cost += (list[1] - abs(total_needed-list[1])) * list[0]
            total_needed = 0
            break
        else:
            cost += list[0] * list[1]
            total_needed -= list[1]
fout.write(str(cost) + "\n")
fout.close()