import sys

# S = int(input("Print the number of small treats:"))
# M = int(input("Print the number of medium treats:"))
# L = int(input("Print the number of Large treats:"))

import fileinput
c = 1
for f in fileinput.input():
    print(f)
    if f == "q":
        exit(0)
    if c % 3 == 1:
        S = int(f)
    elif c % 3 == 2:
        M = int(f)
    elif c % 3 == 0:
        L = int(f)
        out = 1 * S + 2 * M + 3 * L
        if out >= 10:
            ans = "Happy"
        elif out < 10:
            ans = "Sad"
        print("output:",ans)
    c+=1

# try:
#     out = 1*S+2*M+3*L
# except:
#     sys.stderr("Error")
#     exit(0)
#
# if out >= 10:
#     ans = "Happy"
# elif out < 10:
#     ans = "Sad"
#
# print(ans)