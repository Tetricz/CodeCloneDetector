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
