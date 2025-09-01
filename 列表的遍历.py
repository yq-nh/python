my_list = ["nh",666,True]

def list_while_func():
    index = 0
    while index<len(my_list):
        element = my_list[index]
        print(element)
        index+=1

def list_for_func():
    for element in my_list:
        print(element)
        
list_while_func()
list_for_func()