def divisor(num):
    try:
        if num <= 0:
            raise ValueError('You can type natural numbers only')
        divisors = [i for i in range(1, num + 1) if num % i == 0]
        print(divisors)
    except ValueError as ve:
        print(ve)


def run():
    try:
        num = int(input('Type a numer: '))
        divisor(num)
    except ValueError:
        print('Type just numbers')


if __name__ == '__main__':
    run()