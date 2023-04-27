m = int(input())
km = m / 1000

if km < 0.1:
    vv = 0
elif km <= 5:
    vv = km * 10
elif km <= 30:
    vv = km + 50
elif km <= 70:
    vv = (km - 30) / 5 + 80
else:
    vv = 89

print("{:02.0f}".format(vv))