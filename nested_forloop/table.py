table_num = int(input('Enter Table Number : '))
for a in range(11):
    for b in range (a, a+1):
        print(table_num,'*',b,'=',table_num*b)