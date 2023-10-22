tekst = str(input("Podaj tekst: "))

if(len(tekst)%2==1):
    szerokosc = 7+int(len(tekst)/2)*2
    wysokosc = 4+int(len(tekst)/2)
    z = int(szerokosc/2)
    x = z
else:
    szerokosc = 6+len(tekst)
    wysokosc = 3+int(len(tekst)/2)
    z = szerokosc/2
    x = z-1

for i in range (wysokosc):
    for j in range (szerokosc):
        if(i==wysokosc-2):
            print(" * " + tekst + " *", end="")
            break
        else:
            if(j==z or j==x or i==wysokosc-1):                 
                print("*", end="")
            else:
                print(" ", end="")
    z = z+1
    x = x-1
    print("")