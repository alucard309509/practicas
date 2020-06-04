###Definir valrores de productos como arrays
##al mostrar el menu imprimir los arrays
#importar la libreria random
##y elegir prodcutos al azar
##opciones de cliente:
#1 - no
#2 - si
#3 - Claro
#4 - Por supuesto
#5 - Mejor hagame el amor
#6 - Ponme en 4 y dame duro por el cucurucho papi


##solo abrir o cerrar tienda sera ingresado por teclado
#leche = ["cantidad: ", 100, "precio: ", 20]
#1 - leche
#2- huevo
#3 coca
#4 sabritas
##random.randint(1,4)
#cantidad = random.randint(0,100)

import random


informedeldia=["clientes",0,"venta_total",0,"total_cliente",0,"total_productos",0]

ventasentotalidad=["venta_por_cliente",0,"ven_total_sabritas",0,"ven_total_huevo",0,"ven_total_leche",0,"ven_total_coca",0]

totales=["total_leche",0,"total_huevo",0,"total_sabritas",0,"total_coca",0]

canes=["can_sabritas",0,"can_leche",0,"can_huevo",0,"can_coca",0]

producto = 0

cantidad = 0

cantidadporcliente=["huevo_por_cliente",0,"leche_por_cliente",0,"coca_por_cliente",0,"sabritas_por_cliente",0]

leche=["cantidad",100, "precio", 20]

huevo=["cantidad",100,"precio",18.5]

sabritas=["cantidad",100,"precio",12.5]

coca=["cantidad",100,"precio",25]

productor=["leche","huevo","sabritas","coca"]

comparador1 = 0
comparador2 = 0


res = input("Cerrar tienda?: ")
while(res!="si"):
    res2 = input("Comprar producto?: ")
    while(res2 != "no"):
        ##if(coca == 0 and huevo == 0 and leche == 0 and sabritas == 0):
        if(comparador1 == leche[1] and comparador1 == huevo[1] and comparador1 == sabritas[1] and comparador1 == coca[1] ):
             print("La tienda ha cerrado, productos agotados")
             break
        else:
            print("###############PRODUCTOS############### \n leche - $20 \n huevo - $18.5 \n sabritas - 25 \n coca - 12.5 \n\n ############################")
            ##producto = input("Ingresar producto a comprar: ")
            producto = random.choice(productor)
            if(producto == "leche"):
        ##    if(producto == "leche"):
                #cantidad = random.randint(0,100)
                ##cantidad = int(input("Ingresar cantidad de leche a llevar: "))
                cantidad = random.randint(1,leche[1])
                if(cantidad > leche[1]):
                    print("No se tiene esa cantidad de leche")
                else:

                    totales[1]= leche[3]*cantidad
                    leche[1] = leche[1] - cantidad
                    canes[3] = canes[3]+cantidad
                    ventasentotalidad[7] = ventasentotalidad[7]+totales[1]
                    cantidadporcliente[3] = cantidadporcliente[3] + cantidad


            elif(producto == huevo[1]):
                cantidad = random.randint(1,huevo[1])
                ##cantidad = int(input("Ingresar cantidad de huevo a llevar: "))
                if(cantidad > huevo[1]):
                    print("No se tiene esa cantidad de huevo")
                else:

                    totales[1]= huevo[3] * cantidad
                    huevo[1] =huevo[1] - cantidad
                    canes[5] = canes[5] + cantidad
                    ventasentotalidad[5] = ventasentotalidad[5]+totales[3]
                    cantidadporcliente[1] = cantidadporcliente[1] + cantidad

            elif(producto == sabritas[1]):
                cantidad = random.randint(1,sabritas[1])
                ##cantidad = int(input("Ingresar cantidad de sabritas a llevar: "))
                if(cantidad > sabritas[1]):
                    print("Producto insuficiente")
                else:

                    totales[5]=sabritas[3] * cantidad
                    sabritas[1] = sabritas[1] - cantidad
                    canes[1] = canes[1] - cantidad
                    ventasentotalidad[3] = ventasentotalidad[3]+totales[5]
                    cantidadporcliente[7] = cantidadporcliente[7] +cantidad

            elif(producto == coca[1]):
                cantidad = random.randint(1,coca[1])
                ##cantidad = int(input("Ingresar cantidad de coca a llevar: "))
                if(cantidad > coca[1]):
                    print("Producto insuficiente")
                else:

                    totales[7] = coca[1]*cantidad
                    coca[1]=coca[1]-cantidad
                    canes[7]=canes[7]-cantidad
                    ventasentotalidad[9] = ventasentotalidad[9]+totales[7]
                    cantidadporcliente[5]= cantidadporcliente[5]+cantidad
            else:
                print("Producto incorrecto")
        res2 = input("Comprar otro producto?: ")
    total_cliente = totales[7] + totales[3] + totales[1] + totales[5]
    informedeldia[3] = informedeldia[3] +informedeldia[5]
    informedeldia[7] =canes[7]+canes[5]+canes[3]+canes[1]
    print("-----------------------El cliente ha terminado la compra--------------------")
    print("Coca vendida: ", cantidadporcliente[5])
    cantidadporcliente[5]=0
    print("Huevo vendido: ", cantidadporcliente[1])
    cantidadporcliente[1] = 0
    print("Leche vendida: ", cantidadporcliente[3])
    cantidadporcliente[3] = 0
    print("Sabritas vendidas: ", cantidadporcliente[7])
    cantidadporcliente[7] = 0
    print("Total a pagar: ", total_cliente)
    informedeldia[1] = informedeldia[1] + 1
    print("---------------------------Producto Restante-------------------")
    print("Huevo: ", huevo[1])
    if(huevo[1]==50):
        print("Huevo a la mitad de su existencia")
    elif(huevo[1]==25):
        print("Huevo Agotandose")
    elif(huevo[1]<=10):
        print("Huevo Escaso")
    print("Leche: ", leche[1])
    if(leche[1]==50):
        print("Leche a la mitad de su existencia")
    elif(leche[1]==25):
        print("Leche Agotandose")
    elif(leche[1]<=10):
        print("Leche Escasa")
    print("Coca: ", coca[1])
    if(coca[1]==50):
        print("Coca a la mitad de su existencia")
    elif(coca[1]==25):
        print("Coca Agotandose")
    elif(coca[1]<=10):
        print("Coca Escasa")
    print("Sabritas: ", sabritas[1])
    if(sabritas[1]==50):
        print("Sabritas a la mitad de su existencia")
    elif(sabritas[1]==25):
        print("Sabritas Agotandose")
    elif(sabritas[1]<=10):
        print("Sabritas Escasas")
    res = input("Cerrar tienda?: ")

print("##################### LA TIENDA HA CERRADO ######################\n\n")
print("#################### Productos vendidos ##################")
print("Total de huevo vendido: ", canes[5])
print("Venta total de huevo: ", ventasentotalidad[5])
print("Total de leche vendida: ", ventasentotalidad[3])
print("Venta total de leche: ", ventasentotalidad[7])
print("Total de Sabritas vendidas: ", canes[1])
print("Venta total de Sabritas: ", ventasentotalidad[3])
print("Total de coca vendida: ", canes[7])
print("Venta total de coca", ventasentotalidad[9])
print("################# Productos restantes ###########################")
print("Leche: ", leche[1])
print("Huevo: ", huevo[1])
print("Coca: ", coca[1])
print("Sabritas: ", sabritas[1])
print("######################### Venta total ##############################")
print("Productos totales vendidos: ", informedeldia[7])
print("Venta total del día: ", informedeldia[3])
print("Total de clientes del día: ", informedeldia[1])
