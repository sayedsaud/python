a = list((1,2,'saud','sayed'))
print(a)
print(len(a))
print(type(a))



b = list((1,2,'saud','sayed'))
print(b)
print(len(b))
print(type(b))


c = ['robert','saud','sanket','mishraji','sayed']
for i in c:
    if i[0]=='s':
        print(i)


c = ['robert','saud','sanket','mishraji','sayed']
for i in c:
    if "s" in i:
        print(i)



d = ['robert','saud','sanket','mishraji','sayed']
for i in d:
    for j in i:
        if j=="r":
         print(i)
         break   




x = ['robert','saud','sanket','mishraji','sayed']
for i in x:
    count=0
    for j in i:
        if j in "aeiou":
         count+=1
    print(i,count)
    
                                                                                                     
