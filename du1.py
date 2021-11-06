#Import fukncí modulu turtle
from turtle import circle, forward, left, right, penup, pendown, setpos, exitonclick, backward

print("Dobrý den, vítejte u hry piškvorky! Hra je určena pro dva hráče, můžete si zvolit libovolnou velikost hracího pole")

#Nastavení velikosti hracího pole
nx = (int(input("Zadej velikost hracího pole strany x: ")))
ny = (int(input("Zadej velikost hracího pole strany y: ")))

#Ošetření vstupů 
while nx <=0:
    print("Velikost strany hracího pole musí být kladné nenulové číslo ")
    nx = (int(input("Zadej znovu velikost hracího pole strany x: ")))
while ny <=0:
    print("Velikost strany hracího pole musí být kladné nenulové číslo ")
    ny = (int(input("Zadej znovu velikost hracího pole strany y: ")))

#Nastavení rychlosti vykreslovní, pomocné proměnné velikost a velikosti čtverce
speed = 10
velikost = nx*ny
a = 100

#Kreslení hracího pole
for _ in range(ny):
	for _ in range(nx):
		# Kreslení čtverce
		for _ in range(4):
			forward(a)
			left(90)
		# Posun na další
		forward(a)
	left(180)
	forward(nx*a)
	right(90)
	forward(a)
	right(90)

#Tělo hry 
#For cyklus pro opakovaní dotazů na kreslení, počet kol ošetřen proměnou velikost 
for i in range(velikost):
    #Podmínka na střídání hráčů
    if i % 2 == 0:
        print("Kolo", i+1, "Hraje první hráč, hraje s kolečky, souřadnice jsou kartézském systému, např. levý dolní roh má 1,1")
        x = (int(input("Zadej souřadnici X v kartézském systému: ")))
        y = (int(input("Zadej souřadnici Y v kartézském systému: ")))
        #Ošetření vstupů 
        while x > nx or x <= 0:
            print("Hraješ mimo hrací pole")
            x = (int(input("Zadej znovu souřadnici X v kartézském systému: ")))
        while y > ny or y <= 0:
            print("Hraješ mimo hrací pole")
            y = (int(input("Zadej znovu souřadnici  Y v kartézském systému: ")))
        #Převedení souřadnic na počátek
        xx = x*a-(a/2)
        yy = y*a-(a/2)
        #Kreslení kolečka 
        kresleni = (penup(),setpos(xx,yy),pendown(),circle(10), penup())   
    else: 
        print("Kolo", i+1, "Hraje druhý hráč, hraje křížky, souřadnice jsou kartézském systému, např. levý dolní roh má 1,1")
        x = (int(input("Zadej souřadnici Y v kartézském systému: ")))
        y = (int(input("Zadej souřadnici Y v kartézském systému: ")))
        while x > nx or x <= 0:
            print("Hraješ mimo hrací pole")
            x = (int(input("Zadej znovu souřadnici X v kartézském systému: ")))
        while y > ny or y <= 0:
            print("Hraješ mimo hrací pole")
            y = (int(input("Zadej znovu souřadnici Y v kartézském systému: ")))
        xx = x*a-(a/2)
        yy = y*a-(a/2)
        #Kreslení křížku 
        kresleni2 = (setpos(xx,yy), pendown()) 
        krizek = (right(45),forward(20), backward(40), forward(20), left(90), forward(20), backward(40), right(45))
print("Konec hry")
exitonclick()
		