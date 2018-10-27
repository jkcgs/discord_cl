import random


def print_random():
    for x in range(10):
        str_set = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        key = ''.join(random.SystemRandom().choice(str_set) for _ in [0]*50)

        print('Secret key {}: {}'.format(x, key))

    print('-----\nChoose one of them and use it as the SECRET_KEY value')


if __name__ == '__main__':
    print_random()
