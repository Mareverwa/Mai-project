from figures import circle_perimeter,circle_area,default_radius
from figures import triangle_area,triangle_perimeter,def_a,def_b,def_c
from figures import square_area,square_perimeter,default_a


 #circle test cases r=defualt_radius
print(f'Area of a circumference of a circle with radius {default_radius} is {circle_perimeter()}')
print(f'Area of a circle with radius {default_radius} is {circle_area()}')
#triangle test cases with side def_a ,def_b , def_c
print(f'Area of a triangle with  sides {def_a} {def_b} {def_c} is {triangle_area()}')
print(f'Perimeter  of a triangle with sides {def_a} {def_b} {def_c} is {triangle_perimeter()}')
#perimeter test cases 
print(f'Area of a sqaure with sides {default_a} is {square_area()}')
print(f'Perimeter of a square with sides {default_a} is {square_perimeter()}')