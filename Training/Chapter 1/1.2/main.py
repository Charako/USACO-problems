"""
ID: Christo97
LANG: PYTHON3
TASK: beads
"""

fin = open('beads.in', 'r')
fout = open('beads.out', 'w')

n = fin.readline().split()
n = int(n[0])
bead_string = fin.readline().strip()
# n = int(input(""))
bead_string = list(bead_string)


head_string = []
tail_string = []
maximum = 0
for i in range(n):
    total = 0
    head_string = bead_string[i:] + bead_string[:i]
    tail_string = bead_string[i:] + bead_string[:i]
    tail_string.reverse()

    if "b" not in tail_string or "r" not in tail_string:
        total = len(head_string)
    elif head_string[0] == "b":
        total += head_string.index("r")
    elif head_string[0] == "r":
        total += head_string.index("b")
    elif head_string[0] == "w":
        if head_string.index("b") > head_string.index("r"):
            total += head_string.index("b")
        else:
            total += head_string.index("r")

    if "b" not in tail_string or "r" not in tail_string:
        total = len(head_string)
    elif tail_string[0] == "b":
        total += tail_string.index("r")
    elif tail_string[0] == "r":
        total += tail_string.index("b")
    elif tail_string[0] == "w":
        if tail_string.index("b") > tail_string.index("r"):
            total += tail_string.index("b")
        else:
            total += tail_string.index("r")
    if total > maximum:
        maximum = total

    if maximum > len(bead_string):
        maximum = len(bead_string)

fout.write(str(maximum) + "\n")
fout.close()
