amount=80
if amount%100 == 0:
    if amount>=500:
        print(amount)
        notes = amount//500
        print("500 rs notes are",notes)
        amount = amount%500
    if amount>=200: 
        notes = amount//200
        print("200 rs notes are ",notes)
        amount = amount%200
    if amount>=100:  
        notes = amount//100
        print("100 rs notes are",notes)
        amount = amount%200
else:
    print("go and earn some money")