"""
ID: Christo97
LANG: PYTHON3
TASK: milk2
"""
fin = open('milk2.in', 'r')
fout = open('milk2.out', 'w')

# N = int(input(""))
N = fin.readline().split()
N = int(N[0])
start_times = []
end_times = []
for i in range(N):
    start, end = map(int, fin.readline().split())
    # start, end = map(int, input("").split())
    start_times.append(start)
    end_times.append(end)

start_times = sorted(start_times)
end_times = sorted(end_times)
#print(start_times, end_times)
total_off = 0
longest_off = 0
total_on = 0
longest_on = 0
# for i in range(len(start_times)-1):
#     if end_times[i] < start_times[i+1]:
#         total_off = start_times[i+1] - end_times[i]
#         if total_off > longest_total_off:
#             longest_total_off = total_off
local_minimum = 10000000000000000
local_maximum = 0
if len(start_times) == 1:
    longest_on = end_times[0] - start_times[0]
    longest_off = 0
for i in range(len(start_times)-1):
    if start_times[i] < local_minimum:
        local_minimum = start_times[i]
    if end_times[i] < start_times[i+1]:
        local_maximum = end_times[i]
        if local_maximum - local_minimum > longest_on:
            longest_on = local_maximum - local_minimum
        if start_times[i+1] - end_times[i] > longest_off:
            longest_off = start_times[i+1] - end_times[i]
        local_minimum = start_times[i+1]
    else:
        total_on = end_times[i +1] - local_minimum
        if total_on > longest_on:
            longest_on = total_on
            total_on = 0
#
# print(longest_on, longest_off)
fout.write(str(longest_on) + " "+str(longest_off) + "\n")
fout.close()








