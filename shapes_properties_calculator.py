#!/usr/bin/python
#Filename; helloworld.py


while True:
	lenght=input("plaes enter your lenght : ");
	wight =input("plaes enter your wight  : ");
	area  = wight * lenght
	print "the area  is ",area ;
	print '''the area   of  : 
		-rect
		-cercal '''
	typ= raw_input (" please enter your chose : ");

	if typ == "rect":
		print " True"
	elif typ == "cercal":
		print" False"      
	else:
		print"this don't chose"
	qui=raw_input("Do you want to try more ? ")
	if qui== "yes":
		continue
	if qui== "no":
		break
	






















