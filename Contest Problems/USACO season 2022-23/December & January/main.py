def cow_problem(N):
    #N = number of cows and therefore number of inputs
    all_cows = input('').split()
    all_cows = [int(item) for item in all_cows]
    all_cows = sorted(all_cows)
    unique_n = sorted(list(set(all_cows)))
    values = []
    position = 0
    for j in range(0,len(unique_n)):
        for i in range(position, len(all_cows)):
            search_number = unique_n[j]
            if all_cows[i] == search_number:
                position = 0
                index = all_cows.index(all_cows[i])
                total = len(all_cows) - index
                position += int(index)
                temp = []
                temp.append(total * search_number)
                temp.append(total)
                temp.append(search_number)
                values.append(temp)
                break
    values = max(values)
    print(values[0], values[2])

#number_input = int(input(""))
#cow_problem(number_input)

def cow_problem_t(N):
    #N = number of cows and therefore number of inputs
    all_cows = input('').split()
    all_cows = [int(item) for item in all_cows]
    all_cows = sorted(all_cows)
    unique_n = sorted(list(set(all_cows)))
    values = []
    position = 0

    for i in range(position, len(all_cows)):
        if len(unique_n) > 0:
                cool = [x for x in unique_n if x == all_cows[i]] #search_number
                if len(cool) == 1:
                    position = 0
                    index = all_cows.index(all_cows[i])
                    total = len(all_cows) - index
                    position += int(index)
                    temp = []
                    temp.append(total * cool[0])
                    temp.append(total)
                    temp.append(cool[0])
                    values.append(temp)
                unique_n.remove(cool[0])
    values = max(values)
    print(values[0], values[2])

number_input = int(input(""))
cow_problem(number_input)