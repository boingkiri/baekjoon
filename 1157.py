S = input()
arr = [0] * 26
for i in S:
    asciiNum = ord(i)
    if (asciiNum >= 97) : asciiNum -= 97
    else : asciiNum -= 65
    arr[asciiNum] = arr[asciiNum] + 1

Max = 0
Maxchr = 0
dup = False
for i in range(0,len(arr)):
    if (arr[i] == 0):
        continue
    elif (arr[i] > Max):
        Max = arr[i]
        Maxchr = i
        dup = False
    elif (arr[i] == Max and not dup):
        dup = True
if dup:
    print("?")
elif Max == 0:
    print("?")
else:
    print(chr(Maxchr+65))