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
# # N = int(input(""))
# N = int(fin.readline().split())
# base_year = 1900
# n_leap_years = [x for x in range(1900, 1900 + N) if x % 4 ==0 and x % 100 != 0]
# number_days = 365 * (N - len(n_leap_years) + 366 * len(n_leap_years))
# #   Monday = 1st Jan, T 2 W 3 T 4 F 5
# months = [0 for x in range(12)]
# names_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
#
# # fridays = number_days - 5
# days_done = 0
# for i in range(N):
#     for j in range(len(months)):
#         if j == 0 or j == 2 or j == 4 or j == 6 or j == 7 or j == 9 or j == 11:
#             if ((days_done + 13) - 5) % 7 == 0:
#                 months[j] = months[j] + 1
#                 days_done += 31
#             else:
#                 days_done += 31
#         elif j == 3 or j == 5 or j == 8 or j == 10:
#             if ((days_done + 13) - 5) % 7 == 0:
#                 months[j] = months[j] + 1
#                 days_done += 30
#             else:
#                 days_done += 30
#         elif j == 1:
#             if N + 1900 in n_leap_years:
#                 if ((days_done + 13) - 5) % 7 == 0:
#                     months[j] = months[j] + 1
#                     days_done += 29
#                 else:
#                     days_done += 29
#             elif N + 1900 not in n_leap_years:
#                 if ((days_done + 13) - 5) % 7 == 0:
#                     months[j] = months[j] + 1
#                     days_done += 28
#                 else:
#                     days_done += 28
# for i in range(12):
#     fout.write()
# fout.close()


