import numpy as np
edificio = []
Compradores = []
rut_compradores = []
departamento = np.zeros([10,5], dtype=object)
precio_A = 3800
precio_B= 3000
precio_C=2800
precio_D=3500

def menu():
    print("1) Mostrar Departamentos en venta disponibles")
    print("2) Comprar departamento")
    print("3) Ver Compradores")
    print("4) Buscar Compradores")
    print("5) Reasignar compra")
    print("6) Mostrar Ganancias totales")
    print("7) Salir")

def nuevacompra():
    print("Desea reasignar comprador")

def salir():
    print("Gracias")
continuar = True
while continuar:
    menu()
    validamenu = True
    while validamenu:
        try:
            opcion = int(input("Seleccione Opción: "))
            if opcion < 1 or opcion > 7:
                print("Ingrese una opcion válida.")
            else:
                validamenu = False
        except ValueError:
            print("Oops! No es valida la opcion.Intente nuevamente...")

    if opcion == 1:
        departamento[0,0] = "10"
        departamento[1,0] = "09"
        departamento[2,0] = "08"
        departamento[3,0] = "07"
        departamento[4,0] = "06"
        departamento[5,0] = "05"
        departamento[6,0] = "04"
        departamento[7,0] = "03"
        departamento[8,0] = "02"
        departamento[9,0] = "01"
        a = 0
        print(departamento)
        print("       A-B-C-D")
        print("Pisos    Tipos")
        print("-----------------------------")
        print("Departamentos disponibles = 0")
        print("--Departamentos Comprados = X")
        print("-----------------------------")

    elif opcion == 2:
        comprador = np.zeros(6, dtype=object)
        departamento[0,0] = "10"
        departamento[1,0] = "09"
        departamento[2,0] = "08"
        departamento[3,0] = "07"
        departamento[4,0] = "06"
        departamento[5,0] = "05"
        departamento[6,0] = "04"
        departamento[7,0] = "03"
        departamento[8,0] = "02"
        departamento[9,0] = "01"
        a=0
        b=0
        c=0
        print("-----------------------------")
        print("INGRESAR DATOS DEL COMPRADOR")
        print("-----------------------------")
        rut = int(input("RUT(Sin digito verificador): "))
        rut_compradores.sort
        rut_compradores.append(rut)
        comprador[0]=rut
        nombre= input("Nombre: ")
        comprador[1] = nombre
        apellido = input("Apellido: ")
        comprador[2] = apellido
        edad = input("Edad: ")
        comprador[3] = edad

        piso = int(input("Seleccione Piso(1-10):"))
        dpto = int(input("Seleccione Departamento(1-4):"))
        departamento [10-piso,dpto] = "X"
        print(departamento)
        edificio.append(departamento)
        comprador[4]=piso
        comprador[5]=dpto
        Compradores.append(comprador)
    elif opcion == 3:
        rut_compradores =[]
        for i in range(len(Compradores)):
            rut_comprador=Compradores[i][0]
            rut_compradores.append(rut_comprador)
        rut_compradores.sort
        print(rut_compradores)

    elif opcion == 4:
        rut = input("Ingrese Rut a buscar: ")
        rut = int(rut)
        for i in range(len(Compradores)):
            if rut in Compradores[i]:
                print("Se encontro el comprador:", Compradores[i])
                break
            else :
                print("El rut ingresado no existe en la lista de compradores.")

    elif opcion == 5:
        rut = input("Ingrese Rut a anular: ")
        rut = int(rut)
        for i in range(len(Compradores)):
            if rut in Compradores[i]:
                print("Se anulará esta compra: ", Compradores[i])
                confi_nueva_compra = input("Ingrese 1 si esta seguro de ingresar un nuevo comprador para el departamento:  ")
                confi_nueva_compra = int(1)
                if confi_nueva_compra == 1:
                    comprador_a_cambiar = Compradores[i]
                    nuevo_rut = input("Rut del nuevo comprador sin digito verificador: ")
                    comprador_a_cambiar[0] = int(nuevo_rut)
                    nuevo_nombre = input("Nombre: ")
                    comprador_a_cambiar[1] = nuevo_nombre
                    nuevo_apellido = input("Apellido: ")
                    comprador_a_cambiar[2]=nuevo_apellido
                    nuevo_edad = input("Edad: ")
                    comprador_a_cambiar[3] = nuevo_edad
        print("se ha resignado la compra")
    elif opcion == 6:
        A = 0
        B = 0
        C = 0
        D = 0
        pisos_A = []
        pisos_B = []
        pisos_C = []
        pisos_D = []
        for i in range(len(departamento)):
            if "X" == departamento[i][1]:
                A = A+1
                pisos_A.append(i)
            if "X" ==  departamento[i][2]:
                B = B +1
                pisos_B.append(i)
            if "X" ==  departamento[i][3]:
                C = C +1
                pisos_C.append(i)
            if "X" ==  departamento[i][4]:
                D = D +1
                pisos_D.append(i)
        # totales
        total_A = precio_A*A
        total_B = precio_B*B
        total_C = precio_C*C
        total_D = precio_D*D
        # recargas
        recargo_A = 0
        for j in range(len(pisos_A)):
            if pisos_A[j]>2:
                recargo_A = 100 + recargo_A
        recargo_B = 0
        for j in range(len(pisos_B)):
            if pisos_B[j]>2:
                recargo_B = 100 + recargo_B
        recargo_C = 0
        for j in range(len(pisos_C)):
            if pisos_C[j]>2:
                recargo_C = 100 + recargo_C
        recargo_D = 0
        for j in range(len(pisos_D)):
            if pisos_D[j]>2:
                recargo_D = 100 + recargo_D
        Total_num = A+B+C+D
        Total_total = total_A+total_B+total_C+total_D
        recargo_total = recargo_A+recargo_B+recargo_C+recargo_D
        Total_Total = Total_total + recargo_total

        print(["Tipo de Departamento" , "Cantidad", "Total","Recargo por piso", "", ""])
        print(["Tipo A "+""+"3800 UF  ",str(A), str(total_A)+" UF", str(recargo_A)+ " UF",""])
        print(["Tipo B "+""+"2000 UF  ",str(B), str(total_B)+" UF", str(recargo_B)+ " UF",""])
        print(["Tipo C "+""+"2500 UF  ",str(C), str(total_C)+" UF", str(recargo_C)+ " UF",""])
        print(["Tipo D "+""+"3500 UF  ",str(D), str(total_D)+" UF", str(recargo_D)+ " UF",""])
        print(["Total  "+""+""+str(Total_num),str(Total_total)+" UF"," + " + str(recargo_total)+ " UF = ",str(Total_Total)+ " UF"])

    elif opcion ==7:
            salir()
            continuar = False
