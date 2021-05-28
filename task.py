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
