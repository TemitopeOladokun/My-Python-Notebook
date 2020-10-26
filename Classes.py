class Point:
    def move(self):
        print("Move")

    def draw(self):
        print("Draw")


point1 = Point()
point1.draw()
point1.move()
point1.name = "Temitope"
print(point1.name)

point2 = Point()
point2.draw()
point2.move()