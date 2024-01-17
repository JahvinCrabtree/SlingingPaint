import math #Numbers and that.

def calculateArea(length, width):
    return length * width

def calculateAreaCircle(radius):
    return math.pi * radius**2 # ** 2 means squared. 

print()

greeting = """Hello, welcome to PaintSlingers LTD.
We got paint, and lots of it."""
print(greeting)
#empty line simulator.
print()

parameters = """When painting a wall you should know to cover 12sqm of wall,
you need 1l of paint, take that into consideration when purchasing. :)"""
print(parameters)
print()

paintOptions = """We have 3 different options of paint here

A) Simply Paint - £3 for .5 Litres, £10 for 2.5 Litres, £15 for 4 Litres.
B) Dontlux - £6 for .5 Litres, £20 for 2.5 Litres, £30 for 4 Litres.
C) DatGoodGood - £9 for .5 Litres, £30 for 2.5 Litres, £45 for 4 Litres. 

The more premium options of paint give for a better finish and makes a house a home. """
print(paintOptions)
print()

userPaintSelection = (input("""Which paint would you like?
                            A
                            B
                            C"""))

selectedPaint = None

while selectedPaint is None:
    selectedPaint = input("Please select a paint option (A, B, or C): ")

    if selectedPaint not in ['A', 'B', 'C']:
        print("Invalid selection. Please choose A, B, or C.")
        selectedPaint = None 

wallChoice = """Now you've selected your paint type, 
how many walls will you be painting?"""
print(wallChoice)
print()

numberOfWalls = None

while numberOfWalls is None:
    try:
        numberOfWalls = int(input("Please enter the amount of walls: "))
        if 0 <= numberOfWalls < 100:
            # No need to assign to numberOfWallsSelection, directly use numberOfWalls
            pass  # You can add more logic here if needed
        else:
            print("Please enter a whole number less than 100.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")

print("Do these walls have any obstructions? Windows etc. ")
print()

hasObstruction = None

while hasObstruction is None:
    hasObstruction = input("Please enter Y or N: ")
    if hasObstruction not in['Y', 'N']:
        print("Invalid selection, try again.")
        hasObstruction = None







height = float(input("Please enter the height of your wall to a single decimal place "))
length = float(input("Please enter the length of your wall to a single decimal place "))

