from random import choice
#Monty hall
swap=0
stay=0
for i in range(100):
    # swap
    door=choice([1,2,3])
    pick=choice([1,2,3])
    goats=[i for i in [1,2,3] if not i==door]
    goat=choice(goats)
    picks=[i for i in [1,2,3] if not (i==goat or i==pick)]
    pick=choice(picks)
    if pick==door:
        swap+=1
    #print(pick,goat,door)

    #stay
    door=choice([1,2,3])
    pick=choice([1,2,3])
    goats=[i for i in [1,2,3] if not i==door]
    goat=choice(goats)
    if pick==goat:
        picks=[i for i in [1,2,3] if not (i==goat or i==pick)]
        pick=choice(picks)
    if pick==door:
        stay+=1
    #print(pick,goat,door)


print("Swap",str(swap)+"%")
print("Stay",str(stay)+"%")
