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

if userPaintSelection == 'A':
    selectedPaint = "Simply Paint"
elif userPaintSelection == 'B':
    selectedPaint = "Dontlux"
elif userPaintSelection == 'C':
    selectedPaint = "DatGoodGood"
else:
    print("Invalid selection. Please choose A, B, or C.")

numerOfWalls = None

wallChoice = """Now you've selected your paint type, 
how many walls will you be painting?"""
print(wallChoice)
print()

numberOfWallsSelection = (input(int(("Please enter a whole number"))))



height = float(input("Please enter the height of your wall to a single decimal place "))
length = float(input("Please enter the length of your wall to a single decimal place "))

