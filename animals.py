legs = input("Does it have legs [y/n]: ")
if legs == 'y':
    is_fluffy = input("Is it fluffy [y/n]: ")

    if is_fluffy == 'y':
        print("It's a cat!")
    elif is_fluffy == 'n':
        print("It's a gator!")
elif legs == 'n':
    lives_on_land = input("Does it live on land [y/n]: ")
    if lives_on_land == 'y':
        print("It's a snake!")
    elif lives_on_land == 'n':
        print("It's a shark!")