def find_max_num(num):
    if not num:
        return None
    
    max = 0
    for x in num:
        if x > max:
            max = x
    return max 
    
num = [0,1,23,45,65,873]
result = find_max_num(num)
print(f'max number is: {result}')


