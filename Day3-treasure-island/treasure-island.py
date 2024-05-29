print('''
                                                                     P
                                        F~                          /\\
                                       /\\                         /__\\
                                      /__\\                        |. |
                                      |n |                       :_|__|_:
                                    :_|  |_:               p       |. |
                                      | n|    p      p    /\\      |. |
                                      |  |   /\\____/\\\ /__\\     |. |
                                      |n |_=_|. . . .|_=_=_=_=_=_=_|. |
                                      |n |. .|  ___  |. . . . . . .|. |
                                      |n |   | |   | |             |. |
                                    __|__|___|_|___|_|_____________|__|__
                                   /          /   /                      \\ ''')
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
direction = input("You're at a cross road. Where do you want to go?\n Type \"left\" or \"right\"\n")
if direction == "left":
    swim_wait = input("You've come to a lake. There is an island in the middle of the lake.\nType \"wait\" to wait for a boat. Type \"swim\" to swim across.\n")
    if swim_wait == "wait":
        door = input("You have reached the island safely. There are 3 doors in front of you."
                     "\n Which one do you want to open? \"red\" or \"yellow\" or \"blue\"?\n ")
        if door == "red":
            print("You are burned by fire. Game Over.")
        elif door == "yellow":
            print("You found the treasure! You WIN!")
        elif door == "blue":
            print("You are eaten by beasts. Game Over.")
        else:
            print("You liar. Game Over.")
    elif swim_wait == "swim":
        print("You are attacked by a trout. Game Over.")
elif direction == "right":
    print("You have fallen into a hole! Game Over.")
