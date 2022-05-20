#                   1
#         012345678901234
parrot = "Norwegian Blue"

print(parrot[0:6:2])    # Nre
print(parrot[0:6:3])    # Nw

number = "9,223;372:036 854,775;807"
seperators = number[1::4]
print(seperators)

letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters
print(backwards[-22::-1])
