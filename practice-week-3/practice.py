#Q:1) A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.

# salery = int(input('enter your salary: '))
# yos = int(input('enter year of services: '))
# bonus=0;
# 
# if yos>=5:
#     bonus = salery/100 *5;
#     print('your net bonus is: ', bonus)
# else:
#     print('you are not eligible for bonus')

#Q:2) Take values of length and breadth of a rectangle from user and check if it is square or not.

# len = int(input('enter length : '))
# breadth = int(input('enter breadth : '))
# if len==breadth:
#     print('rectengular')
# else:
#     print('not a rectengular')

#Q:3) Take two int values from user and print greatest among them.

# f_no = int(input('enter first no: '))
# s_no = int(input('enter seconf no: '))
# 
# if f_no>s_no:
#     print(f_no, 'is greate than', s_no)
# else:
#     print(s_no, 'is greate than', f_no)


#Q:4) A school has following rules for grading system:
#a. Below 25 - F
#b. 25 to 45 - E
#c. 45 to 50 - D
#d. 50 to 60 - C
#e. 60 to 80 - B
#f. Above 80 - A
#Ask user to enter marks and print the corresponding grade.

# num = int(input('enter marks : '))
# if num>100:
#     print('out of range')
# elif num>=80 and num<=100:
#     print(num, '- A')
# elif num>=60 and num<=80:
#     print(num, '- B')
# elif num>=50 and num<=60:
#     print(num, '- C')
# elif num>=45 and num<=50:
#     print(num, '- D')
# else:
#     print('fail')

#Q:5) Take input of age of 3 people by user and determine oldest and youngest among them.

#Q:6) Write a program to print absolute vlaue of a number entered by user.

# num = int(input('enter no : '))
# if num<0:
#     num= num*-1
# print(num)


#Q:7) A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.

#Q:8) Modify the above question to allow student to sit if he/she has medical cause.
#Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.

# noch = int(input('enter no of classe held: '))
# noca = int(input('enter no of classe attended: '))
# res = noca*100/noch
# 
# if noca>noch:
#     print('error')
# elif res>=75:
#     print ('percentage of class attended', res, '%')
#     print('allow to sit in exam')
# else:
#     print ('percentage of class attended', res, '%')
#     cnfrm = input('if has medical cause y or n ? :')
#     if cnfrm== 'y' or cnfrm== 'Y':
#         print('allow to sit in exam special calse')
#     else:
#         print('not allow to sit in exam')


#Q:9) A 4 digit number is entered through keyboard. Write a program to print a new number with digits reversed as of orignal one. 










