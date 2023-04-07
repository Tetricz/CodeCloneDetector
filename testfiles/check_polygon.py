import os  # this is just for decoration to test the program
import math # so is this
# the above imports are just stuff

def check_triangle(a, b, c):
# next line is blank

# next line is 5 whitespaces
     
       # indented comment
    if a == b:
        if a == c:
            if b == c:
                return "Equilateral"  # found 
            else:
                return "Isosceles"
        else:
            return "Isosceles"
    else:
        if b != c:
            if a == c:
                return "Isosceles"
            else:
                return "Scalene"
        else:
            return "Isosceles"
            
def check_rectangle(a, b, c, d):
    if (a == b) and (a == c) and (a == d):
        return "Square"
    else:
        if(a == b):
            if (c == d):
                return "rectangle"
            else:
                return "UNKNOWN"
        elif (a == c):
            if (b == d):
                return "rectangle"
            else:
                return "UNKNOWN"
        elif (a == d):
            if (b == c):
                return "rectangle"
            else:
                return "UNKNONWN"
        else:
            return "UNkNOWN"

            