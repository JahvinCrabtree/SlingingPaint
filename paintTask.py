import math # </3
class PaintSlingers:
    def __init__(self):
        self.selectedPaint = None
        self.numberOfWalls = None
        self.wallArea = None
        self.hasObstruction = None

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

        totalCost = (paintRequired * costPerUnit)
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
        while True:
            try:
                self.numberOfWalls = int(input("Please enter the amount of walls: "))
                if 0 <= self.numberOfWalls < 100:
                    break  # Exit the loop if the input is valid
                else:
                    print("Please enter a whole number less than 100.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    def getObstructionInfo(self):
        self.hasObstruction = input("Is there an obstruction? (Y/N): ").upper()
        validObstruction = False
        
    def getObstructionInfo(self):
        try:
            self.hasObstruction = input("Is there an obstruction? (Y/N): ").upper()

            if self.hasObstruction == 'Y':
                validObstruction = True  # Set this to True to break out of the loop
            elif self.hasObstruction == 'N':
                self.obstructionArea = 0
                validObstruction = True
            else:
                print("Please, enter Y or N")
                return  # Return to the caller if the input is neither 'Y' nor 'N'
        except ValueError:
            print("Invalid input. Please enter a valid input.")
            return  # Return to the caller if a ValueError occurs

        # Now, handle the obstruction type input
        try:
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
        except ValueError:
            print("Invalid input. Please enter a valid input.")

    def calculatePaintRequired(self):
        self.wallArea = self.calculateArea(height, length) * numberOfWalls
        self.wallArea -= self.obstructionArea
        paintRequired = self.wallArea / 12.5
        return round(paintRequired, 1)

    def calculateTotalCost(self):
        paintRequired = self.calculatePaintRequired()
        costPerUnit = None # totalcost solves thispytho
        return round(self.totalCost(paintRequired, costPerUnit), 2)



greeting = """
Hello, welcome to B&Q.
We got paint, and lots of it.

"""
print(greeting)

paintSlingers = PaintSlingers()
paintSlingers.getPaintOptions()

paintSlingers.getWallInfo()
paintSlingers.getObstructionInfo()

height = float(input("Please enter the height of your wall in meters: "))
length = float(input("Please enter the length of your wall in meters: "))
print()

numberOfWalls = paintSlingers.numberOfWalls

paintRequired = paintSlingers.calculatePaintRequired()
totalCost = paintSlingers.calculateTotalCost()

print(f"The amount of paint required is: {paintRequired} Litres, And that'll cost the very affordable price of £{totalCost:.2f}")