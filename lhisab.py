#!/usr/bin/python
#Filename; helloworld.py
#==========================================#
def area_rect():
 lenght=int(input("plaes enter your lenght : "));
 wight =int(input("plaes enter your wight  : "));	
 area1 = lenght * wight
 print ("the area  is ",area1 );
 area_rect()
def area_cercle():
 radius=int(input("plaes enter your radius :"));
 area2 = radius * radius * 3.14
 print ("the area  is",area2) ;
area_cercle()
def area_square():
 side=int(input("plaes enter your side :"));
 area3= side * side 
 print ("the area  is ",area3) ;
area_square()   
def area_triangle():
 base=int(input("plaes enter your base :"));
 height=int(input("plaes enter your height :"));
 area4= base * height / 2
 print ("the area  is ",area4) ;
area_triangle()
def area_trapeze():
 small_base=int(input("plaes enter your small base :"));
 big_base=int(input("plaes enter your big base :"));
 height=int(input("plaes enter your height :"));
 area5= (small_base + big_base) * height / 2
 print ("the area  is ",area5) ;
area_trapeze()
#============================================#
def surrraundings_triangle():
	side1 =int(input('please entre your side1'));
	side2 =int(input('please entre your side2'));
	side3 =int(input('please entre your side3'));
	surraundings=side1 + side2 + side3
	print (surraundings)
surrraundings_triangle()  
def surrraundings_square():
	side =int(input('please entre your side'));
	surraundings=side * 4
	print (surraundings)
surrraundings_square()
def surrraundings_rectangle():
	wight=int(input('please entre your wight'));
	lenght=int(input('please entre your lenght'));
	surraundings=(wight + lenght) * 2
	print (surraundings)
surrraundings_rectangle()
def surrraundings_trapeze():
	side1 =int(input('please entre your side1'));
	side2 =int(input('please entre your side2'));
	side3 =int(input('please entre your side3'));
	surraundings=side1 + side2 + side3	
	print (surraundings)
surrraundings_trapeze()
def surrraundings_cercle():
	radius =int(input('please entre your radius'));
	surraundings=radius * 3.14
	print (surraundings)
surrraundings_cercle()
   	
	 
 
 	
