equalArr = ['c','s']
minusArr = ['c','d']
jArr = ['l','n']
S = input()
count = 0
i = len(S) - 1

while i >= 0:
    if (S[i] == '='):
        try:
            if (S[i-1] in equalArr):
                i = i - 2
                count += 1
            elif (S[i-1] == 'z' and S[i-2] == 'd'):
                i = i - 3
                count += 1
            elif (S[i-1] == 'z'):
                i = i -2
                count += 1
            else : 
                i -= 1
                count += 1
            continue
        except IndexError:
            continue
    elif (S[i] == '-'):
        try:
            if (S[i-1] in minusArr):
                i = i - 2
                count += 1
            else : 
                i -= 1
                count += 1
            continue
        except IndexError:
            continue
    elif (S[i] == 'j'):
        try:
            if(S[i-1] in jArr):
                i = i - 2
                count += 1
            else : 
                i -= 1
                count += 1
            continue
        except IndexError:
            continue
    else:
        count += 1
        i -= 1

print(count)
