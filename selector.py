import random

def check_python():
    print('check python')

def random_num():
    return random.sample(range(1, 46), k=6)

if __name__ == '__main__':
    print(random_num())
