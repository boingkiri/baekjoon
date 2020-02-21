
def check_cabbage_area(field : list,
                    x : int, y : int, 
                    max_x : int, max_y : int,
                    count : int) :
    check = eliminate_sub_cabbage_area(field, x, y, max_x, max_y)
    if (check):
        count += 1
    if (max_x == x and max_y == y):
        return count
    elif(max_x == x):
        x = 0
        y += 1
    else:
        x += 1
    

def eliminate_sub_cabbage_area(field : list, 
                                x : int, y : int,
                                max_x : int, max_y : int):
    if (field[y][x] == 0) : 
        return False
    else :
        field[y][x] = 0
        if (x == max_x and y == max_y):
            return
        elif (x == max_x):
            eliminate_sub_cabbage_area(field, x, y+1, max_x, max_y)
        elif(y == max_y):
            eliminate_sub_cabbage_area(field, x+1, y, max_x, max_y)
        else:
            eliminate_sub_cabbage_area(field, x+1, y, max_x, max_y)        
            eliminate_sub_cabbage_area(field, x, y+1, max_x, max_y)
        return True

T = int(input())

for i in range(0,T):
    M,N,K = input().split()
    field = [([0] * int(M)) * int(N)]
    print(len(field))
    print(len(field[0]))
    for j in range(0,int(K)):
        X,Y = input().split()
        field[int(Y)][int(X)] = 1
    max_x = len(field[0])
    max_y = len(field)
    print(check_cabbage_area(field, 0, 0, max_x, max_y, 0))
