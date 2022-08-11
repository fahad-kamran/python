mark = int(input('Enter Your Marks : '))

if mark < 33:
    print('Fail')
elif mark > 33 and mark < 50:
    print('Grade D')
elif mark > 50 and mark < 60:
    print('Grade C')
elif mark > 60 and mark < 70:
    print('Grade b')
elif mark > 70 and mark < 80:
    print('Grade A')
elif mark > 80 and mark < 100:
    print('Grade A+')
else:
    print('undefined')