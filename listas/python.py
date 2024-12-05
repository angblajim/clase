#progama que clasifique las edades que nos da el usuario
niños=0
adolescentes=0
adultos=0
ancianos=0

edades=int(input("¿Cuantas veces quieres clasificar las edades?"))

for i in range(edades):
    edad=int(input(f"Ingresa la edad {i+1}º:  "))
    if edad < 12:
        niños+=1
    else:
        if <12 edad <19:
            adolescentes+=1
        else:
            if <=20 edad <=55:
                adulo+=1
            else:
                anciano+=1
    
    print("")
    print("")
    print("")
