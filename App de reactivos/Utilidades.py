from Diccionarios import Dict_reactivos, Dict_alimentos, Dict_cucarachas, Dict_epitelios, Dict_gramineas, Dict_acaros, Dict_hongos, dict_pruebas, Stock_acaros, Stock_alimentos, Stock_cucarachas, Stock_epitelios, Stock_gramineas, Stock_hongos

USD_PEN = 3.42
precio_hist_dol = 50.0
precio_acaros_dol = 35.0
precio_prick_dol = 30.0
tiempo_prick = 15
tiempo_intra = 30
precio_hora = 50
precio_lanceta = 0.346
nro_acaros = 0
nro_pricks = 0
nro_intra = 0
tipo_prueba = 0
key_prick = "none"

def conv_dol(var):
    """Funcion para conversion dolares"""
    return (var * USD_PEN)

def precio_aero(precio_hora, precio_insumo, precio_total_reactivos):
    """Funcion para calculo de precio total para prick test de aeroalergenos"""
    return precio_hora + precio_insumo + precio_total_reactivos

def askyesorno():
    """Funcion para preguntar si o no"""
    while True:
        user_input = input().strip().lower()

        if user_input in ["y","yes","si"]:
            return True
        elif user_input in ["n","no"]:
            return False
        else: print("Por favor responda si o no")

def mainmenu_select():
    """Funcion para menu principal"""
    while True:
        user_input = input().strip()

        if user_input in ["1","2","3","4"]:
            return user_input
        else:
            print("Elija una funcion valida\n")

def select_prueba():
    """Funcion para seleccion de prueba"""
    while True:
        print("Seleccione el tipo de prueba\n")
        print("1.Prick test con aeroalergenos\n2.Prick test con alimentos\n3.Prick test con medicamentos\n")
        tipo_prueba = input().strip()
        return tipo_prueba

def stockdetail(inputvalue):
    """Detalle de stocks"""
    if inputvalue == "1":
        for key, value in Stock_acaros.items():
            print(f"{key}:{value}")
        for key, value in Stock_cucarachas.items():
            print(f"{key}:{value}")
        for key, value in Stock_hongos.items():
            print(f"{key}:{value}")
        for key, value in Stock_gramineas.items():
            print(f"{key}:{value}")
    elif inputvalue == "2":
        for key, value in Stock_alimentos.items():
            print(f"{key}:{value}")
    elif inputvalue == "3":
        print("\nBrindando un estimado de costo, no se puede agregar costo de medicamento, agregarlo de forma manual.\n")

def convert_key_to_prick(k,Dict):
    """Convertir keys ingresadas en nombre completo segun diccionario"""
    value = Dict.get(k)
    return value

def update_stocks(dict,key,value):
    """Actualizacion de stocks"""
    dict[key]=value
    return print("Valor actualizado !")

def conteo_pricks(dict):
    """Contar nro de pricks a usar"""
    for key,value in dict.items():
        conteo = 0
        if value == 1:
            conteo += 1
        return int(conteo)
        

    


