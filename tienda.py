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

leche = 100
precio_leche = 20
huevo = 100

precio_huevo = 18.5
sabritas = 100
precio_sabritas = 12.5
coca = 100
precio_coca = 25

clientes = 0
venta_total=0
total_cliente = 0
total_productos = 0

venta_por_cliente = 0
ven_total_sabritas = 0
ven_total_huevo=0
ven_total_leche=0
ven_total_coca=0

total_leche = 0
total_huevo = 0
total_sabritas = 0
total_coca = 0

can_sabritas=0
can_leche=0
can_huevo=0
can_coca = 0

producto = 0
cantidad = 0

huevo_por_cliente = 0
leche_por_cliente = 0 
coca_por_cliente = 0
sabritas_por_cliente = 0

res = input("Cerrar tienda?: ")
while(res!="si"):
    res2 = input("Comprar producto?: ")
    while(res2 != "no"):
        if(coca == 0 and huevo == 0 and leche == 0 and sabritas == 0):
             print("La tienda ha cerrado, productos agotados")
             break
        else:
            print("###############PRODUCTOS############### \n leche - $20 \n huevo - $18.5 \n sabritas - 25 \n coca - 12.5 \n\n ############################")
            producto = input("Ingresar producto a comprar: ")
            if(producto == "leche"):
                cantidad = int(input("Ingresar cantidad de leche a llevar: "))
                if(cantidad > leche):
                    print("No se tiene esa cantidad de leche")
                else:
                    total_leche = precio_leche * cantidad
                    leche = leche - cantidad
                    can_leche = can_leche + cantidad
                    ven_total_leche = ven_total_leche + total_leche
                    leche_por_cliente = leche_por_cliente + cantidad
            elif(producto == "huevo"):
                cantidad = int(input("Ingresar cantidad de huevo a llevar: "))
                if(cantidad > huevo):
                    print("No se tiene esa cantidad de huevo")
                else:
                    total_huevo = precio_huevo * cantidad
                    huevo = huevo - cantidad
                    can_huevo = can_huevo + cantidad
                    ven_total_huevo = ven_total_huevo + total_huevo
                    huevo_por_cliente = huevo_por_cliente + cantidad
            elif(producto == "sabritas"):
                cantidad = int(input("Ingresar cantidad de sabritas a llevar: "))
                if(cantidad > sabritas):
                    print("Producto insuficiente")
                else:
                    total_sabritas = precio_sabritas * cantidad
                    sabritas = sabritas - cantidad
                    can_sabritas = can_sabritas + cantidad
                    ven_total_sabritas = ven_total_sabritas + total_sabritas
                    sabritas_por_cliente = sabritas_por_cliente + cantidad
            elif(producto == "coca"):
                cantidad = int(input("Ingresar cantidad de coca a llevar: "))
                if(cantidad > coca):
                    print("Producto insuficiente")
                else:
                    total_coca = precio_coca * cantidad
                    coca = coca - cantidad
                    can_coca = can_coca + cantidad
                    ven_total_coca = ven_total_coca + total_coca
                    coca_por_cliente = coca_por_cliente + cantidad
            else:
                print("Producto incorrecto")
        res2 = input("Comprar otro producto?: ")
    total_cliente = total_coca + total_huevo + total_leche + total_sabritas
    venta_total = venta_total + total_cliente
    total_productos = can_coca + can_huevo + can_leche + can_sabritas
    print("-----------------------El cliente ha terminado la compra--------------------")
    print("Coca vendida: ", coca_por_cliente)
    coca_por_cliente = 0
    print("Huevo vendido: ", huevo_por_cliente)
    huevo_por_cliente = 0
    print("Leche vendida: ", leche_por_cliente)
    leche_por_cliente = 0
    print("Sabritas vendidas: ", sabritas_por_cliente)
    sabritas_por_cliente = 0
    print("Total a pagar: ", total_cliente)
    clientes = clientes + 1
    print("---------------------------Producto Restante-------------------")
    print("Huevo: ", huevo)
    if(huevo==50):
        print("Huevo a la mitad de su existencia")
    elif(huevo==25):
        print("Huevo Agotandose")
    elif(huevo<=10):
        print("Huevo Escaso")
    print("Leche: ", leche)
    if(leche==50):
        print("Leche a la mitad de su existencia")
    elif(leche==25):
        print("Leche Agotandose")
    elif(leche<=10):
        print("Leche Escasa")
    print("Coca: ", coca)
    if(coca==50):
        print("Coca a la mitad de su existencia")
    elif(coca==25):
        print("Coca Agotandose")
    elif(coca<=10):
        print("Coca Escasa")
    print("Sabritas: ", sabritas)
    if(sabritas==50):
        print("Sabritas a la mitad de su existencia")
    elif(sabritas==25):
        print("Sabritas Agotandose")
    elif(sabritas<=10):
        print("Sabritas Escasas")
    res = input("Cerrar tienda?: ")

print("##################### LA TIENDA HA CERRADO ######################\n\n")
print("#################### Productos vendidos ##################")
print("Total de huevo vendido: ", can_huevo)
print("Venta total de huevo: ", ven_total_huevo)
print("Total de leche vendida: ", can_leche)
print("Venta total de leche: ", ven_total_leche)
print("Total de Sabritas vendidas: ", can_sabritas)
print("Venta total de Sabritas: ", ven_total_sabritas)
print("Total de coca vendida: ", can_coca)
print("Venta total de coca", ven_total_coca)
print("################# Productos restantes ###########################")
print("Leche: ", leche)
print("Huevo: ", huevo)
print("Coca: ", coca)
print("Sabritas: ", sabritas)
print("######################### Venta total ##############################")
print("Productos totales vendidos: ", total_productos)
print("Venta total del día: ", venta_total)
print("Total de clientes del día: ", clientes)
