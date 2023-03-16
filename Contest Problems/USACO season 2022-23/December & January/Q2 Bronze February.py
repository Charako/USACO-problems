#T = int(input(""))


# def rotate(list_input, initial, n, times):
#     for h in range(times):
#         for i in range(len(initial)):
#             for j in range(n):
#                 location = initial[i][j]
#                 list_input[j][n-i-1] = location
#     return list_input
# def rotate_list(lst, n):
#     for i in range(n):
#         lst = [list(x) for x in zip(*lst[::-1])]
#     return lst
#
# def given_T(T):
#     initial_n = int(input(""))
#     canvas_goal = []
#     for i in range(initial_n):
#         input1 = list(input(""))
#         canvas_goal.append(input1)
#     stamp = []
#     stamp_input_n = int(input(""))
#     for i in range(stamp_input_n):
#         input2 = list(input(""))
#         stamp.append(input2)
#     # copy_stamp = [["" for i in range(stamp_input_n)] for i in range(stamp_input_n)]
#     # print(copy_stamp)
#     print(rotate_list(stamp, 3))
#
#
# def can_create_stamp_painting(desired, stamp):
#     n = len(desired)
#     k = len(stamp)
#
#     # Try all possible positions of the stamp on the canvas
#     for i in range(n - k + 1):
#         for j in range(n - k + 1):
#             # Try all possible rotations of the stamp
#             for r in range(4):
#                 rotated_stamp = stamp
#                 # rotate_list(stamp, r)
#                 for _ in range(r):
#                     rotated_stamp = list(zip(*rotated_stamp[::-1]))
#                 # Stamp the rotated stamp on the canvas
#                 for ii in range(k):
#                     for jj in range(k):
#                         if rotated_stamp[ii][jj] == '*' and desired[i + ii][j + jj] != '*':
#                             break
#                     else:
#                         continue
#                     break
#                 else:
#                     # The stamp matches the desired painting
#                     return True
#     # The stamp cannot create the desired painting
#     return False
#
# # Read the input
# t = int(input())
# input("")
# # if t==4:
# #
# #     for i in range(4):
# #
# #         n = int(input())
# #         desired = [input().strip() for _ in range(n)]
# #     # print(_)
# #         k = int(input())
# #         stamp = [input().strip() for _ in range(k)]
# #         input("")
# # else:
# #     print("asdfadfhadrg")
# for _ in range(t):
#
#     # print("checking", _)
#     n = int(input())
#     desired = [input().strip() for _ in range(n)]
#     # print(_)
#     k = int(input())
#     stamp = [input().strip() for _ in range(k)]
#     # Check if the stamp can create the desired painting
#     # print("hi", _)
#     if _ == t-1:
#         # print("we are here")
#         if can_create_stamp_painting(desired, stamp):
#             print("YES")
#
#         else:
#             print("NO")
#     else:
#         if can_create_stamp_painting(desired, stamp):
#             print("YES")
#             input("")
#             print("we got to this point")
#         else:
#             print("NO")
#             input("")
# O(TN^4K^2) time complexity

# Rotate stamp by 90 degrees.
def rotate_ninety(shape, K):
    shape = list(list(row) for row in shape)
    # Create a new shape with rotated dimensions.
    rotated_shape = [[''] * K for _ in range(K)]
    for i in range(K):
        for j in range(K):
            rotated_shape[j][K - i - 1] = shape[i][j]
    # Copy the rotated shape back into the original shape.
    for i in range(K):
        shape[i] = ''.join(rotated_shape[i])
    return shape


# Check if stamp can be used at a given position in the painting.
def can_stamp(K, painting, stamp, i, j):
    for x in range(K):
        for y in range(K):
            if stamp[x][y] == "*" and painting[i + x][j + y] == ".":
                return False
    return True


def solve(N, K, painting, stamp):
    canvas = [["." for _ in range(N)] for _ in range(N)]
    # Go through every K by K area in the painting and try stamping.
    for i in range(N - K + 1):
        for j in range(N - K + 1):
            # Try stamping with all 4 orientations of the stamp.
            for h in range(4):
                if can_stamp(K, painting, stamp, i, j):
                    # Stamp with current orientation.
                    for x in range(K):
                        for y in range(K):
                            if stamp[x][y] == "*":
                                canvas[i + x][j + y] = "*"
                # Rotate the stamp by 90 degrees.
                stamp = rotate_ninety(stamp, K)
    if canvas == [list(row) for row in painting]:
        print("YES")
    else:
        print("NO")


T = int(input())
for i in range(T):
    # Read empty line.
    input()
    N = int(input())
    painting = [input() for j in range(N)]
    K = int(input())
    stamp = [input() for j in range(K)]
    solve(N, K, painting, stamp)
# given_T(T)

"""
10

2
**
*.
1
*

3
.**
.**
***
2
.*
**

3
...
.*.
...
3
.*.
...
...

3
**.
.**
..*
2
.*
*.

8
**..****
**..****
**..****
**..****
........
........
........
........
3
..*
..*
..*

2
**
*.
1
*

3
.**
.**
***
2
.*
**

3
...
.*.
...
3
.*.
...
...

3
**.
.**
..*
2
.*
*.

8
**..****
**..****
**..****
**..****
........
........
........
........
3
..*
..*
..*


"""




