a = eval(input("enter a :"))
b = eval(input("enter b :"))
c = eval(input("enter c :"))

if a+b > c:
    if b + c > a:
        if c + a > b:
            perimeter = a+b+c
            print('perimeter:',perimeter)
else:
    print('invalid!')

x = 5
y = 6
print(f'the value of x is {x} and y is {y}')

number= input('enter your name')
print(type(number))

number_1=eval(input('enter your age:'))
print(number_1)
print(type(number_1))

x=eval(input('enter your score:'))
if x> 90:
    print('A')
elif x>80:
    print('B')
else:
    print('stupid')

x=eval(input("enter your score A:"))
y=eval(input("enter your score B:"))
if x>=90 and y >=90:
    print ('x is A, y is A')
else:
    print('stupid')
