from collections import namedtuple
import csv
import matplotlib.pyplot as plt
RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')
def lee_poblaciones(ruta_fichero):
    with open(ruta_fichero,encoding='utf-8') as f:
        lista = []
        fichero = csv.reader(f)
        for pais,codigo,año,censo in fichero:
            pais = pais                
            codigo = codigo
            año = int(año)
            censo = int(censo)
            RegistroPoblacion = (pais,codigo,año,censo)
            lista.append(RegistroPoblacion)
        return lista
        
def calcula_paises(poblaciones):
    lista = []
    for pais,codigo,año,censo in poblaciones:
        pais = pais
        if pais not in lista:
            lista.append(pais)
    lista.sort()
    return lista

def filtra_por_pais(poblaciones, nombre_o_codigo):
    lista = []
    for pais,codigo,año,censo in poblaciones:
        if nombre_o_codigo == pais or codigo:
            año = int(año)
            censo = int(censo)
            FechaPoblacion = (año,censo)
            lista.append(FechaPoblacion)
    return lista

def filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    lista = []
    for pais,codigo,año,censo in poblaciones:
        for i in paises:
            if i == pais:
                if anyo == int(año):
                    censo = int(censo)
                    PaisHabitantes = (pais, censo)
                    lista.append(PaisHabitantes)
    return lista

def muestra_evolucion_poblacion(poblaciones, nombre_o_codigo):
    lista_años = []
    lista_habitantes = []
    for pais,codigo,año,censo in poblaciones:
        if nombre_o_codigo == pais or codigo:
            año = int(año)
            censo = int(censo)
            lista_habitantes.append(censo)
            lista_años.append(año)
    plt.title(f'Evolucion de censo en {nombre_o_codigo}')
    plt.plot(lista_años, lista_habitantes)
    plt.show()

def muestra_comparativa_paises_anyo(poblaciones, anyo, paises):
    lista_paises = []
    lista_habitantes = []
    for pais,codigo,año,censo in poblaciones:
        for i in paises:
            if i == pais:
                if anyo == int(año):
                    censo = int(censo)
                    lista_paises.append(pais)
                    lista_habitantes.append(censo)
    plt.title('Comparación de censos')
    plt.bar(lista_paises, lista_habitantes)
    plt.show()

if __name__ == '__main__':
    poblaciones = lee_poblaciones('data/population.csv')
    muestra_comparativa_paises_anyo(poblaciones, 2016, ('Austria', 'Arab World'))