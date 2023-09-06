while True:
    a = input("convert from celcius'c' to farenheit'f' or vice versa or exit'e': ")

    if a == 'c':
        b = float(input('Enter your temperature in celcius: '))
        result = (b * 9//5) + 32
        result_int = int(result)
        print(b , 'degree celcius is' , result_int , 'farenheit')

    elif a == 'f':
        c = float(input('Enter your temperature in farenheit: '))
        output = (c - 32) * 5//9
        output_int = int(output)
        print(c, 'farenheit is' , output_int , 'celcius')

    elif a == 'e':
        print('thank you!!')
        break

    else:
        print('Invalide option, choose the correct the option.')