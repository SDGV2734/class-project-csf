# exercise 4

def List_check(given_list):

    if len(given_list) == 8:

        fifth_element = given_list[4]

        rep_of_fifth_element  = given_list.count(fifth_element)

        return rep_of_fifth_element == 3

        return True
    
    return False
    
    
given_list = [19, 19, 15, 5, 5, 5, 1, 2]
result = List_check(given_list)
print(result)
     
 
given_list2 = [19, 15, 5, 7, 5, 5, 2]
result2 = List_check(given_list2)
print(result2)


given_list3 = [11, 12, 14, 13, 14, 13, 15, 14]
result3 = List_check(given_list3)
print(result3)


given_list4 = [19, 15, 11, 7, 5, 6, 2]
result4 = List_check(given_list4)
print(result4)

