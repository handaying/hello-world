# Calculate the area of DC and Bubbling area.
# width: width to the edge.
import math
def area(width, diameter):
    R = diameter/2
    angle = math.acos((R-width)/R)
    a = (R**2)*(angle-math.sin(angle)*math.cos(angle))
    return a

#side_area = area(0.2,2)
#print(side_area)