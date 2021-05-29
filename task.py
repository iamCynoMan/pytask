# #WAP to count the number of equal numbers from three given integers
def ques1(x, y, z):
    result = set([x, y, z])
    if len(result) == 3:
        return print("0")
    else:
        return print(4 - len(result))


a = input("Enter First Number: ")
b = input("Enter 2nd Number: ")
c = input("Enter 3rd Number: ")
ques1(a, b, c)


# # # WAP to find the number of notes (Sample of notes: 10, 20, 50, 100, 200 and 500 ) against a given amount.

# def ques2(a):
#     Q = [500, 200, 100, 50, 20, 10]
#     x = 0
#     for i in range(6):
#         q = Q[i]
#         x += int(a / q)
#         a = int(a % q)
#     if a > 0:
#         x = -1
#     return print(x)


# ques2(int(input()))


# # #WAP to find the median among the given list of numbers

# import statistics
# items = [6, 1, 8, 2, 3]
# statistics.median(items)
