Score = input()
r,t = Score.split(':')
if t>r:
    print(2)
elif t<r:
    print(1)
else:
    print(0)

