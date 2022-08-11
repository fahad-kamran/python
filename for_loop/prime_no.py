num = int(input('Enter Number : '))

for a in range (2, num+1,1):
    if a == num:
        print(num, 'is a Prime Number')
    elif num % a == 0:
        print(num, 'is not a prime number')
        break