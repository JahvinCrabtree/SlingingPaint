import math #Numbers and that.

def calculateArea(length, height):
    return length * height

def calculateAreaCircle(radius):
    return math.pi * radius**2 # ** 2 means squared. 

def totalCost(wallArea, numberOfWalls, selectedPaint):
    if selectedPaint == "Simply Paint":
        cost_per_square_unit = 10
    elif selectedPaint == "Dontlux":
        cost_per_square_unit = 20
    else:
        cost_per_square_unit = 30
    
    total_cost = wallArea * numberOfWalls * cost_per_square_unit
    return total_cost

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

A) Simply Paint - £10 for 2.5 Litres.
B) Dontlux - £20 for 2.5 Litres.
C) DatGoodGood - £30 for 2.5 Litres.

The more premium options of paint give for a better finish and makes a house a home. """
print(paintOptions)
print()

selectedPaint = None

while selectedPaint is None:
    selectedPaint = input("Please select a paint option (A, B, or C): ")

    if selectedPaint not in ['A', 'B', 'C']:
        print("Invalid selection. Please choose A, B, or C.")
        selectedPaint = None 
print()

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

wallArea = calculateArea(height, length)

sum = totalCost(wallArea, numberOfWalls, selectedPaint)
print ("That'll be the very affordable price of £" + str(sum))

