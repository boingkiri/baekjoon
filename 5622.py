arr2 = ['A','B','C']
arr3 = ['D','E','F']
arr4 = ['G','H','I'] 
arr5 = ['J','K','L'] 
arr6 = ['M','N','O'] 
arr7 = ['P','Q','R','S'] 
arr8 = ['T','U','V']
arr9 = ['W','X','Y','Z']

S = input()
num_S = len(S)
sum = 0

for i in S:
    if (i in arr2):
        sum += 2
    elif (i in arr3):
        sum += 3
    elif (i in arr4):
        sum += 4
    elif (i in arr5):
        sum += 5
    elif(i in arr6):
        sum += 6
    elif(i in arr7):
        sum += 7
    elif(i in arr8):
        sum += 8
    else:
        sum += 9
sum += len(S)

print(sum)