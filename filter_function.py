number=[5,8,10,9,12,7,13,56,88,]
def even(x):
    if x%2==0:
        return True
    else:
        False
even_obj=list(filter(even,number))
print(even_obj)
