from Utilidades import  conteo_pricks, update_stocks, convert_key_to_prick, select_prueba, stockdetail, conv_dol, askyesorno, mainmenu_select
from Diccionarios import Dict_Stocks, mainmenu, Dict_reactivos, Dict_acaros, Dict_alimentos, Dict_cucarachas, Dict_epitelios, Dict_gramineas, Dict_hongos, dict_pruebas, Stock_acaros, Stock_alimentos, Stock_cucarachas, Stock_epitelios, Stock_gramineas, Stock_hongos

USD_PEN = 3.42
precio_hist_dol = 50.0
precio_acaros_dol = 35.0
precio_prick_dol = 30.0
tiempo_prick = 0.25
tiempo_intra = 0.5
precio_hora = 50
precio_lanceta = 0.346
nro_acaros = 0
nro_pricks = 0
nro_intra = 0
tipo_prueba = "0"
p_acaros_sol = conv_dol(precio_hist_dol)
p_prick_sol = conv_dol(precio_prick_dol)
p_hist_sol = conv_dol(precio_hist_dol)
seleccion_mainmenu = 0

#actualizacion de USD_PEN
print("Ingrese ultimo tipo de cambio actualizado:\n")
USD_PEN = input()
print("Gracias. Iniciando programa.")

#Inicio del programa
while True:
    print("Bienvenido al aplicativo para cotizacion de pruebas de prick test.\n")
    print("Seleccione que desea realizar: ")
    for key, value in mainmenu.items():
        print(f"{key}:{value}")
    seleccion_mainmenu = mainmenu_select()
    #Cotizacion de prueba
    if seleccion_mainmenu == "1":
        tipo_prueba = select_prueba()
        print("\nSe muestra a continuacion los stocks disponibles de los reactivos de la prueba seleccionada: \n")
        stockdetail(tipo_prueba)
        if tipo_prueba == "1":
            nro_acaros = conteo_pricks(Stock_acaros)
            nro_pricks = conteo_pricks(Stock_cucarachas)+conteo_pricks(Stock_epitelios)+conteo_pricks(Stock_hongos)+conteo_pricks(Stock_gramineas)
            nro_pricks = nro_pricks + nro_acaros
            precio_final = ((nro_pricks*p_prick_sol)/60)+((nro_acaros*p_acaros_sol)/60)+(p_hist_sol/60)+(precio_hora*tiempo_prick)+precio_lanceta
            print("El precio final es de "+str(precio_final))
            print("\nDesea regresar al menu principal? Responda Si para regresar, No para salir:")
            respuesta = askyesorno()
            if respuesta == False:
                break
        elif tipo_prueba == "2":
            nro_pricks = conteo_pricks(Stock_alimentos)
            precio_final = ((nro_pricks*p_prick_sol)/60)+(p_hist_sol/60)+(precio_hora*tiempo_prick)+precio_lanceta
            print("El precio final es de "+str(precio_final))
            print("\nDesea regresar al menu principal? Responda Si para regresar, No para salir:")
            respuesta = askyesorno()
            if respuesta == False:
                break
        elif tipo_prueba == "3":
            print("\nIndique el nro de prick e ID a realizar: ")
            nro_pricks, nro_intra = input().split()
            if nro_pricks > 0:
                precio_final = (tiempo_prick*precio_hora)+(p_hist_sol/60)+(precio_hora*tiempo_prick)+precio_lanceta
            if nro_intra > 0:
                precio_final += (tiempo_intra*precio_hora)
            print("\nEl precio total es: "+precio_final)
                
    #Actualizacion de stocks
    elif seleccion_mainmenu == "2":
        print("Seleccione el grupo de reactivos a actualizar: \n")
        for key,value in Dict_reactivos.items():
            print(f"{key}:{value}")
        key_dict = input()
        
        name_dict = convert_key_to_prick(key_dict,Dict_reactivos)
        Dict_update = locals()[convert_key_to_prick(key_dict,Dict_reactivos)]
        Stock_update = locals()[convert_key_to_prick(key_dict,Dict_Stocks)]
        print("Usted selecciono: "+str(name_dict))
        print(f"\nSeleccione el reactivo a actualizar: \n")
        for key, value in Dict_update.items():
            print(f"{key}:{value}")
        key_prick = input()
        name_key = convert_key_to_prick(key_prick, Dict_update)
        print(f"Ingrese el nuevo stock: \n")
        new_stock = int(input())
        print(f"Se actualizara el reactivo "+str(name_key)+" con "+str(new_stock)+" de stock. Desea continuar ?")
        respuesta = askyesorno()
        if respuesta == True:
            update_stocks(dict=Stock_update, key=name_key, value=new_stock)

            if Stock_update == Stock_acaros:
                Stock_acaros[str(name_key)]=int(new_stock)
                print(Stock_acaros)
                print(name_key)
                print(new_stock)
            elif Stock_update == Stock_hongos:
                Stock_hongos.update({name_key:new_stock})
                print(Stock_hongos)
            elif Stock_update == Stock_cucarachas:
                Stock_cucarachas.update({name_key:new_stock})
                print(Stock_cucarachas)
            elif Stock_update == Stock_gramineas:
                Stock_gramineas.update({name_key:new_stock})
                print(Stock_gramineas)
            elif Stock_update == Stock_epitelios:
                Stock_epitelios.update({name_key:new_stock})
                print(Stock_epitelios)
            elif Stock_update == Stock_alimentos:
                Stock_alimentos.update({name_key:new_stock})
                print(Stock_alimentos)
            else:
                print("Valor ingresado no valido!")

            print("Se ha actualizado el reactivo "+str(name_key)+", ahora tiene "+str(new_stock)+" de stock\n")
            print("Regresando al menu principal\n")
        elif respuesta == False:
            print("Regresando al menu principal.")
    elif seleccion_mainmenu == "3":
        print("Gracias por usar nuestro aplicativo!")
        break