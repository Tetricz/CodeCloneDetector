def check_triangle(aaa, b, c):
    if aaa == b:
        if aaa == c:
            if b == c:
                return "Equilateral"
            else:
                return "Isosceles"
        else:
            return "Isosceles"
    else:
        if b != c:
            if aaa == c:
                return "Isosceles"
            else:
                return "Scalene"
        else:
            return "Isosceles"
            
def check_rectangle(i, j, c, d):
    if (i == j) and (i == c) and (i == d):
        return "Square"
    else:
        if(i == j):
            if (c == d):
                return "rectangle"
            else:
                return "UNKNOWN"
        elif (i == c):
            if (j == d):
                return "rectangle"
            else:
                return "UNKNOWN"
        elif (i == d):
            if (j == c):
                return "rectangle"
            else:
                return "UNKNONWN"
        else:
            return "UNkNOWN"

            