n = int(input())
if n < 100:
    print("00")
elif n <= 5000:
    print("{:02}".format(n//100))
elif n<= 30000:
    print(n//1000+50)
elif n<=70000:
    print((n-30000)//5000+80)
else:
    print(89)
