R = int(input('radii of first circle:'))
print(R)
x = int(input('abscissa of first circle is:'))
print(x)
y = int(input('ordinate of first circle is:'))
print(y)
r = int(input('radii of second circle:'))
print(r)
m = int(input('abscissa of second circle is:'))
print(m)
n = int(input('ordinate of second circle is:'))
print(n)
d = ((x-m)**2+(y-n)**2)**0.5
print(d)
if(R-r<d<R+r):
	print('circles intersect')
else:
	print('circles dont intersect')