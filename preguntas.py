"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    import csv

    sum= 0
    with open('data.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            x=', '.join(row)
            sum+=int(x.split()[1])

    return sum
#print("Pregunta 1:")
#print(pregunta_01())

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    dic= {}
    with open('data.csv', 'r') as csvfile:
        lines = csvfile.readlines()
        for row in lines:
            row=row.replace("\n", "")
            columnas=row.split()
            leter=columnas[0]

            if leter in dic:
                dic[leter]+=1
            else:
                dic[leter]=1
    resp=[]
    for leter in sorted(dic):
        resp.append((leter,dic[leter]))

    return resp

#print("Pregunta 2:")
#print(pregunta_02())

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    dic= {}
    with open('data.csv', 'r') as csvfile:
        lines = csvfile.readlines()
        for row in lines:
            row=row.replace("\n", "")
            columnas=row.split()
            leter, number=columnas[0], columnas[1]

            if leter in dic:
                dic[leter]+=int(number)
            else:
                dic[leter]=int(number)
    resp=[]
    for leter in sorted(dic):
        resp.append((leter,dic[leter]))

    return resp

#print("Pregunta 3:")
#print(pregunta_03())

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    dic= {}
    with open('data.csv', 'r') as csvfile:
        lines = csvfile.readlines()
        for row in lines:
            row=row.replace("\n", "")
            columnas=row.split()
            mes=columnas[2].split("-")[1]

            if mes in dic:
                dic[mes]+=1
            else:
                dic[mes]=1
    resp=[]
    for mes in sorted(dic):
        resp.append((mes,dic[mes]))

    return resp

#print("Pregunta 4:")
#print(pregunta_04())

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    dic= {}
    with open('data.csv', 'r') as csvfile:
        lines = csvfile.readlines()
        for row in lines:
            row=row.replace("\n", "")
            columnas=row.split()
            leter, number=columnas[0], columnas[1]

            if leter in dic:
                if dic[leter][0] < int(number):
                    dic[leter][0]=int(number)

                if dic[leter][1] > int(number):
                    dic[leter][1]=int(number)
            else:
                dic[leter]=[int(number),int(number)]
    resp=[]
    for leter in sorted(dic):
        resp.append((leter,dic[leter][0],dic[leter][1]))

    return resp

#print("Pregunta 5:")
#print(pregunta_05())

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    dic= {}
    with open('data.csv', 'r') as csvfile:
        lines = csvfile.readlines()
        for row in lines:
            row=row.replace("\n", "")
            columnas=row.split()
            strings=columnas[4].split(",")
            for string in strings:
                leter,number=string.split(":")[0],string.split(":")[1]

                if leter in dic:
                    if dic[leter][1] < int(number):
                        dic[leter][1]=int(number)

                    if dic[leter][0] > int(number):
                        dic[leter][0]=int(number)
                else:
                    dic[leter]=[int(number),int(number)]
    resp=[]
    for leter in sorted(dic):
        resp.append((leter,dic[leter][0],dic[leter][1]))

    return resp

#print("Pregunta 6:")
#print(pregunta_06())

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    dic= {}
    with open('data.csv', 'r') as csvfile:
        lines = csvfile.readlines()
        for row in lines:
            row=row.replace("\n", "")

            columnas=row.split()
            leter, number=columnas[0], columnas[1]

            if number in dic:
                dic[number].append(leter)
            else:
                dic[number]=[leter]
    resp=[]
    for number in sorted(dic):
        resp.append((number,dic[number]))

    return resp

#print("Pregunta 7:")
#print(pregunta_07())

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """

    dic= {}
    with open('data.csv', 'r') as csvfile:
        lines = csvfile.readlines()
        for row in lines:
            row=row.replace("\n", "")
            columnas=row.split()
            leter, number=columnas[0], columnas[1]

            if number in dic:
                dic[number][leter]=leter
            else:
                dic[number]={leter:leter}
    resp=[]
    for number in sorted(dic):
        resp.append((number,sorted(dic[number])))

    return resp

#print("Pregunta 8:")
#print(pregunta_08())

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    dic= {}
    with open('data.csv', 'r') as csvfile:
        lines = csvfile.readlines()
        for row in lines:
            row=row.replace("\n", "")
            columnas=row.split()
            strings=columnas[4].split(",")
            for string in strings:
                leter=string.split(":")[0]

                if leter in dic:
                    dic[leter]+=1
                else:
                    dic[leter]=1

    return dic

#print("Pregunta 9:")
#print(pregunta_09())

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """

    resp= []
    with open('data.csv', 'r') as csvfile:
        lines = csvfile.readlines()
        for row in lines:
            row=row.replace("\n", "")
            columnas=row.split()
            leter, C4, C5=columnas[0], len(columnas[3].split(",")), len(columnas[4].split(","))
            resp.append((leter,C4,C5))

    return resp

#print("Pregunta 10:")
#print(pregunta_10())

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    dic= {}
    with open('data.csv', 'r') as csvfile:
        lines = csvfile.readlines()
        for row in lines:
            row=row.replace("\n", "")
            columnas=row.split()
            strings=columnas[3].split(",")
            number=int(columnas[1])
            for string in strings:
                leter=string

                if leter in dic:
                    dic[leter]+=number
                else:
                    dic[leter]=number

    return dic

#print("Pregunta 11:")
#print(pregunta_11())

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    dic= {}
    with open('data.csv', 'r') as csvfile:
        lines = csvfile.readlines()
        for row in lines:
            row=row.replace("\n", "")
            columnas=row.split()
            strings=columnas[4].split(",")
            sum=0
            for string in strings:
                sum+=int(string.split(":")[1])
            leter=columnas[0]
            if leter in dic:
                dic[leter]+=sum
            else:
                dic[leter]=sum

    return dic
#print("Pregunta 12:")
#print(pregunta_12())