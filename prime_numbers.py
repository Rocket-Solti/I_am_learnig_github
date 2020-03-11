num =int(input('Enter any number:'))
for i in range (2,num):
    if num % i== 0:
        print('the number you entered is Not Prime number')
        break
else:
    print('Your Number is a Prime number')
