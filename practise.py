##a=int(input('enter your number : '))
##print(a)


##a=str("saud")
##print(a[3])

##a=str("saud")
##print(a[-2])

##a='hellohellohello'
##print(a)

##a="hello"
##b="world"
##print(a+b)


##a=10
##b=20
##a,b=b,a
##print(a)
##print(b)

##a=(1,2,3,4,3,2)
##for i in a:
##    if i ==3:
##        print(i)



##a=(1,2,3,4,3,2)
##count=a.count(3)
##print(f'occurence of 3={count}')



##a=(1,2,3,4,3,2)
##print(a[1],a[2],a[3])


##a=(1,2,3,4,3,2)
##new=tuple(x for x in  a if x !=3)
##print(new)


##a=str(input('enter your name: '))
##for i in range(1, len(a) + 1):
##    print(a[:i])


##for i in range(1,10,1):
##    for i in range(i):
##        print(i, end= " ")
##    print("\n")


##for num in range(10):
##    for i in range(num):
##        print (num, end=" ") 
##    print("\n")

##for num in range(10):
##    for i in range(num):
##        print ('*', end=" ") 
##    print("\n")
##for num in range(10,1,-1):
##    for i in range(num):
##        print ('*', end=" ") 
##    print("\n")

##for num in range(10,1,-1):
##    for i in range(num):
##        print ('*', end=" ") 
##    print("\n")


##n=[10,15,30,65,24,26,14,18]
##print('given list',n)
##for i in n:
##    if i % 5==0:
##        print('divisible of 5 = ',i)



##str_x = "Emma is good developer. Emma is a writer"
##find = str_x.count('Emma')
##print(f'Emma apperars {find} times')



n=1234
print('given number',n)
while n > 0:
    digit = n % 10
    number= n // 10
    print(digit, end= ' ')


##number = 7536
##print("Given number", number)
##while number > 0:
##    # get the last digit
##    digit = number % 10
##    # remove the last digit and repeat the loop
##    number = number // 10
##    print(digit, end=" ")
