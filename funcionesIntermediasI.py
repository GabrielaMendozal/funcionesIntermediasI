# Actualizar valores en diccionarios y listas

x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


#Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
x = [ [5,2,3], [10,8,9] ]

x[1][0]=15
print (x)

#Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.

estudiantes[0] ['last_name'] = 'Bryant'
print (estudiantes)

#En el directorio_deportes, cambia "Messi" por "Andrés".


directorio_deportes ['fútbol'] [0] = "Andrés"
print (directorio_deportes)


#Cambia el valor 20 en z a 30.
z [0] ['y'] = 30
print (z)

# 2 Iterar a través de una lista de diccionarios
#iterateDictionary(estudiantes) 

estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


# debería devolver: (está bien si cada par clave-valor termina en 2 líneas separadas;
# un bonus para que aparezcan exactamente como se muestra a continuación)
#first_name - Michael, last_name - Jordan
#first_name - John, last_name - Rosales
#first_name - Mark, last_name - Guillen
#first_name - KB, last_name - Tonel

def iterate_Dictionary(list):
    for i in range(0, len(list)):
        output = ""
        for key,val in list[i].items():
            output += f" {key} - {val},"
        print(output)

iterate_Dictionary(estudiantes)  


#Obtener valores de una lista de diccionarios

def iterate_Dictionary2(key_name, list):
    for i in range (0, len (list)):
    
        for key, val in list [i].items():
            if key ==key_name:
                print (val)

iterate_Dictionary2('first_name',estudiantes)
iterate_Dictionary2('last_name',estudiantes)

#Iterar a través de un diccionarios con valores de lista

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_Info(dict):
    for key,val in dict.items():
        print(f"{len(val)} {key.upper()}")
        for i in range(0, len(val)):
            print(val[i])

print_Info(dojo)