#problem 1 from google classroom 
# Exercise 3
def main_array(the_array):
    rep_of_19s =  the_array.count(19)
    rep_of_5s = the_array.count(5)

    if rep_of_19s == 2 and rep_of_5s >= 3:
        return True
    
    else:
        return False


input_array =  [19, 19, 15, 5, 3, 5, 5, 2]
result = main_array(input_array)
print(result)

input_array_2 =  [19, 15, 15, 5, 3, 3, 5, 2]
result_2 = main_array(input_array)