import os
# print("hello world")
# print("my age is 20","i have apples")

# name = "deepak"

# price = 26
# age = 21
# print("my name is :",age)

# print(type(age)
# )
# print(type(name))

# a=5
# b=3
# sum = a + b
# print(sum)

# a = 20
# b = 10
# print(not(a<b))

# a = 5
# b = 7.4

# print(a+b)

# NAME = input("AANTER YOUR NAME ")
# print("welcome",NAME)

# num1 = int(input("enter your first number"))
# num2 = int(input("enter your seconf number :"))
# print("sum=",num1+num2)

# BASIC 2

# str = "i have my opnion also"
# ch = str[4]
# print(ch)
# # 
# str = "the boys season 3 is gonna be wild"
# ch = str[7]
# print(ch)

# slicing in python

# str = "stranger things is trending"
# ch  = str[2:6]
# print(ch)

# firstname = input("enter your first name")
# print(len(firstname),firstname)

# CONDITIONAL STATEMENT
#  passing_marks = int(input("enter your marks :"))

# if(passing_marks < 33):
#    print("you are fail")
#    print("do rexam")
# elif(passing_marks > 33):
#    print("you got passed")
#    print("congratulation")
# elif(passing_marks > 70):
#    print("you got A")      
   
# passing_marks = int(input("Enter your marks: "))

# if passing_marks < 33:
#     print("You failed")
#     print("Do re-exam")
# elif passing_marks > 70:
#     print("You got an A")
# elif passing_marks >= 33:
#     print("You passed")
#     print("Congratulations")

# marks = int(input("Enter your marks:"))

# if(marks >= 90):
#    grade = "A"
# elif(marks < 90 and marks >= 80):
#    grade = "B"
# elif(marks < 80 and marks >= 70):
#    grade = "c"
# elif(marks < 70 and marks >= 60):
#    grade = "d"
# elif(marks < 50):
#    grade = "f"

# WAP CHECK NUMER IS EVEN OR ODD

# num = int(input("Enter your number"))
# rem = num % 2
# if(rem == 0):
#     print("even")
# else:
#     print("odd")



   
# print("your grade is:", grade)

# LIST IN PYTHON
# list = [1 ,2 ,3 , 4,]

# list.append(5)
# print(list)

# list.sort(reverse= True )
# print(list)

# list.insert(5,11)
# print(list)

# list.remove(1)  ##element dekhta h ## 
# print(list)

# list.remove(3)
# print(list)

# list.pop(1)
# print(list)

# movies = []
# mov = input("enter your moive 1")
# movies.append(mov)
# mov = input("enter your movie 2")
# movies.append(mov)
# mov = input("enter your movie name 3")
# movies.append(mov)

# print(movies)

# list = [input("num1"),input("num2"),input("num3")]
# copy_list = list.copy()
# copy_list.reverse()

# if(list == copy_list):
#  print("this list an palindrome ")
# else:cl
#  print("this list is not pallindrome")





# info = {
#     "name" : "deepak",
#     "class" : "cse",
#     "skils" : ["python","javascript","aws","azure"] # type: ignore
# }

# info.update({"name" :"tela"})
# print(info)

# day1 = {
#     "excercise" : "no",
#     "breakfast" : "yes",
#     "study": {
#         "math": "yes",
#         "aws" : "yes",
#         "magic" : "no", 
#     },
#     "lunch" : "yes", 
# }
# day1.update({"excercise" : "yes",})
# print(day1["excercise"])

# collection = {1,2,3,4,5,}
# print(type(collection))
#  tupple ko = ()
#  set ko = {}
#  dictionary ko {}

# dictionary = {
#               "cat" : "a small animal",
#               "table" : ["a piece of furniture","listof facts and figure"]

#                     }
# print(dictionaary)

# set={
#     "python","java","c++","c++","python","javascript","java","python","java","c++","c"}
# print(len(set))

# dictionary ={}

# x = int(input("enter the marks of phy:"))
# dictionary.update({"phy" : x})
# print(dictionary)

# print(type(dictionary))
# lsit = [1,1,1,1,1,1]

# values = {
#     ("float",9.0),
#     ("int",9)
# }
# print(type(values))

# i = 1;
# while i <= 10:
#     print("tanmay",i)
#     i+=2
    ##PRINT A NUMBER FROM FROM 1 TO 100##
# i=1;
# while i<=100:
#     print("current",i)
#     i+=1

# i = 100;
# while i>=1:
#     print("current",i)
#     i-=1
# x=int(input("enter your number"))
# i=1;
# while i*x<=x*10:
#     print(i*x)
#     i+=1


# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# x = int(input("Please enter the length +1 of list: "))
# i = 0

# while i < x:  
#     print(list[i])
#     i +=  1

# i=0;
# while i<len(list):
#     print(list[i])
# <<<<<<< HEAD
# #     i+=1  
# # for el in range(1,100,1):
# #     print(el)


# Cafe_Menu = {
#     'pizza': 60,
#     'pazta': 60,
#     'tikki': 70
# }

# # Display the menu
# print(f'Hello! Here is our menu: {Cafe_Menu}')

# # Take the customer's first order
# Customer_order = input('Enter your order: ')
# total_order = 0

# if Customer_order in Cafe_Menu:
#     total_order += Cafe_Menu[Customer_order]
#     print(f'Your order for {Customer_order} has been placed.')
# else:
#     print(f'Sorry, {Customer_order} is not available. Please select from the menu.')

# # Ask if the customer wants to order anything else
# Second_order = input('Would you like to order anything else (Yes/No)? ').strip().lower()

# if Second_order == 'yes':
#     item = input('Enter your order: ').strip()
#     if item in Cafe_Menu:
#         total_order += Cafe_Menu[item]
#         print(f'Your order for {item} has been placed.')
#     else:
#         print(f'Sorry, {item} is not available. Please select from the menu.')

# # Display the total
# print(f'Your total is: {total_order}')
# =======
#     i+=1
# FUNCTION AND RETURN STATEMENT #

# def mulxi(a,b):
#     mulxi = a*b
#     print(mulxi)
#     return(mulxi)

# mulxi(2,8)
# >>>>>>> 0a009044ed069d62c43871c8895d2e3974734675


# def aver(a,b,c):
#     average = a+b+c
#     total = average/3
#     print(total)
#     return total

# aver(2,6,8)
# def fct(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#         print(fact)
#     return(fact)


# fct(7)

#USD TO INR

# def usd(n):
#     print(n*83)

# usd(9)

# def checker(n):
#     if(n%2==0):
#         print("this is an even number")
#     else:
#         print("this is an odd number")


# n=int(input("enter your number"))
# result = checker(n)
# print(result)

# def fact(n):
#         if (n==1 or n==0):
#             return 1
#         return fact(n-1) * n



# result = fact(5)
# print(result)

# def nat(n):
#     if(n==1):
#         return 1
#     return nat(n-1)+n

# result =   nat(2)
# print(result)

# f = open("dexter.txt","r")
# data = f.read()
# print(data)
# print(type(data))

# f = open("dexter.txt","r")
# line1 = f.readline()
# print(line1)
 
# line2 = f.readline()
# print(line2)

# f = open("dexter.txt  ","a")
# f.write("\n after the weekend")
 
# f.close()

# with open("machine.txt","w+") as f:
#     data = f.write("hi everyone \n we learning file i/o \n using java  \n i like programming in html")
#     print(data)
#     f.close()

# def search_word(word):
#     with open("machine.txt","r") as f:
#         data = f.read()
#         if(data.find(word)!= -1):
#             print("found")
#         else:
#             print("not found")


# search_word("html")

# def check_wrodline(word):
    
#     lice_no= 1
#     with open("machine.txt","r") as f:
#         while word:
#             if(word in )

# for i in range(1,6):
#     for j in range(1,6):
#         print('*',end=" ")
#     print()

# r = 6
# for i in range(1,r+1):
#     for j in range(1,i+1):
#        print('*',end=' ')
#     print()

# r = 6
# for i in range(r,0,-1):
#     for j in range(i):
#         print('x',end =' ')
#     print()

# r = 4
# for i in range(1,r+1):
#     for j in range(1,i+1):
#         print(j,end = ' ')
#     print()

# r = 5
# for i in range(r,0,-1):
#     for j in range(1,i):
#         print(j,end = ' ')
#     print()
    
# n = 5
# for i in range(n):
#     print(' ' * (i) + '* ' *(n-i))

# phone_book = {}

# # Menu and instructions
# print(
#     """Phonebook Operations:
#     1 = Add a contact in PhoneBook
#     2 = Delete a contact in PhoneBook
#     3 = Search for a contact in PhoneBook
#     4 = List all contacts in PhoneBook
#     5 = Exit
#     """
# )

# # Continuous loop for multiple operations
# while True:
#     # User input for operation choice
#     User_choice = input('Enter your operation "1", "2", "3", "4", or "5": ')
    
#     if User_choice == "1":
#         # Add a contact
#         Contact_Name = input('Enter the name of the contact: ')
#         Contact_Number = input(f'Enter the number for {Contact_Name}: ')
#         if Contact_Name in phone_book:
#             print('This contact already exists.')
#         else:
#             phone_book[Contact_Name] = Contact_Number
#             print(f'{Contact_Name} has been saved in the phonebook.')
    
#     elif User_choice == "2":
#         # Delete a contact
#         del_contact = input('Enter the contact name you want to delete: ')
#         if del_contact in phone_book:
#             del phone_book[del_contact]
#             print(f'{del_contact} has been deleted.')
#         else:
#             print(f'{del_contact} does not exist in the phonebook.')
    
#     elif User_choice == "3":
#         # Search for a contact
#         Search_contact = input('Enter the contact name you want to search for: ')
#         if Search_contact in phone_book:
#             print(f'{Search_contact}: {phone_book[Search_contact]}')
#         else:
#             print('This contact does not exist.')
    
#     elif User_choice == "4":
#         # List all contacts
#         if phone_book:
#             print("Phonebook entries:")
#             for name, phone in phone_book.items():
#                 print(f"{name}: {phone}")
#         else:
#             print("The phonebook is empty.")
    
#     elif User_choice == "5":
#         # Exit the program
#         print("Exiting PhoneBook. Goodbye!")
#         break
    
#     else:
#         # Invalid input handling
#         print("Invalid choice. Please enter a number between 1 and 5.")


# ---------------------------------------------Todo-list app------------------------------------------------------------------------------

# def todo():
#     tasks = []
#     Number_tasks = int(input("Welcome to the todo Enter how many task you gonna perform today :"))
#     for i in range (1,Number_tasks+1):
#         Current_task = input(f'Enter you task{i} :')
#         tasks.append(Current_task)
    
#     if len(tasks) >= 3:
#         print(f'You Gotta Do a lot Today\n{tasks}')
#     else:
#         print(f'Yee you have less Work Today\n{tasks}')
#     while True:
#         operation = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-Views\n5-Exit\n:----->"))
#         if operation == 1:
#             New_task = input('Enter your New Task :')
#             tasks.append(New_task)
#             print(f'{New_task}Has Been added')
#         elif operation == 2:
#             Update_task = input('Enter the task you want to update :')
#             if Update_task in tasks:
#                 bhale = input('Enter Your New Task :')
#                 ind = tasks.index(Update_task)
#                 tasks[ind]=bhale
#                 print('....Updating\nTask has been updated')
#             else:
#                 print('This task is not Exist')
#         elif operation == 3:
#             Del_task = input('Enter the task you wan to delete : ')
#             if Del_task in tasks:
#                 inde = tasks.index(Del_task)
#                 del tasks[inde]
#                 print('.....Deleting\nTask has been deleted')
#         elif operation == 4:
#                 if len(tasks) >= 3:
#                     print(f'You Gotta Do a lot Today\n{tasks}')
#                 else:
#                     print(f'Yee you have less Work Today\n{tasks}')
#         elif operation == 5:
#             print('Dhnayawad........')
#             break
#     else:
#         print('please Enter a valid number')

# todo()

# Vowels = 'aeiou'
# for char in Vowels:
#     print(char,end=' ')

# a = 0
# b = 1


# for _ in range(10):
#     next_number = a+b
#     a,b = b,next_number 
#     print(next_number,end=" ") 
while True:

        Number = int(input('Enter the Number you want to check'))
        is_prime = True

        for i in range(2,int(Number**0.5)+1):
            if Number%i == 0:
                is_prime = False
                break

        if is_prime:
            print('it is prime')
        else:
            print('not prime')
















    
    
     