def run(): 
    list = [
        {'pokemon': 'pikachu', 'type' : 'electric'},
        {'pokemon': 'torchic', 'type' : 'fire'},
        {'pokemon': 'evee', 'type' : 'normal'},
        {'pokemon': 'greninja', 'type' : 'water'}
    ]

    # Acceder a los diccionarios usando índices de las listas
    # for i in list:
    #     (i['pokemon'], ':', i['type'])

    #Acceder a los diccionarios usando el método items
    for i in list:
        for pokemon, type in i.items():
            print(pokemon, '-', type)


    dict = {
        'fire_pokemon': ['torchic', 'chamander', 'cindaquill'],
        'water_pokemon': ['squirtuttle', 'psyduck', 'greninja'],
        'electric_pokemon': ['pikachu', 'zapdos', 'raichu']
    }

    #Imprimir los valores y kes del diccionario de listas
    # for key, value in dict.items():
    #     print(key, '-', value)



if __name__ == '__main__':
    run()