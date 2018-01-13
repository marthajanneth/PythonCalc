def Menu()
    #Función que Muestra el Menu
    print("Calculadora")

    print("Menu")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")

def Calculadora()
    #Funcion Para Calcular Operaciones Aritmeticas
    Menu()
    opc = int(input(Selecione Opcionn))
    while (opc 0 and opc 5)
        x = int(input(Ingrese Numeron))
        y = int(input(Ingrese Otro Numeron))
        if (opc==1)
            print La Suma es, x+y
            opc = int(input(Selecione Opcionn))
        elif(opc==2)
            print La Resta es,x-y
            opc = int(input(Selecione Opcionn))
        elif(opc==3)
            print La Multiplicacion es,xy
            opc = int(input(Selecione Opcionn))
        elif(opc==4)
            try
              print La Division es, xy
              opc = int(input(Selecione Opcionn))
            except ZeroDivisionError
              print No se Permite la Division Entre 0
              opc = int(input(Selecione Opcionn))
Calculadora()
