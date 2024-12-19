import random
taash=[2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
house=[random.choice(taash)]
u=[random.choice(taash), random.choice(taash)]
print('House: ',house)
print('You: ',u)
game=0
while game==0 and sum(u)<21 and sum(house)<21:
    dec=input('Hit or Stand?\n')
    if dec=='hit':
            print('\n\n\n\n')
            u.append(random.choice(taash))
            print('House: ',house)
            print('You: ',u)
    if dec=='stand':
            while sum(house)<21 and sum(house)<sum(u):
                print('\n\n\n\n')
                house.append(random.choice(taash))
                print('House: ',house)
                print('You: ',u)
                game+=1
if (game>=0 and sum(u)>sum(house) and sum(u)<=21) or sum(house)>21:
    print('You win!')
elif (game>=0 and sum(u)<sum(house) and sum(house)<=21) or sum(u)>21:
    print('House wins!')
elif game>=1 and sum(u)==sum(house):
    print('Push!')
