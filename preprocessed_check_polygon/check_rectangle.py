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
