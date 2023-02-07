n_of_Q = int(input(""))
things_for_conversion = [input("") for i in range(n_of_Q)]

for i in range(len(things_for_conversion)):
    length = len(things_for_conversion[i])
    if "MOO" in things_for_conversion[i]:
        print(length - 3)
    elif "OOO" in things_for_conversion[i] or "MOM" in things_for_conversion[i]:
        print((length - 3) + 1)
    elif "OOM" in things_for_conversion[i]:
        print((length - 3) + 2)
    else:
        print("-1")


"""
Number of commands equals 0, -1 or len of the string - 3 + the number of replacements needed.
Possible valid three letter combinations:
MOO
OOO
MOM
OOM



Bank of test cases:
OOMOMOOMOMMOOOMOOOOM
MOOOOOOMMOMOMOOOM
MMOOOOM
MMOOOMMOMOMMOOOOOMM
MOOMMOMO
OOOMOMOOMOOMMMOOOOO
MMOOOOMMMMMMMOM"""


#
# def delete(num, string):
#     if num == 0:
#         string = string[1:]
#         return string
#     elif num == -1:
#         string = string[:-1]
#         return string
#
#
# def replace(num, string):
#     if string[num] == "M":
#         string[num] == "O"
#     elif string[num] == "O":
#         string[num] == "M"
#     return string[num]
