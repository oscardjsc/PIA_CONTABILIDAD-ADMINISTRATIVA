from os import sep
from prettytable import PrettyTable
import os
limpiador = lambda: os.system('cls')


print("BIENVENIDOS AL PROGRAMA PARA LA REALIZACION DE UN PRESUPUESTO MAESTRO (PIA)")
print("GRUPO 32")
print("LTI")
print("PROFESOR: PABLO RODRIGUEZ PERALES")

print("Integrantes:")
print("BARRIENTOS AGÜERO DEBANHI NOHEMI #2003270")
print("DUEÑAS LAZCANO RONALDO #1994545")
print("GAMERO CASTAÑEDA DARA BERENICE #2016903")
print("SANCHEZ CANTU OSCAR DE JESUS #2018166")
print("SEGURA MARTINEZ REBECA #1994383")
print("TREJO VEGA ENRIQUE ALONSO #1930976")
print("Instruciones: Favor de ir tecleando los valores que se soliciten")


def sp():
    print("*"*60)


def productoas():
    global total_a
    limpiador()
   

    print("\t\PRESUPUESTO DE VENTAS")
    print("\t\Primer producto")
    print("PRIMER SEMESTRE")
    cantidad1 = int(input("Ingresa la Cantidad de unidades: "))
    precio1 = int(input("Ingresa el Precio: "))
    a_importe = (cantidad1 * precio1)
    print(f"Las ventas esperadas del primer producto en el PRIMER SEMESTRE es de: {a_importe}")
    print("\n")


    print("SEGUNDO SEMESTRE")
    cantidad1_2 = int(input("Ingresa la Cantidad de unidades: "))
    precio1_2 = int(input("Ingresa el Precio: "))
    a2_importe = (cantidad1_2 * precio1_2)
    print(f"Las ventas esperadas del  primer producto en el SEGUNDO SEMESTRE es de: {a2_importe}")
    print("\n")


    print("El total del primer producto es: ")
    total_A = (a_importe + a2_importe)
    print(total_A)
    sp()


    
    print("\t\tSegundo producto")
    print("PRIMER SEMESTRE")
    cantidad2 = int(input("Ingresa la Cantidad de unidades: "))
    precio2 = int(input("Ingresa el Precio: "))
    b_importe = (cantidad2 * precio2)
    print(f"Las ventas esperadas del segundo producto en el PRIMER SEMESTRE es: {b_importe}")
    print("\n")


    print("\t\tSegundo producto")
    print("SEGUNDO SEMESTRE")
    cantidad2 = int(input("Ingresa la Cantidad de unidades: "))
    precio2 = int(input("Ingresa el Precio: "))
    b2_importe = (cantidad2 * precio2)
    print(f"Las ventas esperadas del  segundo producto en el SEGUNDO SEMESTRE es: {b2_importe}")
    print("\n")


    print("Total del Segundo producto: ")
    total_B = (b_importe + b2_importe)
    print(total_B)
    sp()


    
    print("\t\tTercer producto")
    print("PRIMER SEMESTRE")
    c_cant = int(input("Ingresa la Cantidad de unidades: "))
    c_precio = int(input("Ingresa el Precio: "))
    c_importe = (c_cant * c_precio)
    print(f"Las ventas esperadas del tercer producto en el PRIMER SEMESTRE es: {c_importe}")
    print("\n")


    print("\t\tTercer producto")
    print("SEGUNDO SEMESTRE")
    c_cant = int(input("Ingresa la Cantidad de unidades: "))
    c_precio = int(input("Ingresa el Precio: "))
    c2_importe = (c_cant * c_precio)
    print(f"Las ventas esperadas del tercer producto en el SEGUNDO SEMESTRE es: {c2_importe}")
    print("\n")


    print("El total del tercer producto es de: ")
    total_C= (c_importe + c2_importe)
    print(total_C)
    sp()

    print("A continuacion el presupuesto de ventas, en una tabla para mejor entendimiento")
    print("VENTAS POR SEMESTRE")
    s_total = (a_importe + b_importe + c_importe)
    s_total2 = (a2_importe + b2_importe + c2_importe)
    total_A = (total_A + total_B + total_C)
    t = PrettyTable(['PRIMER SEMESTRE','SEGUNDO SEMESTRE','TOTAL ANUAL'])
    t.add_row([s_total,s_total2,total_a])
    print(t)
    input("Pulse Enter para continuar")
    sp()


def flujo():
    limpiador()


    
    print(f"\tSALDO CLIENTES")
    sp()
    print("Ingrese el Saldo Clientes: ")
    saldo_cliente= int(input())
    print(f"Ingresa las Ventas: {total_a}")
    total_clientes= (saldo_cliente + total_a)
    print(f"Saldo Clientes Total: {total_clientes}")


    
    print("\tENTRADAS")
    primer_año= int(input("Ingresa el Cobro del primer año: "))
    segundo_año= int(input("Ingresa el Cobro del segundo año: "))
    entradas_total= (primer_año + segundo_año)
    print(f"El número total de las entradas es: {entradas_total} ")
    total_clientes2= (total_clientes - entradas_total)
    print(f"El saldo total de los clientes es: {total_clientes2}")
    sp()
    input("Pulse Enter para continuar")


def P_Produccion():
    limpiador()
    print("\t*PRESUPUESTO DE PRODUCCION*")
    sp()


   
    print(f"El presupuesto de produccion del PRIMER SEMESTRE")
    nu_a = int(input("Ingresa la Cantidad de unidades: "))
    inventario_finalA = int(input("Ingresa el Inventario Final: "))
    total_unidades = (nu_a + inventario_finalA)
    print(f"El total de unidades sera de: {total_unidades}")
    inventario_inicialA = int(input("Ingresa el Inventario  incial: "))
    up = (total_unidades - inventario_inicialA)
    print(f"El numero de unidades a producirse de manera total en el PRIMER SEMESTRE son: {up}")
    
    
    print(f"\t\tEl presupuesto de producción del SEGUNDO SEMESTRE")
    nu_a2 = int(input("Ingresa la Cantidad de unidades: "))
    inventario_finalA2 = int(input("Ingresa el Inventario Final: "))
    print("Total de unidades es de: ")
    total_unidades2 = (nu_a2 + inventario_finalA2)
    print(f"El total de unidades sera de: {total_unidades2}")
    inventario_inicialA2 = int(input("Ingresa el Inventario  inicial: "))
    up_a2 = (total_unidades2 - inventario_inicialA2)
    print(f"El numero de unidades a producirse de manera total en SEGUNDO SEMESTRE son: {up_a2}")



    print(f"\t\tProduccion Total del primer producto")
    numero_unidades_AT = (nu_a + nu_a2)
    print(f"Las Unidades a vender son : {numero_unidades_AT}")
    print(f"El Inventario finales de: {inventario_finalA2}")
    Total_UnidadesA= (numero_unidades_AT + inventario_finalA2)
    print(f"El total de unidades es: {Total_UnidadesA}")
    inventario_inicialA = inventario_finalA
    TotalT= (Total_UnidadesA - inventario_inicialA)
    print(f"El total de unidades del primer producto es de: {TotalT}")
    sp()


    
    print(f"\t\tPresupuesto de producción del segundo producto e PRIMER SEMESTRE")
    nu_b = int(input("Ingresa la Cantidad de unidades: "))
    inventario_finalB = int(input("Ingresa el Inventario Final: "))
    total_unidades = (nu_b + inventario_finalB)
    print(f"El total de unidades sera de: {total_unidades}")
    inventario_inicialB = int(input("Ingresa el Inventario  inicial: "))
    up = (total_unidades - inventario_inicialB)
    print(f"El numero de unidades a producirse de manera total en PRIMER SEMESTRE son: {up}")
    
  
    print(f"\t\tEl presupuesto de produccion del segundo producto en SEGUNDO SEMESTRE")
    nu_b2 = int(input("Ingresa la Cantidad de unidades: "))
    inventario_finalB2 = int(input("Ingresa el Inventario Final: "))
    print("El total de unidades sera de: ")
    total_unidades2 = (nu_b2 + inventario_finalB2)
    print(f"El total de unidades sera de: {total_unidades2}")
    inventario_inicialB2 = int(input("Ingresa el Inventario  incial: "))
    up_b2 = (total_unidades2 - inventario_inicialB2)
    print(f"El numero de unidades a producirse de manera total en SEGUNDO SEMESTRE son: {up_b2}")



    print(f"\t\tProduccion Total SEGUNDO PRODUCTO")
    nu_bt = (nu_b + nu_b2)
    print(f"Las unidades a vender seran: {nu_bt}")
    print(f"El inventario final es de: {inventario_finalB2}")
    Total_UnidadesB= (nu_bt + inventario_finalB2)
    print(f"El Total de las unidades es de de: {Total_UnidadesB}")
    inventario_inicialB = inventario_finalB
    TotalBT= (Total_UnidadesB - inventario_inicialB)
    print(f"Unidades Totales de SEGUNDO PRODUCTO: {TotalBT}")
    sp()


   
    print(f"\t\tPresupuesto de Produccion TERCER PRODUCTO PRIMER SEMESTRE")
    nu_c = int(input("Ingresa la Cantidad de unidades: "))
    inventario_finalC = int(input("Ingresa el Inventario Final: "))
    total_unidades = (nu_c + inventario_finalC)
    print(f"El numero total de unidades sera de : {total_unidades}")
    inventario_inicialC = int(input("Ingresa el Inventario  inicial: "))
    up = (total_unidades - inventario_inicialC)
    print(f"El numero de unidades a producirse de manera total en PRIMER SEMESTRE son: {up}")
    
   
    print(f"\t\tPresupuesto de Produccion TERCER PRODUCTO SEGUNDO SEMESTRE")
    nu_c2 = int(input("Ingresa la Cantidad de unidades: "))
    inventario_finalC2 = int(input("Ingresa el Inventario Final: "))
    print("El numero total de unidades sera de: ")
    total_unidades2 = (nu_c2 + inventario_finalC2)
    print(f"El numero total de unidades sera de: {total_unidades2}")
    inventario_inicialC2 = int(input("El inventario inicial es:: "))
    up_c2 = (total_unidades2 - inventario_inicialC2)
    print(f"El numero de unidades a producirse de manera total en SEGUNDO SEMESTRE son: {up_c2}")


  
    numero_unidades_CT = (nu_c + nu_c2)
    print(f"Las Unidades a Vender son: {numero_unidades_CT}")
    print(f"El Inventario Final es de: {inventario_finalC2}")
    Total_UnidadesC= (numero_unidades_CT + inventario_finalC2)
    print(f"El Total de unidades es de: {Total_UnidadesC}")
    inventario_inicialC = inventario_finalC
    TotalCT= (Total_UnidadesC - inventario_inicialC)
    print(f"el total de unidades totales del TERCER PRODUCTO es de: {TotalCT}")
    sp()
    input("*****PRESIONE ENTER PARA CONTINUAR*****")


def P_Mate():
    limpiador()
    print("\tPRESUPUESTO REQUERIMIENTOS PARA MATERIALES")


    
    print(f"\tPRIMER PRODUCTO")
    nu_a = int(input("Ingresa la Cantidad de unidades del primer producto en el primer semestre: "))
    nu_a2 = int(input("Ingresa la Cantidad de unidades del primer producto en el segundo semestre: "))


    print("--Requerimientos de los Materiales A, B y C--")
    req_a = float(input("Ingresa los requerimientos Primer Material A: "))
    req_a2 = float(input("Ingresa los requerimientos Segundo Material A: "))


    req_b = float(input("Ingresa los requerimientos Primer Material B: "))
    req_b2 = float(input("Ingresa los requerimientos Segundo Material B: "))


    req_c = float(input("Ingresa los requerimientos Primer Material C: "))
    req_c2 = float(input("Ingresa los requerimientos Segundo Material C: "))


    total_A1 = (nu_a * req_a)
    total_A2 = (nu_a2 * req_a2)
    total_AT = (total_A1 + total_A2)
    total_B1 = (nu_a * req_b)
    total_B2 = (nu_a2 * req_b2)
    total_BT = (total_B1 + total_B2)
    total_C1 = (nu_a * req_c)
    total_C2 = (nu_a2 * req_c2)
    total_CT = (total_C1 + total_C2)


    print(" A continuacion, a manera de tabla, se le muestra los materiales requeridos del primer producto")
    t = PrettyTable(['PRIMER SEMESTRE','SEGUNDO SEMESTRE','TOTAL'])
    t.add_row([total_A1,total_A2,total_AT])
    print(t)


    print("TOTAL DEL MATERIAL B QUE SE REQUIERE")
    t = PrettyTable(['PRIMER SEMESTRE','SEGUNDO SEMESTRE','TOTAL'])
    t.add_row([total_B1,total_B2,total_BT])
    print(t)


    print("TOTAL DEL MATERIAL C QUE SE REQUIERE")
    t = PrettyTable(['PRIMER SEMESTRE','SEGUNDO SEMESTRE','TOTAL'])
    t.add_row([total_C1,total_C2,total_CT])
    print(t)
    sp()
    input("*****PRESIONE ENTER PARA CONTINUAR*****")


    
    limpiador()
    print(f"\tSEGUNDO PRODUCTO")
    nu_a = float(input("Ingresa la cantidad de unidades del segundo producto en el primer semestre: "))
    nu_a2 = float(input("Ingresa la cantidad de unidades del segundo producto en el segundo semestre: "))


    print("--Requerimientos de los Materiales A, B y C--")
    req_a = float(input("Ingreso los requerimientos Primer Material A"))
    req_a2 = float(input("Ingresa los requerimientos Segundo Material A"))


    req_b = float(input("Ingresa los requerimientos Primer Material B"))
    req_b2 = float(input("Ingresa los requerimientos Segundo Material B"))


    req_c = float(input("Ingresa los requerimientos Primer Material C"))
    req_c2 = float(input("Ingresaa los requerimientos Segundo Material C"))


    total_A1 = (nu_a * req_a)
    total_A2 = (nu_a2 * req_a2)
    total_AT = (total_A1 + total_A2)
    total_B1 = (nu_a * req_b)
    total_B2 = (nu_a2 * req_b2)
    total_BT = (total_B1 + total_B2)
    total_C1 = (nu_a * req_c)
    total_C2 = (nu_a2 * req_c2)
    total_CT = (total_C1 + total_C2)


    print("A continuacion, a manera de tabla, se le muestra los materiales requeridos para el segundo producto")
    t = PrettyTable(['PRIMER SEMESTRE','SEGUNDO SEMESTRE','TOTAL'])
    t.add_row([total_A1,total_A2,total_AT])
    print(t)


    print("TOTAL DEL MATERIAL B QUE SE REQUIERE")
    t = PrettyTable(['PRIMER SEMESTRE','SEGUNDO SEMESTRE','TOTAL'])
    t.add_row([total_B1,total_B2,total_BT])
    print(t)


    print("TOTAL DEL MATERIAL C QUE SE REQUIERE")
    t = PrettyTable(['PRIMER SEMESTRE','SEGUNDO SEMESTRE','TOTAL'])
    t.add_row([total_C1,total_C2,total_CT])
    print(t)
    sp()
    input("*****PRESIONE ENTER PARA CONTINUAR*****")


 
    limpiador()
    print(f"\tTERCER PRODUCTO")
    nu_a = float(input("Ingresa la cantidad de unidades del tercer producto en el primer semestre: "))
    nu_a2 = float(input("Ingresa la cantidad de unidades del tercer producto en el segundo semestre: "))


    print("--Requerimientos de los materiales A, B y C--")
    req_a = float(input("Ingresa los requerimientos Primer Material A"))
    req_a2 = float(input("Ingresa los requerimientos Segundo Material A"))


    req_b = float(input("Ingresa los requerimientos Primer Material B"))
    req_b2 = float(input("Ingresa los requerimientos Segundo Material B"))


    req_c = float(input("Ingresa los requerimientos Primer Material C"))
    req_c2 = float(input("Ingresa los requerimientos Segundo Material C"))


    total_A1 = (nu_a * req_a)
    total_A2 = (nu_a2 * req_a2)
    total_AT = (total_A1 + total_A2)
    total_B1 = (nu_a * req_b)
    total_B2 = (nu_a2 * req_b2)
    total_BT = (total_B1 + total_B2)
    total_C1 = (nu_a * req_c)
    total_C2 = (nu_a2 * req_c2)
    total_CT = (total_C1 + total_C2)


    print("A continuacion, a manera de tabla, se le muestra, los materiales requeridos del tercer producto")
    t = PrettyTable(['PRIMER SEMESTRE','SEGUNDO SEMESTRE','TOTAL'])
    t.add_row([total_A1,total_A2,total_AT])
    print(t)


    print("TOTAL DEL MATERIAL B QUE SE REQUIERE")
    t = PrettyTable(['PRIMER SEMESTRE','SEGUNDO SEMESTRE','TOTAL'])
    t.add_row([total_B1,total_B2,total_BT])
    print(t)


    print("TOTAL DEL MATERIAL C QUE SE REQUIERE")
    t = PrettyTable(['PRIMER SEMESTRE','SEGUNDO SEMESTRE','TOTAL'])
    t.add_row([total_C1,total_C2,total_CT])
    print(t)
    sp()
    input("*****PRESIONE ENTER PARA CONTINUAR*****")


def P_Materiales():


    limpiador()
    print(f"\tPRESUPUESTO COMPRA MATERIALES")


    
    print("MATERIAL A")
    sp()
    print("PRIMER SEMESTRE")
    req_a = int(input("Ingresa el requerimiento de materiales: "))
    inventario_finalA = int(input("Ingresa el Inventario final: "))
    total_materialesA = (req_a + inventario_finalA)
    print(f"Los materiales son: {total_materialesA} ")
    inventario_inicialA = int(input("Ingresa el inventario inicial: "))
    total_materialesA_t = (total_materialesA - inventario_inicialA)
    print(f"Los materiales a comprar son: {total_materialesA_t}")
    precio_compra = float(input("Ingresa el precio de compra: "))
    Total_materialA = (total_materialesA_t * precio_compra)
    print(f"El total del material A en pesos en el primer semestres es de : {Total_materialA}")
    sp()


    print("SEGUNDO SEMESTRE")
    req_a2 = int(input("Ingresa el requerimentos de materiales: "))
    inventario_finalA2 = int(input("Ingresa el inventario final: "))
    total_materialesA = (req_a + inventario_finalA)
    print(f"Los materiales son: {total_materialesA} ")
    inventario_inicialA2 = int(input("Ingresa el inventario inicial: "))
    total_materialesA_t2 = (total_materialesA - inventario_inicialA2)
    print(f"Los materiales a comprar son: {total_materialesA_t2}")
    precio_compra = float(input("Ingresa el precio de compra: "))
    Total_materialA2 = (total_materialesA_t * precio_compra)
    print(f"El total del material A en pesos en el segundo semestres es deE: {Total_materialA2}")


    
    limpiador()
    print("\nTOTAL MATERIAL A")
    sp()
    print(f"El requerimientos de materiales: {req_a + req_a2}")
    print(f"El inventario final es de: {inventario_finalA + inventario_finalA2}")
    print(f"Los materiales son de : {total_materialesA + total_materialesA_t2}")
    print(f"El inventario inicial es de : {inventario_inicialA + inventario_inicialA2}")
    print(f"Los materiales a comprar es: {total_materialesA_t + total_materialesA_t2}")
    print(f"El material en pesos sera de: ${Total_materialA + Total_materialA2} ")
    sp()
    input("*****PRESIONE ENTER PARA CONTINUAR*****")


    
    print("MATERIAL B")
    sp()
    print("PRIMER SEMESTRE")
    req_a = int(input("Ingresa el requerimento de materiales: "))
    inventario_finalA = int(input("Ingresa el inventario final: "))
    total_materialesA = (req_a + inventario_finalA)
    print(f"Los materiales son: {total_materialesA} ")
    inventario_inicialA = int(input("Ingresa el inventario inicial: "))
    total_materialesA_t = (total_materialesA - inventario_inicialA)
    print(f"Los materiales a comprar son: {total_materialesA_t}")
    precio_compra = float(input("Ingresa el precio de compra: "))
    Total_materialA = (total_materialesA_t * precio_compra)
    print(f"El total del material B en pesos en el primer semestre es de: {Total_materialA}")
    sp()


    
    print("SEGUNDO SEMESTRE")
    req_a2 = int(input("Ingresa el requerimento de materiales: "))
    inventario_finalA2 = int(input("Ingresa el inventario final: "))
    total_materialesA = (req_a + inventario_finalA)
    print(f"El total de los materiales es de: {total_materialesA} ")
    inventario_inicialA2 = int(input("Ingresa el inventario inicial: "))
    total_materialesA_t2 = (total_materialesA - inventario_inicialA2)
    print(f"Los materiales a comprar seran de: {total_materialesA_t2}")
    precio_compra = float(input("Ingresa el precio de compra: "))
    Total_materialA2 = (total_materialesA_t * precio_compra)
    print(f"El total del material B en pesos en el segundo semestre es de: {Total_materialA2}")


   
    limpiador()
    print("\nTOTAL MATERIAL B")
    sp()
    print(f"EL requerimiento de materiales: {req_a + req_a2}")
    print(f"El inventario Final es de: {inventario_finalA + inventario_finalA2}")
    print(f"Los materiales son: {total_materialesA + total_materialesA_t2}")
    print(f"El inventario inicial es de: {inventario_inicialA + inventario_inicialA2}")
    print(f"Los materiales a comprar es de: {total_materialesA_t + total_materialesA_t2}")
    print(f"El material en pesos sera de: ${Total_materialA + Total_materialA2} ")
    sp()
    input("*****PRESIONE ENTER PARA CONTINUAR*****")


    
    print("MATERIAL C")
    sp()
    print("PRIMER SEMESTRE")
    req_a = int(input("Ingresa el requerimento de materiales: "))
    inventario_finalA = int(input("Ingresa el inventario final: "))
    total_materialesA = (req_a + inventario_finalA)
    print(f"El total de los materiales es de: {total_materialesA} ")
    inventario_inicialA = int(input("Ingresa el inventario incial: "))
    total_materialesA_t = (total_materialesA - inventario_inicialA)
    print(f"Los materiales a comprar son de: {total_materialesA_t}")
    precio_compra = float(input("Ingresa el precio de compra: "))
    Total_materialA = (total_materialesA_t * precio_compra)
    print(f"El total del material C en pesos en el primer semestre es de: {Total_materialA}")
    sp()


   
    print("SEGUNDO SEMESTRE")
    req_a2 = int(input("Ingresa el requerimento de materiales: "))
    inventario_finalA2 = int(input("Ingrsa el inventario final: "))
    total_materialesA = (req_a + inventario_finalA)
    print(f"El total de los materiales es de: {total_materialesA} ")
    inventario_inicialA2 = int(input("Inventario incial: "))
    total_materialesA_t2 = (total_materialesA - inventario_inicialA2)
    print(f"Total de material a comprar son de: {total_materialesA_t2}")
    precio_compra = float(input("Ingresa el precio de compra: "))
    Total_materialA2 = (total_materialesA_t * precio_compra)
    print(f"El total del material C en pesos en el segundo semestre es de:: {Total_materialA2}")


 
    limpiador()
    print("\nTOTAL MATERIAL C")
    sp()
    print(f"El requerimientos de materiales dio a: {req_a + req_a2}")
    print(f"El inventario final fue de : {inventario_finalA + inventario_finalA2}")
    print(f"Los materiales total es de: {total_materialesA + total_materialesA_t2}")
    print(f"El inventario inicial es de: {inventario_inicialA + inventario_inicialA2}")
    print(f"Los materiales a comprar es: {total_materialesA_t + total_materialesA_t2}")
    print(f"El material en pesos sera de: ${Total_materialA + Total_materialA2} ")
    sp()
    input("*****PRESIONE ENTER PARA CONTINUAR*****")


def Proveedores_F_Salida():
    limpiador()
    print("\tSALDOS PROVEEDORES Y FLUJOS DE SALIDA")
    sp()
    saldo_c = int(input("Ingresa el Saldo Clientes: "))
    total_clientes = (saldo_c + total_a)
    print(f"El Saldo Total Clientes es de: {total_clientes}")
    print("**Aqui inicia el apartado de las entradas de efectivo**")
    Año_1 = int(input("Ingresa la cobranza del primer año que se tenga: "))
    Año_2 = int(input("Ingresa la cobranza del segundo año que se tenga: "))
    total_entradas = (Año_1 + Año_2)
    print(f"El calculo del total de entradas dio a : {total_entradas}")
    Total_Clientes2 = (total_clientes - total_entradas)
    print(f"El saldo clientes de clientes dio a : {Total_Clientes2}")
    sp()
    input("*****PRESIONE ENTER PARA CONTINUAR*****")


def Mano_Directa():
    limpiador()
    global total_horas_reqSum
    print("\tPRESUPUESTO PARA MANO DE OBRA DIRECTA")


   
    sp()
    print("PRIMER PRODUCTO EN EL PRIMER SEMESTRE")
    unidades_p1= int(input("Ingresa las unidades a producir: "))
    horas_por_unidad= int(input("Ingresa las horas de mano de obra: "))
    total_horas_req1 = (unidades_p1 * horas_por_unidad)
    print(f"El total de horas es de: {total_horas_req1}")
    cuota_por_hora= int(input("Ingresa el precio por hora: "))
    importe_mano_obra_directa = total_horas_req1 * cuota_por_hora
    print(f"El costo total de mano de obra dio a : {importe_mano_obra_directa}")


    
    print("PRIMER PRODUCTO EN EL SEGUNDO SEMESTRE")
    unidades_p2 = int(input("Ingresa las unidades a producir: "))
    horas_por_unidad2 = int(input("Ingresa las horas de mano de obra: "))
    total_horas_req2 = (unidades_p2 * horas_por_unidad2)
    print(f"El total de horas sera de: {total_horas_req2}")
    cuota_por_hora2 = int(input("Ingresa el precio por hora: "))
    importe_mano_obra_directa2 = total_horas_req2 * cuota_por_hora2
    print("El costo total de mano de obra dio a: ", importe_mano_obra_directa2)


    
    unidades_totales = (unidades_p1 + unidades_p2)
    print(f"El calculo del total de unidades a producior dio a: {unidades_totales}")
    Total_horas_unidad = (horas_por_unidad + horas_por_unidad2)
    print(f"El calculo del total de horas requeridas por unidad dio a : {Total_horas_unidad}")
    Total_horas_req = (unidades_totales * Total_horas_unidad)
    print(f"El calculo del total otal de horas requeridas dio a : {Total_horas_req}")
    Total_importemano_obra_directa = (importe_mano_obra_directa + importe_mano_obra_directa2)
    print(f"El total del costo de mano de obra en este producto sera de: {Total_importemano_obra_directa}")
    sp()
    input("*****PRESIONE ENTER PARA CONTINUAR*****")


    
    
    limpiador()
    sp()
    print("SEGUNDO PRODUCTO EN EL PRIMER SEMESTRE")
    unidades_p1B = int(input("Ingresa las unidades a producir: "))
    horas_por_unidadB1 = int(input("Ingresa la horas de mano de obra: "))
    total_horas_reqB1 = (unidades_p1B * horas_por_unidadB1)
    print(f"El total de horas sera de : {total_horas_reqB1}")
    cuota_por_horaB1= int(input("Ingresa el precio por hora: "))
    importe_mano_obra_directaB1= total_horas_reqB1 * cuota_por_horaB1
    print(f"El costo total de mano de obra dio a: {importe_mano_obra_directaB1}")


    
    print("SEGUNDO PRODUCTO EN EL SEGUNDO SEMESTRE")
    unidades_p1B2 = int(input("Ingresa las unidades a producir: "))
    horas_por_unidadB2 = int(input("Ingresa las horas de mn-ano de obra: "))
    total_horas_reqB2 = (unidades_p1B2 * horas_por_unidadB2)
    print(f"El total de horas sera de: {horas_por_unidadB1 + total_horas_reqB2}")
    cuota_por_horaB2 = int(input("Ingresa el precio por hora: "))
    importe_mano_obra_directaB2 = total_horas_reqB2 * cuota_por_horaB2
    print(f"El costo total de mano de obra dio a: {importe_mano_obra_directaB2}")


    
    unidades_totalesB = (unidades_p1B + unidades_p1B2)
    print(f"El calculo del total de unidades a producir dio: {unidades_totalesB}")
    uniTotal_horas_unidadB = (horas_por_unidadB1)
    print(f"El calculo del total de horas requeridas por unidad dio a: {uniTotal_horas_unidadB}")
    Total_horas_reqB = (unidades_totalesB * uniTotal_horas_unidadB)
    print("El calculo del total de horas requeridas dio a : ", Total_horas_reqB)
    Total_importemano_obra_directaB = (importe_mano_obra_directaB1 + importe_mano_obra_directaB2)
    print("El total del costo de mano de obra en este producto sera de: ", Total_importemano_obra_directaB)
    sp()
    input("*****PRESIONE ENTER PARA CONTINUAR*****")




    limpiador()
    sp()
    print("\tTOTAL DE TODO EL PRESUPUESTO(LOS 3 PRODUCTOS)")
    print(f"El total de las unidades a requerir son: {unidades_totales + unidades_totalesB} ")
    print(f"El total de las horas Requeridas por las 3 unidades: {Total_horas_req + Total_horas_reqB}")
    total_horas_reqSum = Total_horas_req + total_horas_reqB1
    print(f"El total de horas requeridas es de: {Total_horas_req + total_horas_reqB1}")
    print(f"EL TOTAL DE LA MANO DE OBRA DIO A : {Total_importemano_obra_directa + Total_importemano_obra_directaB}")


    print("\tHORAS QUE SE REQUIERAN")
    print(f"PRIMER SEMESTRE: {total_horas_req1 + total_horas_reqB1}")
    print(f"SEGUNDO SEMESTRE: {total_horas_req2 + total_horas_reqB2}")
    print(f"TOTAL: {Total_horas_req + Total_horas_reqB}")


    print("\tTOTAL MANO DE OBRA DIRECTA")
    print(f"El total de mano de obra en el primer semestre es de: {importe_mano_obra_directa + importe_mano_obra_directaB1}")
    print(f"El total de mano de obra en el segundo semestre es de: {importe_mano_obra_directa2 + importe_mano_obra_directaB2} ")
    print(f"El total de mano de obra es de: {Total_importemano_obra_directa + Total_importemano_obra_directaB}")
    sp()
    input("*****PRESIONE ENTER PARA CONTINUAR*****")


def Gastos_I():
    limpiador()
    global total_GIF
    print("\tGASTOS INDIRECTOS DE FABRICACION")
    sp()
    print("PRIMER SEMESTRE")
    seguros_s1 = int(input("Ingresa los seguros: "))
    depreciacion_s1 = int(input("Ingresa la depreciacion: "))
    energeticos_s1 = int(input("Ingresa los ergeticos: "))
    mantenimiento_s1 = int(input("Ingresa la cantidad de mantenimiento: "))
    varios_s1 = int(input("Ingresa lo que se requiera en varios/otros: "))
    totalGIF_s1 = (depreciacion_s1 + seguros_s1 + mantenimiento_s1 + energeticos_s1 + varios_s1)
    print(f"El total de gastos indirectos es de: {totalGIF_s1} en el primer semestre")


    print("SEGUNDO SEMESTRE")
    seguros_s2= int(input("Ingresa los seguros: "))
    depreciacion_s2= int(input("Ingresa la depreciacion: "))
    energeticos_s2= int(input("Ingresa los energeticos: "))
    mantenimiento_s2= int(input("Ingresa la cantidad de maantenimiento: "))
    varios_s2= int(input("Ingresa lo que se requiere en varios/otrs: "))
    totalGIF_s2= (depreciacion_s2 + seguros_s2 + mantenimiento_s2 + energeticos_s2 + varios_s2)
    print(f"El total de gastos indirectos es de: {totalGIF_s2} en el segundo semestre")

    total_depreciacion = (depreciacion_s1 + depreciacion_s2)
    print(f"Total Depreciacion: {total_depreciacion}")

    total_seguros = (seguros_s1 + seguros_s2)
    print(f"Total Seguros: {total_seguros}")

    total_mantenimiento = (mantenimiento_s1 + mantenimiento_s2)
    print(f"Total Mantenimiento: {total_mantenimiento}")

    total_energeticos = (energeticos_s1 + energeticos_s2)
    print(f"Total Energeticos: {total_energeticos}")

    total_varios = (varios_s1 + varios_s2)
    print(f"Total Varios: {total_varios}")

    total_GIF = (total_depreciacion + total_seguros + total_mantenimiento + total_energeticos + total_varios)
    print(f"Total G.I.F: {total_GIF}")
    input("Presione Enter para continuar...")

    limpiador()
    print(f"Total de G.I.F: {total_GIF}")
    print(f"Total de HRS.: {total_horas_reqSum}")
    total_GIF = (total_GIF / total_horas_reqSum)
    print(f"TASA G.I.F. POR UNIDAD: {total_GIF}")
    sp()
    input("*****PRESIONE ENTER PARA CONTINUAR*****")


def Gastos_O():
    limpiador()
    print("\tGASTOS DE OPERACION")


    
    print("PRIMER SEMESTRE")
    depreciacion_s1 = int(input("Ingresa la depreciacion : "))
    salarios_s1 = int(input("Ingresa los salarios: "))
    comisiones_s1 = int(input("Ingresa las comisiones: "))
    varios_s1 = int(input("Ingresa los varios/ otros que se tengan: "))
    intereses_s1 = int(input("Ingresa los intereses por algun prestamo: "))
    print(f"Total: {depreciacion_s1 + salarios_s1 + comisiones_s1 + varios_s1 + intereses_s1}")


    
    print("SEGUNDO SEMESTRE")
    depreciacion_s2 = int(input("Ingresa la depreciacion : "))
    salarios_s2 = int(input("Ingresa los salarios: "))
    comisiones_s2 = int(input("Ingresa las comisiones: "))
    varios_s2 = int(input("Ingresa los varios/ otros que se tengan: "))
    intereses_s2 = int(input("Ingresa los intereses por algun prestamo: "))
    print(f"Total: {depreciacion_s2 + salarios_s2 + comisiones_s2 + varios_s2 + intereses_s2}")
    input("*****PRESIONE ENTER PARA CONTINUAR*****")



    print(f"TOTAL DE GASTOS DIRECTOS: {depreciacion_s1+ salarios_s1 +comisiones_s1+ varios_s1 + intereses_s1 + depreciacion_s2 + salarios_s2 + comisiones_s2 + varios_s2 + intereses_s2}")
    sp()
    input("*****PRESIONE ENTER PARA CONTINUAR*****")


def Costo_U():
    limpiador()
    print("\tCOSTO UNITARIO PRODUCTO TERMINADO")
    
    print("PRIMER PRODUCTO")
    print("Material A")
    costo_a = float(input("Ingresa el costos del material A del primer producto: "))
    cantidad_a = float(input("Ingresa la cantidad del material A del primer producto: "))
    costo_unitario = costo_a * cantidad_a 
    print(f"El costo unitario dio a: {costo_unitario}")


    print("Material B")
    costo_b = float(input("Ingresa el costo del material B del primer producto: "))
    cantidad_b = float(input("Ingresa la cantidad del material B del primer producto: "))
    costo_unitario_b = costo_b * cantidad_b 
    print(f"El costo unitario dio a: {costo_unitario_b}")


    print("Material C")
    costo_c = float(input("Ingresa el costo del material C del primer producto: "))
    cantidad_c = float(input("Ingresa la cantidad del material C del primer producto: "))
    costo_unitario_c = costo_c * cantidad_c 
    print(f"El costo unitario es dio a: {costo_unitario_c}",)


    costo_mano = int(input("Ingresa el costo de mano de obra del primer producto"))
    cant_mano = float(input("Ingresa la cantidad de mano de obra del primer producto"))
    costo_unitario_mano = costo_mano * cant_mano 
    print(f"El costo unitario dio a: {costo_unitario_mano}")



    costo_gastos_fab = float(input("Ingresa el costo de GIF del primer producto: "))
    cant_gastos = float(input("Ingresa la cantidad de GIF del primer producto"))
    costo_unitario_fab = costo_gastos_fab * cant_gastos 
    print(f"El costo unitario dio a: {costo_unitario_fab}")


    print(f"El costo por unidad del primer producto sera de: ${costo_unitario+costo_unitario_b+costo_unitario_c+costo_unitario_mano+costo_unitario_fab}")
    sp()


    print("SEGUNDO PRODUCTO")

    costo_a = float(input("Ingresa el costo del material A del segundo producto: "))
    cantidad_a = float(input("Ingresa el la cantidad del material B del segundo producto: "))
    costo_unitario = costo_a * cantidad_a 
    print(f"El costo por unidad sera de: {costo_unitario}")


    print("Material B")
    costo_b = float(input("Ingresa el costo del material B del segundo producto: "))
    cantidad_b = float(input("Ingresa la cantidad del material B del segundo producto: "))
    costo_unitario_b = costo_b * cantidad_b 
    print(f"El costo por unidad sera de: {costo_unitario_b}")


    print("Material C")
    costo_c = float(input("Ingresa el costo del material C del segundo producto: "))
    cantidad_c = float(input("Ingresa la cantidad del material C del segundo producto: "))
    costo_unitario_c = costo_c * cantidad_c 
    print(f"El costo por unidad sera de: {costo_unitario_c}",)


    print("Mano de Obra")
    costo_mano = float(input("Ingresa el costo de la mano de obra del segundo producto: "))
    cant_mano = float(input("Ingresa la cantidad de mano de obra del segundo producto: "))
    costo_unitario_mano = costo_mano * cant_mano 
    print(f"El costo por mano de obra sera de: {costo_unitario_mano}")


    print("Gastos Indirectos de Fabricacion")
    costo_gastos_fab = float(input("Ingresa el costo de GIF del segundo producto: "))
    cant_gastos = float(input("Ingresa la cantidad de GIF del segundo producto:"))
    costo_unitario_fab = costo_gastos_fab * cant_gastos 
    print(f"El costo por unidad del GIF dio a: {costo_unitario_fab}")


    print(f"El costo por unidad total del segundo producto sera de: ${costo_unitario+costo_unitario_b+costo_unitario_c+costo_unitario_mano+costo_unitario_fab}")
    sp()


    print("TERCER PRODUCTO")
    print("Material A")
    costo_a = float(input("Ingresa el costo del material A en el tercer producto: "))
    cantidad_a = float(input("Ingresa la cantidad del material A en el tercer producto "))
    costo_unitario = costo_a * cantidad_a 
    print(f"El costo por unidad sera de: {costo_unitario}")


    print("Material B")
    costo_b = float(input("Ingresa el costo del material B en el tercer producto: "))
    cantidad_b = float(input("Ingresa el cantidad del material B en el tercer producto: "))
    costo_unitario_b = costo_b * cantidad_b 
    print(f"El costo por unidad sera de: {costo_unitario_b}")


    print("Material C")
    costo_c = float(input("Ingresa el costo del material C en el tercer producto: "))
    cantidad_c = float(input("Ingresa la cantidad del material C en el tercer producto: "))
    costo_unitario_c = costo_c * cantidad_c 
    print(f"El costo por unidad sera de: {costo_unitario_c}")


    print("Mano de Obra")
    costo_mano = float(input("Ingresa el costo de mano de obra del tercer producto: "))
    cant_mano = float(input("Ingresa la cantidad de mano de obra del tercer producto: "))
    costo_unitario_mano = costo_mano * cant_mano 
    print(f"El costo por unidad dio a: {costo_unitario_mano}")


    print("Gastos Indirectos de Fabricacion")
    costo_gastos_fab = float(input("Ingresa los costos GIF en el tercer producto: "))
    print("Ingresa la cantidad de GIF por el tercer producto: ")
    cant_gastos = float(input())
    costo_unitario_fab = costo_gastos_fab * cant_gastos 
    print(f"El calculo del costo por unidad dio a: {costo_unitario_fab}")


    print(f"El costo total por unidad del tercer producto es de: ${costo_unitario+costo_unitario_b+costo_unitario_c+costo_unitario_mano+costo_unitario_fab}")
    sp()
    input("*****PRESIONE ENTER PARA CONTINUAR*****")


def Inventario_F():
    print("\tINVENTARIOS FINALES")
    print("*"*80)
    print("El inventario final de materiales fue")
    print("Material A")
    unidades_a = int(input("Ingresa las unidades del material A: "))
    costo_a = float(input("Ingresa el costo por unidad del material A: "))
    costo_total_a = (unidades_a * costo_a)
    print(f"El costo por unidad del material A es de: {costo_total_a}")


    print("Material B")
    unidades_b = int(input("Ingresa las unidades del material B: "))
    costo_b = float(input("Ingresa el costo del material B:: "))
    costo_total_b = (unidades_b * costo_b)
    print(f"El costo por unidad del material B es de: {costo_total_b}")


    print("Material C")
    unidades_c = int(input("Ingresa las unidades del material C: "))
    costo_c = float(input("Ingresa el costo del material C: "))
    costo_c = (unidades_c * costo_c)
    print(f"El costo por unidad del material C es de: {costo_c}")


    inventario_final_mat = (costo_total_a + costo_total_b + costo_c)
    print(f"El inventario final del material dio a: {inventario_final_mat}")


    print("Inventario Final Producto Terminado")
    print("Ingresa la cantidad del primer producto :")
    UDSA2= float(input())
    CUA2= float(input("Ingresa el costo del primer producto: "))
    CTA2= (UDSA2 * CUA2)
    print("El costo por unidad dio a: ", CTA2)


  
    print("Ingresa la cantidad del segundo producto: ")
    UDSB2= float(input())
    print("Ingresa el costo del primer producto: ")
    CUB2= float(input())
    CTB2= (UDSB2 * CUB2)
    print("El costo por unidad dio a: ", CTB2)


    
    print("Ingresa la cantidad del tercer producto: ")
    UDSC2= float(input())
    print("Ingresa el costo del tercer producto: ")
    CUC2= float(input())
    CTC2= (UDSC2 * CUC2)
    print("El costo por unidad dio a: ", CTC2)


    inventario_final_mat2= (CTA2 + CTB2 + CTC2)
    print("Los costos por unidad de los 3 productos, de manera conjunta, es de: ", inventario_final_mat2)
    sp()
    input("*****PRESIONE ENTER PARA CONTINUAR*****")


def Produccion_V():
    print("\tESTADO DE COSTOS DE PRODUCCION Y VENTA")
    print("En caso de que no se cuente con el dato, ingresar el 0")
    saldo_inicial = int(input("Ingresa el saldo inicial de materiales: "))
    compras_materiales = int(input("Ingresa las compras de materiales: "))
    material_disponible = compras_materiales + saldo_inicial
    print(f"Los materiales disponibles son: {material_disponible}")


    inventario_final_m = int(input("Ingresa el inventario final de materiales: "))
    materiales_utilizados = material_disponible - inventario_final_m
    print(f"Los materiales utilizados son: {materiales_utilizados}")
    mano_obra_directa = int(input("Ingresa la mano de obra: "))
    gastos_fab_indirectos = int(input("Ingresa el G.I.F: "))
    print(f"El costo de produccion dio a: {materiales_utilizados + mano_obra_directa + gastos_fab_indirectos}")
    inventario_inicial = int(input("Ingresa el inventario inicial de productos terminados: "))
    total_productos = materiales_utilizados + mano_obra_directa + gastos_fab_indirectos + inventario_inicial
    print(f"El total de produccion disponible es de: {total_productos}")
    inventario_final = int(input(f"Ingresa el inventario final de productos terminados: "))
    print(f"Para concluir, el costo de ventas dio a: {total_productos-inventario_final}")
    sp()
    input("*****PRESIONE ENTER PARA CONTINUAR*****")


def Estado_R():
    limpiador()
    print("\tESTADO DE RESULTADOS")
    sp()
    VER1 = float(input("Ingresa las ventas: "))
    CDV1 = float(input("Ingresa el costo de ventas: "))
    UtilidadBruta = VER1-CDV1
    print(f"La utilidas bruta dio a: {UtilidadBruta}")
    GastosO = float(input("Ingresa los gastos de operacion: "))
    UtilidadO= (UtilidadBruta-GastosO)
    print (f"La utilidad operativa dio a: {UtilidadO}")
    ISR1 = float(input("Ingresa el ISR: "))
    PTprimera_cantidad = float(input("Ingresa el PTU: "))
    UtilidadN = (UtilidadO-ISR1-PTprimera_cantidad)
    print (f"La utilidad neta dio a: {UtilidadN}")
    sp()
    input("*****PRESIONE ENTER PARA CONTINUAR*****")


def Flujo_Efectivo():
    limpiador()
    print("\tESTADO FLUJO EFECTIVO")
    sp()
    print("*****Entradas*****")
    cobranza_1 = int(input("Ingresa la primera cobranza "))
    cobranza_2 = int(input("Ingresa la segunda cobranza "))
    print(f"Total Entradas: {cobranza_1 + cobranza_2}")
    sp()
    print('*****Salidas*****')
    proveedor_1 = int(input("Ingresa el pago al primer proveedor: "))
    proveedor_2 = int(input("Ingresa el pago al segundo proveedor: "))
    Pmano_obra_directa= int(input("Ingresa la mano de obra: "))


    gastos_in = float(input("Ingresa el GIF: "))
    gastos_op = float(input("Ingresa los gastos de operacion: "))
    compra_a = float(input("Ingresa la compra de maquinara: "))
    ISR1 = float(input("Ingresa el primer pago del ISR: "))
    ISR2 = float(input("Ingresa el segundo pago del ISR: "))
    print(f"El total de salidas dio a: {proveedor_1 + proveedor_2 + Pmano_obra_directa + gastos_in + gastos_op + compra_a + ISR1 + ISR2}")
    sp()
    input("*****PRESIONE ENTER PARA CONTINUAR*****")


def Balance_General():
    limpiador()
    sp()
    print("\tBIMBO S.A DE C.V")
    print("\tBalance General")
    sp()
    print("**ACTIVOS CIRCULANTES**")
    efectivo_a = int(input("Ingresa la cantidad de efectivo: "))
    clientes = int(input("Ingresa la seccion de clientes: "))
    deudores = int(input("Ingresa los Deudores Diversos: "))
    empleados = int(input("Ingresa los empleados: "))
    inventario_m = int(input("Ingresa el inventario de materiales"))
    inventario_producto = int(input("Ingresa el inventario de producto terminado"))
    activo_circulante = efectivo_a + clientes + deudores + empleados + inventario_m + inventario_producto
    print(f"TOTAL DE ACTIVOS CIRCULANTES: ${activo_circulante}")
    sp()


    print("**ACTIVOS NO CIRCULANTES**")
    terreno = int(input("Ingresa la seccion de terreno: "))
    equipo = int(input("Ingresa la seccio de planta y equipo: "))
    depreciacion = int(input("Ingresa la depreciación acumulada: "))
    activo_no_circulante = terreno + equipo - depreciacion
    print(f"TOTAL DE LOS ACTIVOS NO CIRCULANTES: ${activo_no_circulante}")
    sp()


    print(f"ACTIVO TOTAL: {activo_circulante + activo_no_circulante}")


    print("\n**PASIVO CORTO PLAZO**")
    proveedores = int(input("Ingresa los proveedores: "))
    documentos = int(input("Ingresa los documentos por pagar: "))
    ISR = int(input("Ingresa el impuesto sobre la renta por pagar: "))
    PTU = int(input("Ingresa el PTU: "))
    pasivo_corto_plazo = proveedores + documentos + ISR + PTU
    print(f"TOTAL DE PASIVO CORTO PLAZO: ${pasivo_corto_plazo}")
    sp()


    print("**PASIVO LARGO PLAZO**")
    obligacionespa = int(input("Ingresa las obligaciones por pagar: "))
    print(f"TOTA DEL PASIVO A LARGO PLAZO: ${obligacionespa}")

    pasivo_total = pasivo_corto_plazo + obligacionespa
    print(f"PASIVO TOTAL: {pasivo_total}")
    sp()
    
    print("\n**CAPITAL CONTABLE**")
    cap_aportado = int(input("Ingresa el capital Aportado"))
    cap_ganado = int(input("Ingresa el capital Ganado"))
    utilidad = int(input("Ingresa la Utilidad del Ejercicio"))
    total_capital = cap_aportado + cap_ganado + utilidad
    print(f"TOTAL DE CAPITAL CONTABLE: ${total_capital}")


    print("\nTOTAL PASIVO MAS CAPITAL CONTABLE: ")
    print(total_capital + pasivo_total)
    sp()
    input("*****PRESIONE ENTER PARA FINALIZAR*****")


def PresupuestoMaestroTotal():
    print("PRESUPUESTO MAESTRO 2022")
    sp()
    productoas()
    flujo()
    P_Produccion()
    P_Mate()
    P_Materiales()
    Proveedores_F_Salida()
    Mano_Directa()
    Gastos_I()
    Gastos_O()
    Costo_U()
    Inventario_F()
    Produccion_V()
    Estado_R()
    Flujo_Efectivo()
    Balance_General()
    print("Que tenga un bonito dia!")

PresupuestoMaestroTotal()
