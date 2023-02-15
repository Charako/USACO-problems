"""
ID: Christo97
LANG: PYTHON3
TASK: combo
"""
fin = open ('combo.in', 'r')
fout = open ('combo.out', 'w')

N = fin.readline().split()
N = int(N[0])
john_password = list(map(int, fin.readline().split(" ")))
master_password = list(map(int, fin.readline().split(" ")))
#
# N =  int(input(""))
# john_password = list(map(int, input("").split(" ")))
# master_password = list(map(int, input("").split(" ")))

range_tot = [x for x in range(1,N+1)]
range_tot = range_tot + range_tot
overspill_list = []

"""
for each password, work out range for each digit and add to list. then iterate through each value of that list
"""
def create_options(list_input):
    sub_lists = []
    for item in list_input:
        individual = [range_tot[i] for i in range(range_tot.index(item)-2, range_tot.index(item) +3)]
        sub_lists.append(individual)
    return sub_lists
def combinations(lists):
    result = []
    def backtrack(temp, index):
        if index == len(lists):
            result.append(temp[:])
            return
        for num in lists[index]:
            temp.append(num)
            backtrack(temp, index + 1)
            temp.pop()
    backtrack([], 0)
    return result
if N > 1:
    all_combinations = combinations(create_options(john_password)) + combinations(create_options(master_password))
    all_combinations_unique = []
    all_combinations = [all_combinations_unique.append(x) for x in all_combinations if x not in all_combinations_unique]
else:
    all_combinations = [1]

fout.write(str(len(all_combinations)) + "\n")
fout.close()
