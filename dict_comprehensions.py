import math 

# Crea un diccionario donde las llaves sean los 100 primeros 
# números naturales y sus valores sean ellos mismos elevados al cubo

# def run():
#     nat_numbers = {i: i**3 for i in range(1, 101) if i % 3 != 0}
#     print(nat_numbers)

# Crea un dict donde las llaves sean los 1000 primeros números nat y sus valores
# sean la raíz cuadrada de ellos mismos

def run():
    nat_numbers = {i: round(math.sqrt(i), 2) for i in range(1, 1001)}
    print(nat_numbers)



if __name__ == '__main__':
    run()