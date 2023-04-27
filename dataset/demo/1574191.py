m = int(input())
km = m / 1000
if km < 0.1:
    VV = 0
elif km <= 5:
    VV = km * 10
elif km <= 30:
    VV = km + 50
elif km <= 70:
    VV = ((km - 30) / 5) + 80
else:
    VV = km = 89
print("{0:02d}".format(int(VV)))
