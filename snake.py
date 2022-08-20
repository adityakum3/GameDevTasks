import time                             # for measuring time and time difference
import keyboard as kb                   # for handling keyboard events
import os
import random  # for randomly placing food

n = 25  # Size of our square arena

a = [["." for i in range(n)] for j in range(n)]  # Our game arena/screen

# Snake array (this array will contain cells occupied by our snake)
sn = [(int(n/2), int(n/2))]

# Other variables

global dir
# this dir variable would decide the heading direction of the snake every frame
dir = "N"
# N,S,E,W stands for North south east and west.

global game                         # Bool which keeps the game loop running.
game = True

ptime = time.time()  # Time as per by clock
dtime = time.time()  # Delta time i.e time between two iteration of loops
# cumulative time (we would check for this time while handling movements)
ctime = 0

global ate
# Bool to check whether snake has recently consumed any food
ate = False
global food
food = (random.randint(0, n), random.randint(0, n))  # Randomly placing food.


def checkInp():
    global dir

    ### Check for documentation of Keyboard module and find function
    ### which returns true when a specific key is pressed.
    ### use WASD movement and change the orientation of snake (dir) to NSEW accordingly.

    ### if kb.function_which_return_true_on_key(W):   #if W is pressed change direction to N and similarly for other directions.
    ###     dir = ??
    pass


def move():
    global ate
    global food
    global game

    head = sn[len(sn)-1]

    if food == head:
        ### randomize the food location again.
        ### What can you do with the ate variable??
        pass

    if dir == "N":
        ### if dir = N append the cell in north direction to head of the snake

        ### sn.append(cell to north of head)   #Choosing the next cell for snake depending on dir variable

        ### if snake has recently not consumed any food we need to remove cell at tail to keep the length of snake same.

        ### if snake not consumed recently:
        ###    delete(element at tail)
        pass

    ### Do same for all other directions South, West, and East

    head = sn[len(sn)-1]

    ### Now check if head has collided with borders of arena
    ### if head.x < arena_x_start or head.x > arena_x_end: #Checking for borders
    ###   How will you end the game here ?? Maybe look at the "game" variable.
    ###   print("Game Over")
    ### if head.y < arena_y_start or head.y > arena_y_end: #Checking for borders
    ###   How will you end the game here ?? Maybe look at the "game" variable.
    ###   print("Game Over")

    ate = False


# __main__
while(game):
    checkInp()  # check for input in every loop

    # Now we need to check if snake is biting itself.
    # That means ??
    # Snake array has duplicate elements.
    for h in sn:
        ### if h occurs more than once:  #Checking for snake biting itself
        ###   Stop game. Again, how? "game" variable?
        ###   print("Game Over")
        pass

    # resetting the screen after every iteration.
    a = [["." for i in range(n)] for j in range(n)]

    dtime = time.time() - ptime  # Assigning the value of deltatime
    ptime = time.time()  # assigning new value of time to ptime

    ### Increment ctime with dtime
    ### ctime = ctime + ??

    if(ctime > 0.5):  # moving the snake after 0.5 seconds of previous movement
        ### You need to reset ctime now so that it can again count to 0.5.
        ### Should snake move now??
        pass

    a[food[0]][food[1]] = "*"  # Assigning character  to food

    for i in sn:
        ### Assign different character '#' to snake cells
        pass

    os.system("cls")  # For linux/Mac use "clear"

    for i in a:
        for j in i:
            print(j, end="")  # printing the whole screen
        print()
