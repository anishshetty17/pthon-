#CENTROID OF A TRIANGLE
print('Assume the three sides(coordinates) of a triangle to be A(p,q), B(r,s) & C(t,u)')
p = int(input('p : '))
q = int(input('q : '))
print('The coordinates of side A is ' , (p,q))
r = int(input('r : '))
s = int(input('s : '))
print('The coordinates of side B is ' , (r,s))
t = int(input('t : '))
u = int(input('u : '))
print('The coordinates of side C is' , (t,u))
print('Let the centroid be having vertices and coordinates as X(v,w)')
v = (p + r + t) / 3
w = (q + s + u) / 3
print('The centroid of triangle is ' , (v,w))