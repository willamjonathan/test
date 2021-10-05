operator = eval(input('select an operator by using the number:1.Addition, 2.Subtraction, 3.Multiplication, 4.Division :'))
number1= eval(input('enter number1:'))
number2= eval(input('enter number2:'))
a = number1+number2
b = number1-number2
c = number1*number2
d = number1/number2
if operator == 1:
    print("it's", a)
elif operator == 2:
    print("it's", b)
elif operator == 3:
    print("it's", c)
elif operator == 4:
    print("it's", d)
else:
    print("error, unidentified operator, choose the right number")



