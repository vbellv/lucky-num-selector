import random

def check_python():
    print('check python')

def random_num():
    result = random.sample(range(1, 46), k=6)
    print(result)

if __name__ == '__main__':
    random_num()
