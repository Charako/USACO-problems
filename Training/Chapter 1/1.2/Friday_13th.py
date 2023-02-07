"""
ID: Christopher97
LANG: PYTHON3
TASK: friday
"""
fin = open('friday.in', 'r')
fout = open('friday.out', 'w')

n = int(fin.readline().strip())
days_of_weeks = {i : 0 for i in range(7)}
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = 0
for i in range(1900, 1900 + n):
	for month in months:
		days_of_weeks[day % 7] += 1
		if month == 28:
			if i % 400 == 0 or (i % 100 != 0 and i % 4 == 0):
				day += 29
				continue
		day += month

for day in range(6):
    fout.write("{} ".format(days_of_weeks[day]))
fout.write("{}\n".format(days_of_weeks[6]))

fin.close()
fout.close()

