N = int(input())

new_ten = N % 10
old_ten = N // 10
count = 1
tmp_sum = new_ten + old_ten
new_number = new_ten * 10 + tmp_sum % 10
while new_number != N:
    new_ten = new_number % 10
    old_ten = new_number // 10
    count += 1
    tmp_sum = new_ten + old_ten
    new_number = new_ten * 10 + tmp_sum % 10 

print(count)