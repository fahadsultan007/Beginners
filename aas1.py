def adding_numbers(num1 , num2):
    return int(num1) + int(num2)

def dividing_numbers(num1 , num2):

    if int(num2) != 0:
        return int(num1) / int(num2)
    else:
        print("You can't divide by zero!")
        return 0
        
def subtracting_numbers(num1 , num2):
    return int(num1) - int(num2) 
 
def multiyplying_numbers(num1 , num2):
    return int(num1) * int(num2)


print('Enter the desire numbers to add :')
print('Enter first number')
num1 = input()
print('Enter second number')
num2 = input()
print('your ans is  :' + str(adding_numbers(num1,num2)))


print('Enter the desire numbers to divide :')
print('Enter first number')
num1 = input()
print('Enter second number')
num2 = input()
print('your ans is  :' + str(dividing_numbers(num1,num2)))


print('Enter the desire numbers to multiply :')
print('Enter first number')
num1 = input()
print('Enter second number')
num2 = input()
print('your ans is  :' + str(multiyplying_numbers(num1,num2)))


print('Enter the desire numbers to subtract :')
print('Enter first number')
num1 = input()
print('Enter second number')
num2 = input()
print('your ans is  :' + str(subtracting_numbers(num1,num2)))