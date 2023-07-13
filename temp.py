clubs = [1,2,3,4,5,6,7,8,9,10]

for i in range(0,len(clubs),4):
    
    for club in clubs[i:i+4]:
        print(club)
    print('\n')