# O(N) time complexity

N, T = (int(i) for i in input("").split(" "))
total = 0
n_eaten = 0
days_since_last_feeding = 0

for i in range(N):
    day, n_haybales = (int(j) for j in input("").split(" "))

    days_since_last_eaten = day - days_since_last_feeding

    n_eaten += min(days_since_last_eaten, total)
    total -= min(days_since_last_eaten, total)
    total += n_haybales
    days_since_last_feeding = day

if days_since_last_feeding <= T:

    days_since_last_eaten = T - days_since_last_feeding + 1

    if total > days_since_last_eaten:
        n_eaten += days_since_last_eaten
    else:
        n_eaten += total

print(n_eaten)