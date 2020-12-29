A = int(input())
B = int(input())
C = int(input())
counting_list = [0] * 10
mul = A * B * C

while mul != 0:
    extract = mul % 10
    counting_list[extract] += 1
    mul = mul // 10
    
for i in counting_list:
    print(i)