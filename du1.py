#Import fukncí modulu turtle
from turtle import circle, forward, left, right, penup, pendown, setpos, exitonclick, backward

print("Dobrý den, vítejte u hry piškvorky! Hra je určena pro dva hráče, můžete si zvolit libovolnou velikost hracího pole")

#Nastavení velikosti hracího pole
velikost_strany = (int(input("Nastav velikost strany čtverce (hodnota větší než 20, doporučuji 100): ")))
while velikost_strany < 20:
    print("Moc malé pole")
    velikost_strany = (int(input("Zadej znovu velikost čtverce 20 a víc ")))

#Počet hracích polí 
nx = (int(input("Zadej velikost hracího pole strany X: ")))
ny = (int(input("Zadej velikost hracího pole strany Y: ")))
#Ošetření vstupů 
while nx <=0:
    print("Velikost strany hracího pole musí být kladné nenulové číslo ")
    nx = (int(input("Zadej znovu velikost hracího pole strany X: ")))
while ny <=0:
    print("Velikost strany hracího pole musí být kladné nenulové číslo ")
    ny = (int(input("Zadej znovu velikost hracího pole strany Y: ")))

#Nastavení rychlosti vykreslovní, pomocné proměnné velikost a velikosti čtverce
speed = 10
velikost = nx*ny

#Kreslení hracího pole
for _ in range(ny):
	for _ in range(nx):
		# Kreslení čtverce
		for _ in range(4):
			forward(velikost_strany)
			left(90)
		# Posun na další
		forward(velikost_strany)
	left(180)
	forward(nx*velikost_strany)
	right(90)
	forward(velikost_strany)
	right(90)

#Tělo hry 
#For cyklus pro opakovaní dotazů na kreslení, počet kol ošetřen proměnou velikost 
for i in range(velikost):
    #Podmínka na střídání hráčů
    print("Kolo", i+1)
    x = (int(input("Zadej souřadnici X v kartézském systému: ")))
    y = (int(input("Zadej souřadnici Y v kartézském systému: ")))
     #Ošetření vstupů 
    while x > nx or x <= 0:
        print("Hraješ mimo hrací pole")
        x = (int(input("Zadej znovu souřadnici X v kartézském systému: ")))
    while y > ny or y <= 0:
        print("Hraješ mimo hrací pole")
        y = (int(input("Zadej znovu souřadnici Y v kartézském systému: ")))
    #Převedení souřadnic na počátek 
    xx = x*velikost_strany-(velikost_strany/2)
    yy = y*velikost_strany-(velikost_strany/2)
    #Křížek nebo koločko
    if i % 2 == 0:
        #Kreslení kolečka 
        penup()
        setpos(xx,yy)
        pendown()
        circle(velikost_strany/5)
        penup() 
    else: 
        #Kreslení křížku 
        setpos(xx,yy)
        pendown()
        right(45)
        forward(velikost_strany/5)
        backward(velikost_strany/2.5)
        forward(velikost_strany/5) 
        left(90) 
        forward(velikost_strany/5)
        backward(velikost_strany/2.5)
        right(45)
       
print("Konec hry")
exitonclick()		
