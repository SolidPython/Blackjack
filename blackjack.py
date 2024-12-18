import random
taash=[2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
house=[random.choice(taash)]
u=[random.choice(taash), random.choice(taash)]
print('House: ',house)
print('You: ',u)
while sum(u)<21:
    dec=input('Hit or Stand?\n')
    if dec=='hit':
            print('\n\n\n\n')
            u.append(random.choice(taash))
            print('House: ',house)
            print('You: ',u)
    if dec=='stand':
            while sum(house)<21 and sum(house)<sum(u) and sum(u)<21:
                print('\n\n\n\n')
                house.append(random.choice(taash))
                print('House: ',house)
                print('You: ',u)
if sum(u)>sum(house) and sum(u)<=21 or sum(house)>21:
    print('You win!')
elif sum(u)<sum(house) or sum(u)>21:
    print('House wins!')
elif sum(u)==sum(house):
    print('Push!')