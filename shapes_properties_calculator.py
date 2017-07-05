import affichage
import lhisab
 



 menuItems = {
	"1" : "Area",
	"2" : "Surrounding",
	
}



menuchoice = {
	"1":"rect",
    "2":"triangle",
    "3" :"square",
	"4" :"trapeze",
	"5" :"cercle" ,
}



choice = affichage.menu(menuItems)


CHoice=input('enter your choice :  ')


    if CHoice=="1" :
     Choice = affichage.menu(menuchoice)
     CHOice=input('enter your choice :  ')
     if CHOice=='1' :
        A_r= lhisab.area_rect();
 
     if CHOice=='2' :
        A_t= lhisab.area_triangle();
	   
     if CHOice=='3' :
        A_s= lhisab.area_square();
	   
     if CHOice=='4' :
        A_tr= lhisab.area_trapeze();
	 
     if CHOice=='5' :
        A_c= lhisab.area_cercle();   

#============================================#



    if CHoice=="2" :
     Choice = affichage.menu(menuchoice)
     CHOice=input('enter your choice :  ')
     if CHOice=='1' :
        S_r= lhisab.surrraundings_rect();
 
     if CHOice=='2' :
        S_t= lhisab.surrraundings_triangle();
	   
     if CHOice=='3' :
        S_s= lhisab.surrraundings_square();  
     if CHOice=='4' :
        S_tr= lhisab.surrraundings_trapeze();
	 
     if CHOice=='5' :
        S_c= lhisab.surrraundings_cercle();  

    






