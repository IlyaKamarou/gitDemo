def calc (c,num,num2):
    if x == '*':
        print( num * num2 )
    elif x == '+':
        print(num + num2)
    elif x == '-':
        print(num - num2)
    elif x == '/':
        print(num / num2)
    elif x == '**':
        print(num ** num2)
    elif x == '//':
        print(num // num2)
    elif x == '%':
        print(num % num2)
    else:
        print('Inputed data is not correct.')                       # Print information about error
out_from_loop = True
while  out_from_loop:
    x = str(input('Enter type of operation ( * + - / ** // % ): ')) # Request type of operation from user
    a = float(input('Enter the first number: '))                    # Request the first number
    b = float(input('Enter the second number: '))                   # Request the second number
    calc(x,a,b)
    var = input('input q for exit: ')
    if var == 'q':
        out_from_loop = False