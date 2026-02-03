print('Hello world - hello')

while True:
    try:
        celsius = float(input('Please enter the temperature in Celsius: '))
        break
    except:
        print('You did not enter a valid number, try again')

fahrenheit = (celsius * (9/5)) + 32

print('The temperature in Fahrenheit is: ', fahrenheit)
