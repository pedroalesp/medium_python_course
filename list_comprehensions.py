def run():
    # nat_numbers = []
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         nat_numbers.append(i**2)

    # Forma 1: Porque 36 es el único número divisible entre 4, 6 y 9
    nat_numbers =[i for i in range(1, 100000) if i % 36 == 0]
    print(nat_numbers)

    #Forma 2: Con operadores lógicos
    nat_numbers_2 =[i for i in range(1, 100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    print(nat_numbers_2)


if __name__ == '__main__': 
    run()