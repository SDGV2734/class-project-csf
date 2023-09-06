# using sorting

def find_end_floor(input_string):
    current_floor=0
    for i in input_string:
        if i =='(':
            current_floor += 1
        elif i ==')':
            current_floor-= 1
    return current_floor
    
input_string="(((((((((())"
current_floor = find_end_floor(input_string)
print(current_floor)