num_1=60
num_2=10
def add_numbers(num_1 , num_2):
    result=num_1+num_2
    print(result)

    add_numbers(num_1 , num_2)


def multiply_numbers(num_1 , num_2):
#if type (num_1==int) and type (num_2==int)
    result=num_1*num_2
    print(result)

    multiply_numbers(num_1 , num_2)

def subtract_numbers(num_1 , num_2):
 
    result=num_1-num_2
    print(result)

subtract_numbers(num_1 , num_2)

def divide_numbers(num_1 , num_2): 
    if num_2==0:
        print("Error:can't divisible by zero") 
        return
    result=num_1/num_2
    print(result)
    
divide_numbers(num_1 , num_2)



