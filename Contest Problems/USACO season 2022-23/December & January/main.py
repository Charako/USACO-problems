N, K = map(int, input("").split(" "))
days_needed = list(map(int, input("").split(" ")))
output = K + 1
number_of_consecutive = 0
for i in range(len(days_needed)-1):
    if number_of_consecutive == 0:
        output_joined = days_needed[i+1] - days_needed[i]   # - number_of_consecutive
        output_separate = 1 + K
        if output_joined >= output_separate:
            output += output_separate
            number_of_consecutive += 1
        else:
            output += output_joined
            number_of_consecutive = 0
    else:
        if output + (1 + K) < output + days_needed[i+1] - days_needed[i] + 1:
            output += 1+K
        else:
            output += days_needed[i+1] - days_needed[i]
print(output)







    #
    #
    #
    #     if (days_needed[i+1] - days_needed[i] + 1 + K - number_of_consecutive) <= (2 + 2*K):
    #         print((2 + 2*K))
    #         print(days_needed[i+1] - days_needed[i] + 1 + K - number_of_consecutive)
    #         print("stop")
    #         # if output == 0:
    #         output += days_needed[i+1] - days_needed[i] + 1 + K - number_of_consecutive
    #         # else:
    #         #     output += days_needed[i+1] - days_needed[i] + 1 - number_of_consecutive
    #         number_of_consecutive += 1
    #     else:
    #         number_of_consecutive = 0
    #         output += 2 + 2*K
    # else:
    #     if number_of_consecutive > 0:
    #         if (days_needed[i+1] - days_needed[i] + 1 - number_of_consecutive) <= (2 + 2*K):
    #             print((2 + 2*K))
    #             print(days_needed[i+1] - days_needed[i] + 1 - number_of_consecutive)
    #             print("stop other")
    #             # if output == 0:
    #             #     output += days_needed[i+1] - days_needed[i] + 1 + K - number_of_consecutive
    #             # else:
    #             output += days_needed[i+1] - days_needed[i] + 1 - number_of_consecutive
    #             number_of_consecutive += 1
    #         else:
    #             number_of_consecutive = 0
    #             output += 2 + 2*K

