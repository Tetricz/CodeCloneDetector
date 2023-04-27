m=float(input())/1000
if m<0.1:
    ans=0
elif 0.1 <= m <= 5:
    ans=int(m*10)
elif 6<= m <= 30:
    ans=int(m+50)
elif 35<= m <= 70:
    ans=int((m-30)/5+80)
elif 70 <= m:
    ans=89
print('{0:02d}'.format(ans))
