"""num1 =[i for i in range(-5,5)]
num2 = [i for i in range(-5,5)]
num3 = [i for i in range(-5,5)]
print('num1 :',num1)
print('num2 :',num2)
print('num3:',num3)"""
def large_number(num1,num2,num3):
    if (num1 > num2) and (num1 > num3):
        largest = num1
    elif (num2 > num1) and (num2 > num3):
        largest = num2
    else:
        largest = num3

    return largest

