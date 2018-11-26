#!/usr/bin/python3
from random import randint
import getch
import sys
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format
"""================================================================================

                              V  A  R  I  A  B  L  E  S

================================================================================"""
coordinates_list = []
empty_coordinates_list = []

move = ""
start_pos = [14,14]
mov_coor = start_pos
planets_dict = {}
prev_coor = start_pos
l = list()

l = [['#']*30 for i in range(30)]

"""======================================================================
                          M O V E M E N T
-------------------------------------------------------------------------

                            START HERE
*************************************************************************

======================================================================"""

# def Start_pos(l = l):
#     """randomly generates the start position
#         Start position at the top."""
#     global start_pos
#     global mov_coor
#     start_pos =  [15, 15]
#     mov_coor = start_pos

#     if start_pos in empty_coordinates_list:
#         coordinates()
#     else:
#         empty_coordinates_list.append(coordinate)
#         lx = int(start_pos[0])
#         if start_pos[1] == 0:                          # x = 0 at the bottom
#             ly = 0
#         else:
#             ly = abs(int(start_pos[0] - 29))
#         l[lx][ly] = " "
#         return start_pos


def make_maze(l = l):
    """Prints the current maze"""
    global mov_coor
    global Avocado

    for i in l:
        print(" ".join(i))
    print("Life: ", end="")
    for i in range(Avocado.Life):
        print("🖤", sep=" ", end="", flush=True)
    print("{:>35}\n".format(str(mov_coor)))

def empty_space(array):
    """Creates an empty string on the l maze
       Takes an array with two elements  as parameters and extracts x,y from it.
    """
    global l
    global empty_coordinates_list
    #This is not needed anymore.
    # def x(x):
    #     if x == None:
    #         x = int(randint(0,30))
    #     return x

    # def y(y):
    #     if y == None:
    #         y = int(randint(0,30))
    #     return y
    # x(x)
    # y(y)
    coordinate = [array[0], array[1]]
    if l[array[0]][array[1]] == " ":
        print("Already visited empty place")            # print "already here"

    elif l[array[0]][array[1]] == '#':
        empty_coordinates_list.append(coordinate)
        y = coordinate[0]
        x = coordinate[1]
        l[y][x] = " "
        return coordinate


def discover(coordinate):
    """if randint = 1, 2 or 3 it will create a new planet
    (TODO) assign it to a new variable.
    Else: it will create an empty_space()"""

    global mov_coor
    global l
    lucky_number = [1, 2, 3]
    roll = randint(0, 12)

    if l[coordinate[0]][coordinate[1]] in " ":
        make_maze()
        print("Already visited space")
    elif l[coordinate[0]][coordinate[1]] == "O":
        print("Already discovered planet")
    else:
        if roll in lucky_number:
            # p3 = Planets(name_gen(), coordinate)            # debugging line
            create_planet(name_gen(), mov_coor)
        elif roll == 0:
            empty_space(coordinate)
            make_maze()
            print("An asteroid cloud... Maybe this was a planet before")

        elif roll == 4:
            empty_space(coordinate)
            make_maze()
            print("...Nothing...")

        else:
            empty_space(coordinate)
            make_maze()
            print("It's empty!")


def movement():
    global mov_coor

    def mov_up():
        global mov_coor
        x = mov_coor[1]
        y = mov_coor[0]
        if y - 1 == -1:
            make_maze()
            print("It's the end of the Universe!")
        else:
            y -= 1
            mov_coor = [y,x]
            print("up")
            discover(mov_coor)
            return mov_coor


    def mov_left():
        global mov_coor
        x = mov_coor[1]
        y = mov_coor[0]
        if x - 1 == 30:
            make_maze()
            print("It's the end of the Universe!")
        else:
            x -= 1
            mov_coor = [y,x]
            print("Left")
            discover(mov_coor)
            return mov_coor

    def mov_down():
        global mov_coor
        x = mov_coor[1]
        y = mov_coor[0]
        if y - 1 == 30:
            make_maze()
            print("It's the end of the Universe!")
            print("Go Up, Left or Right")
        else:
            y += 1
            mov_coor = [y,x]
            print("down")
            discover(mov_coor)
            return mov_coor

    def mov_right():
        global mov_coor
        x = mov_coor[1]
        y = mov_coor[0]
        if x + 1 == 30:
            make_maze()
            print("It's the end of the Universe!")
            print("Go Up, Left or Right")
        else:
            x += 1
            mov_coor = [y,x]
            print("right")
            discover(mov_coor)
            return mov_coor

# OLD movement (BROKEN)
#     def mov_up(mov_coor=mov_coor):
#         x = mov_coor[1]
#         y = mov_coor[0]
#         if y - 1 == -1:
#             make_maze()
#             print("It's the end of the Universe!")
#             print("Go Down, Left or Right")
#             movement()

#         else:
#             mov_coor[0] -= 1
#             discover(mov_coor)
#             print("Up")

#     def mov_left(mov_coor=mov_coor):
#         x = mov_coor[1]
#         y = mov_coor[0]
#         if x - 1 == 30:
#             make_maze()
#             print("It's the end of the Universe!")
#             print("Go Up, Down or Right")
#             movement()

#         else:
#             mov_coor[1] -= 1
#             discover(mov_coor)
#             print("Left")

#     def mov_down(mov_coor = mov_coor):
#         x = mov_coor[1]
#         y = mov_coor[0]
#         if y - 1 == 30:
#             make_maze()
#             print("It's the end of the Universe!")
#             print("Go Up, Left or Right")
#             movement()

#         else:
#             mov_coor[0] += 1
#             discover(mov_coor)
#             print("down")

#     def mov_right(mov_coor = mov_coor):
#         x = mov_coor[1]
#         y = mov_coor[0]
#         if x + 1 == 30:
#             make_maze()
#             print("It's the end of the Universe!")
#             print("Go Up, Left or Right")
#             movement()

#         else:
#             mov_coor[1] += 1           # I think x+1 is ->
#             discover(mov_coor)
#             print("right")


    print("Which way you want to go?")
    # move = input("Up, Down, Left, Right?: ")
    print("Use (WASD) keys to move")
    move = getch.getch()
    if move.lower() == "w":
        # avocado_sterling()
        mov_up()
        print("moving up")
        # discover(mov_coor)

        movement()
    elif move.lower() == "s":
        mov_down()
        # discover(mov_coor)
        movement()
    elif move.lower() == "a":
        mov_left()
        # discover(mov_coor)
        movement()
    elif move.lower() == "d":
        mov_right()
        # discover(mov_coor)
        movement()
    elif move == "i":
        show_planets(mov_coor)
        movement()
    elif move == "p":
        scan_planet(mov_coor)
        movement()
    elif move == "":
        print("exit movement()")
    else:
        print("Try again.")
        movement()

        #for the /real/ terminal only.
    # print("Which way you want to go?")
    # print("Use (WASD) keys to move")
    # move = getch.getch()        #
    # if move.lower() in "w":
    #     mov_up()
    #     movement()
    # elif move.lower() in "s":
    #     mov_down()
    #     movement()
    # elif move.lower() in "a":
    #     mov_left()
    #     movement()
    # elif move.lower() in "d":
    #     mov_right()
    #     movement()
    # elif move == "i":
    #     show_planets()
    # elif move == "p":
    #     scan_planet()
    # elif move == "":
    #     print("exit movement()")
    # else:
    #     print("exit movement()")

# def avocado_sterling():
#     global mov_coor
#     global prev_coor

#     var = l[prev_coor[0]][prev_coor[1]]

#     l[mov_coor[0]][mov_coor[1]] = "£"
#     l[prev_coor[0]][prev_coor[1]] = var
#     prev_coor = mov_coor


def scan_planet(mov_coor=mov_coor):
    global planets_dict
    key = tuple(mov_coor)
#    local_list = list(planets_dict[key])
    # for key, value in planets_dict.items():

        # if mov_tuple == mov_coor:
            # value.Scanned_Planet()
            # planets_dict.update({key: Scanned_Planet()})
    if l[mov_coor[0]][mov_coor[1]] == 'O':
        make_maze()
        planets_dict.update({key : Scanned_Planet()})
        print("{:15} {}".format("Name:", value.name))
        print("{:15} {}".format("Coordinates:", str(value.coor)))
        print("{:15} {}".format("Atmospher:", value.atmos))
        print("{:15} {}".format("Size:", value.size))
        print("{:15} {}".format("Life:", value.islife))
    else:
        make_maze()
        print("Error: There is a planet here already")
        print("no planet here")

def show_planets(mov_coor=mov_coor):
    for key, value in planets_dict.items():
#        if value.coor == mov_coor:
        print("{:15} {}".format("Name:", value.name))
        print("{:15} {}".format("Coordinates:", str(value.coor)))
        print("{:15} {}".format("Atmospher:", value.atmos))
        print("{:15} {}".format("Life:", value.islife))
        print("\n")
        # else:
        #     print("There is no Planet on {}".format(mov_coor))



"""=====================================================================
                           P L A N E T S
------------------------------------------------------------------------

                            START HERE
************************************************************************

====================================================================="""

def name_gen():
    i = 0
    name = chr(randint(97,122))
    how_long = randint(3,10)
    while len(name) <= how_long:
        if i == 200000:
            break
        else:
            character = chr(randint(97,122))
            if character in "aeiou":                # if c is vowel
                if name[-1] not in "aeiou":         # if previous is consonant
                    name += character

            else:                                   # if c is consonant
                if name[-1] in "aeiou":             # if previous was vowel
                    name += character
                elif name[-1] in "mnp":             # previous was "mnp"
                    name += character
                elif name[-1] in "bpsmnr" and character in "rslmn":
                    name += character
                    i += 1
    name = name.capitalize()
    return name

def create_planet(name, coordinate):
    global planets_dict
    global mov_coor
    key = tuple(coordinate)

    def planet_lookup(coordinate):
        for key, value in planets_dict.items():
            if value.coor == coordinate:
                make_maze()
                print("Planet {}, Coordinates {}".format(value.name, value.coor))
                print("{} for debugin".format(key))

    if l[coordinate[0]][coordinate[1]] == 'O':
        make_maze()
        print("Error: There is a planet here already")
    else:
        l[coordinate[0]][coordinate[1]] = "O"
        make_maze()
        coordinates_list.append(coordinate)
        planets_dict.update({key : Planets(name, mov_coor)})
        planet_lookup(coordinate)



# this code randomly generates a position in l.
# def coordinates():
#     global coordinate
#     global coordinates_list
#     def x():
#         x = int(randint(0,30))
#         return x

#     def y():
#         y = int(randint(0,30))
#         return y
#     x()
#     y()
#     coordinate = [x,y]
#     if coordinate in coordinates_list:
#         coordinates()
#     else:
#         coordinates_list.append(coordinate)
#         ly = coordinate[0]
#         if coordinate[1] == 0:                          # x = 0 at the bottom
#             lx = 0
#         else:
#             lx = coordinate[1]
#         l[lx][ly] = "@"
#         return coordinate


class Planets:

    global coordinates_list
    size = "Unknown."
    atmos = "Unknown."
    islife = "Unknown."
    notes = "No notes available"

    def __init__(self, name, coordinate):
        self.name = name
        self.coor = coordinate
        print("Initizalizing {} on {}".format(self.name, self.coor))

    # def ship_scanner(self, size, atm, live, resources):
    #     self.size = size_gen()
    #     self.atm = atm()
    #     self.live = is_live()
    #     self.res = resources()


def size_gen(self):
    Planets.size = (randint(0, 100))**2
    return Planets.size

def atmos_gen(self):
    atmos_list_1 = ["Oxigen present", "Oxigen detected", "Low Oxigen", "No oxigen"]
    atmos_list_2 = ["Poisonous gases detected", "No poisonous gases detected", "Some poisonous gas detected"]
    atmos_list_3 = ["Dry", "water detected", "Sea-Wide Planet"]
    atmos_list_4 = ["Lighting storms common", "No rainy season", "Sand Storms"]
    Planets.atmos = [atmos_list_1[randint(0,2)], atmos_list_2[randint(0,2)], atmos_list_3[randint(0,2)], atmos_list_4[randint(0,2)]]

def life_gen(self):
    life_list_1 = ["Microscopic organisms", "Barren", "Only vegetation", "Animals detected", "Dangerous animals"]
    Planets.islife = [life_list_1[randint(0,4)]]

class  Scanned_Planet:
        var = "Unknown."
        def __init__(self, name, coor, size, atmos, life):
            super().__init__(self, name, coor)
            self.size = size
            self.atmos = atmos
            self.islife = life

            if self.size != var:
                print("This planet was scanned already!")
                print("{:15} {}".format("Name:", self.name))
                print("{:15} {}".format("Coordinates:", str(self.coor)))
                print("{:15} {}".format("Atmospher:", self.atmos))
                print("{:15} {}".format("Life:", self.islife))
            else:

                # Planets.size_gen(self)
                # Planets.atmos_gen(self)
                # Planets.life_gen(self)

"""======================================================================
                           A V O C A D O
======================================================================"""

class StarShipAvocado:
    name = "Avocado"
    Life = 11
    global mov_coor

    def __init__(self):
        self.name

    def AvoPos(self):
        global mov_coor
        avo_pos = mov_coor
        return avo_pos


    def Damage(self, damg):
        self.Life -= damg


Avocado = StarShipAvocado()


# planets_dict = {}
# def Create_planet(name, coordinate):
#     global planets_dict
#     planets_dict.update({"planet_" + (str(len(planets_dict) + 1)) : Planets(name, coordinate)})
#     print(planets_dict)


# Create_planet("asdf", [22,12])
# Create_planet("lkjh", [13,13])

# for key, value in planets_dict.items():
#     print(key, value.name, value.coor)

def main():
    global start_pos
    global coordinates_list
    global coordinate
    global mov_coor
    global planets_dict
    ans = ''
    # Print start
    cprint(figlet_format('STAR AVOCADO', font='starwars'),
       'yellow', 'on_red', attrs=['bold'])
    print("WELCOME")
    empty_space(start_pos)
    make_maze()

    movement()
    ans = input("do you really want to exit? Y/N > ")
    if ans.lower() in "qyes":
        print("Thank you for playing")
        print("Program Finished")
    else:
        movement()


main()
