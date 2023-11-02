# 31.	Let x and y denote the coordinates of a point on the plane. Write a program that determines in which quadrant of the coordinate system 
# the point P (x, y) is located or on which axis it is located, or that it is located in the position (0,0) of the coordinate system. 
# Sample result:
# x = 5
# y = 2
# Point P(5,2) is in the first quadrant of the coordinate system

x = 5
y = 2

if x > 0:
    if y > 0:
        print("First quadrant")
    elif y < 0:
        print("Fourth quadrant")
    else:
        print("OX axe")
elif x < 0:
    if y > 0:
        print("Second quadrant")
    elif y < 0:
        print("Third quadrant")
    else:
        print("OX axe")
elif x == 0 and y > 0 or y < 0:
    print("OY axe")
else:
    print("(0,0) point")