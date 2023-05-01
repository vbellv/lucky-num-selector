import random

def random_num():
    return random.sample(range(1, 46), k=6)

if __name__ == '__main__':
    times = int(input('Enter num(1-100): '))
    for _ in range(times):
        print(random_num())
