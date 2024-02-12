isItPrimeNo = int(input('Enter a number: '))
if isItPrimeNo > 1:
    for x in range(2, isItPrimeNo):
        if isItPrimeNo % x == 0:
            print('Not a prime number')
            break
    else:
        print('Prime number')
else:
    print('Not a prime number')