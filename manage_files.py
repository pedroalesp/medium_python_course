# Leemos un archivo de texto existente e imprimimos su contenido, guardándolo en una lista
def read():
    numbers = []
    with open('./files/numbers.txt', 'r', encoding='utf-8') as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


# Creamos o escribimos un archivo que no existía, a partir de una lista y el método write() - no confundir con el nombre de la función
# Nota que cada vez que hagamos esto, el archivo se va a sobrescribir en cada iteración
def write():
    pokemons = ['pikachu', 'charizard', 'bulbasaur', 'magicarp']
    with open('./files/pokemon.txt', 'w', encoding='utf-8') as f:
        for pokemon in pokemons:
            f.write(pokemon)
            f.write('\n')


# Añadimos contenido al archivo de arriba sin que se sobrescriba, en ocasiones necesitaremos de alguno de los dos métodos
def appen_method():
    pokemons_legendary = ['Zapdos', 'Entei', 'Rayquaza', 'Mew']
    with open('./files/pokemon.txt', 'a', encoding='utf-8') as f:
        for pokemon in pokemons_legendary:
            f.write(pokemon)
            f.write('\n') 


def run():
    appen_method()


if __name__ == '__main__':
    run()