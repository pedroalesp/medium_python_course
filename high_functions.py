from typing import List


def run():
    # squares = [i ** 2 for i in my_list]
    # print(squares)


    my_list = [1, 2, 3, 4, 5]
    squares = list(map(lambda i: i**2, my_list))
    print(squares)


if __name__ == '__main__':
    run()