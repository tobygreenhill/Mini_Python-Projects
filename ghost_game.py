from random import randint
print("Ghost Game")
feeling_brave = True
score = 0
while feeling_brave:
    ghost_door = randint(1,3)
    print("Three Doors Ahead...")
    print("a GHOST BEHIND ONE .")
    print("Which door will you open")
    door = input("1,2 or 3")
    door_num = int(door)
    if door_num == ghost_door:
        print("GHOST!")
        feeling_brave = False
    else:
        print("No Ghost")
        print("You enter the next room")
        score = score + 1
print("Run away!")
print ("Game over! You scored", score)