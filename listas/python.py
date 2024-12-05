#progama que clasifique las edades que nos da el usuario
niños=0
adolescentes=0
adultos=0
ancianos=0

edad=int(input("¿Cuantas veces quieres clasificar las edades?"))

for edades in range(edad):
    if edad < 12:
        niños+=1
    else:
        if <=13 edad <=19:
            adolescentes+=1
        else: