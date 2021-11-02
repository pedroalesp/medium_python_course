def divisor(num):
    assert num > 0, 'You can type natural numbers only'
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    print(divisors)


def run():
    try:
        num = int(input('Type a numer: '))
        divisor(num)
    except ValueError:
        print('Type just numbers')


if __name__ == '__main__':
    run()