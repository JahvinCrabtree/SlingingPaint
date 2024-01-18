import math

class PaintSlingers:
    def __init__(self):
        self.selectedPaint = None
        self.numberOfWalls = None
        self.wallArea = None
        self.hasObstruction = None
        self.obstructionArea = 0  # Initialize to 0

    def calculateArea(self, length, height):
        return length * height

    def calculateAreaCircle(self, radius):
        return math.pi * radius**2

    def calculateTriangleArea(self, base, height):
        return 0.5 * base * height

    def totalCost(self, paintRequired, costPerUnit=None):
        while costPerUnit is None or self.selectedPaint not in {'A', 'B', 'C'}:
            self.selectedPaint = input("Please select a valid paint option (A, B, or C): ").upper()
            if self.selectedPaint == "A":
                costPerUnit = 4.16 / 2.5
            elif self.selectedPaint == "B":
                costPerUnit = 22 / 2.5
            elif self.selectedPaint == "C":
                costPerUnit = 68.75 / 2.5
            else:
                print("Invalid input. Please select a valid paint option (A, B, or C): ")

        totalCost = paintRequired * costPerUnit
        return totalCost

    def getPaintOptions(self):
        paintOptions = """We have 3 different options of paint here

        A) Leyland - £4.16 for 2.5 Litres.
        B) Dulux - £22 for 2.5 Litres.
        C) YesColours - £68.75 for 2.5 Litres.

        The more premium options of paint have a better longevity"""
        print(paintOptions)
        print()

    def getWallInfo(self):
        try:
            self.numberOfWalls = int(input("Please enter the number of walls: "))
            if not (0 <= self.numberOfWalls < 100):
                print("Please enter a whole number less than 100.")
                return False  # Return False if the input is invalid
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            return False  # Return False if a ValueError occurs

        return True  # Return True if the input is valid

    def getObstructionInfo(self):
        try:
            self.hasObstruction = input("Is there an obstruction? (Y/N): ").upper()

            if self.hasObstruction == 'Y':
                obstructionType = input("Is the obstruction round, rectangle, triangle, or none? (Type 'round', 'rectangle' or 'triangle'): ").lower()

                radius = 0
                obstructionLength = 0
                obstructionHeight = 0

                match obstructionType:
                    case 'round':
                        radius = float(input("Enter the radius of the round obstruction: "))
                        self.obstructionArea = self.calculateAreaCircle(radius)
                    case 'rectangle':
                        obstructionLength = float(input("Enter the length of the rectangle obstruction: "))
                        obstructionHeight = float(input("Enter the height of the rectangle obstruction: "))
                        self.obstructionArea = self.calculateArea(obstructionLength, obstructionHeight)
                    case 'triangle':
                        base = float(input("Enter the base length of the triangular obstruction: "))
                        height = float(input("Enter the height of the triangular obstruction: "))
                        self.obstructionArea = self.calculateTriangleArea(base, height)
                    case _:
                        print("Invalid obstruction type. Please enter 'round', 'rectangle' or 'triangle'")
            elif self.hasObstruction == 'N':
                self.obstructionArea = 0
            else:
                print("Please, enter Y or N")
                return False  # Return False if the input is neither 'Y' nor 'N'
        except ValueError:
            print("Invalid input. Please enter a valid input.")
            return False  # Return False if a ValueError occurs

        return True  # Return True if the input is valid

    def calculatePaintRequired(self, length, height):
        self.wallArea = self.calculateArea(length, height)
        self.wallArea -= self.obstructionArea
        paintRequired = self.wallArea / 12.5
        return round(paintRequired, 1)

    def calculateTotalCost(self, paintRequired, costPerUnit=None):
        return round(self.totalCost(paintRequired, costPerUnit), 2)

greeting = """
Hello, welcome to B&Q.
We got paint, and lots of it.

"""
print(greeting)

paintSlingers = PaintSlingers()
paintSlingers.getPaintOptions()

# Ensure numberOfWalls is set before using it in the loop
if not paintSlingers.getWallInfo():
    print("Invalid input for the number of walls. Exiting.")
else:
    totalCostAllWalls = 0
    totalAmountPaint = 0
    for wall in range(paintSlingers.numberOfWalls):
        print(f"\nWall {wall + 1}")
        if not paintSlingers.getObstructionInfo():
            continue  # Skip to the next iteration if obstruction info is invalid

        height = float(input("Please enter the height of your wall in meters: "))
        length = float(input("Please enter the length of your wall in meters: "))

        paintRequired = paintSlingers.calculatePaintRequired(length, height)
        totalCost = paintSlingers.calculateTotalCost(paintRequired)

        totalCostAllWalls += totalCost
        totalAmountPaint += paintRequired

        print(f"The amount of paint required for Wall {wall + 1} is: {paintRequired} Litres, And that'll cost the very affordable price of £{totalCost:.2f}")
    print()
    print(f"The total amount of paint is: {totalAmountPaint} and the total cost is: {totalCostAllWalls}")