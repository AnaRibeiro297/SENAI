# -*- coding: UTF-8 -*-

n= [0,0,0,0]
s = 0
x = 0

while x < 4:
    n[x] = float(input("n %d: "% x))
    s += n[x]
    x+= 1
x = 0
while x < 4:
    print("n %d: %6.2f" %(x,n[x]))
    x += 1
print("A média: %5.2f" % (s/ x))

