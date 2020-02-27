count = 1
total = 0

X = int(input())
while (total + count < X):
    total += count
    count += 1
    
remainer = X - total
# print("count : " + str(count))
# print("total : " + str(total))
# print("remainer : "+ str(remainer))

if (count % 2 == 0): # num ->countup 
    numerator = remainer
    denominator = count - remainer + 1
else: # denom -> countdown
    numerator = count - remainer + 1
    denominator = remainer
print(str(numerator)+'/'+str(denominator))