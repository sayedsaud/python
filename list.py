# a = list((1,2,'saud','sayed'))
# print(a)
# print(len(a))
# print(type(a))



# b = list((1,2,'saud','sayed'))
# print(b)
# print(len(b))
# print(type(b))


# c = ['robert','saud','sanket','mishraji','sayed']
# for i in c:
#     if i[0]=='s':
#         print(i)


# c = ['robert','saud','sanket','mishraji','sayed']
# for i in c:
#     if "s" in i:
#         print(i)



# d = ['robert','saud','sanket','mishraji','sayed']
# for i in d:
#     for j in i:
#         if j=="r":
#          print(i)
     #  break   




# x = ['robert','saud','sanket','mishraji','sayed']
# for i in x:
#     count=0
#     for j in i:
#         if j in "aeiou":
#          count+=1
#     print(i,count)


# a = ['robert','saud','sanket','mishraji','sayed']
# i=0
# while i<len(a):
#     j=0
#     c=0
#     while j<len(a[i]):
#         if a[i][j] in "aeiou":
#          c=c+1
#         j+=1
#     print(a[i],c)
        
#     i+=1     
    
# l = ['robert','saud','sanket','mishraji','sayed']                                                                                                    
# for i in l:
#    if len(i) >= 5:
#       print(i)

# x = ['robert','saud','sanket','mishraji','sayed']
# for i in x:
#     c=""
#     count=0
#     for j in i:
#         if j in "aeiou":
#          count+=1
#          c=c+j
#     print(f"this is name = {i}  number of vowel {count} vowel {c}")



x = ['robert','Saud','sanket','mishraji','Sayed']
for i in x:
    c=""
    count=0
    for j in i.lower():
        if j in "aeiou":
         count+=1
         c=c+j
    print(f"this is name = {i}  number of vowel {count} vowel {c}")
