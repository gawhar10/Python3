"""
find area of
1. tiangle
    a. right angled
    b. any
2. square
3. rectangle
4. circle
"""
print("***Enter Choice***\n" +
      "for triangle: 1\n" +
      "for square: 2\n" +
      "for rectangle: 3\n" +
      "for circle: 4\n")
my_choice = int(input("Enter Choice: "))

if my_choice == 1:
    print("Enter\n" +
          "for right angled: 1\n" +
          "for any: 2")
    next_choice = int(input("Enter next choice: "))
    if next_choice == 1:
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        triangle_area = (base*height)/2
        print("Area of right angled triangle is: "+str(triangle_area))
    elif next_choice == 2:
        a = float(input("Enter side a: "))
        b = float(input("Enter side b: "))
        c = float(input("Enter side c: "))

        s = (a+b+c)/2
        any_triangle_area = (s*(s-a)*(s-b)*(s-c)) ** (1./2)
        print("Area of Any Triangle: "+str(any_triangle_area))
    else:
        print("Invalid input!")
elif my_choice == 2:
    side = float(input("Enter side: "))
    square_area = side*side
    print("Area of Square: " + str(square_area))
elif my_choice == 3:
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    rectangle_area = length*width
    print("Area of Rectangle: "+str(rectangle_area))
elif my_choice == 4:
    radius = float(input("Enter radius: "))
    circle_area = (radius*radius)*(22/7)
    print("Area of Circle: " + str(circle_area))
else:
    print("Invalid input!")
