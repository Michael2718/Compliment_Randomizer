import random


def is_hard_consonant(c):
    hard_letters = ['п', 'б', 'ф', 'в', 'т', 'д', 'с', 'з', 'ц', 'м', 'н', 'р', 'л']
    return c in hard_letters


def generate_compliment(array, mode):
    random_adjective = array[random.randrange(0, len(array))]
    if mode == 'single':
        return "Спокойной ночи, моя {}❤".format(random_adjective)
    elif mode == "plural":
        if is_hard_consonant(random_adjective[-3]) and random_adjective[-2] != 'я':
            return "Спокойной ночи, мои {}❤".format(random_adjective[:-2] + 'ые')
        else:
            return "Спокойной ночи, мои {}❤".format(random_adjective[:-2] + 'ие')


if __name__ == "__main__":
    file = open('adjectives.txt', mode='r', encoding='utf8').read()
    arr_of_adjectives = file.split("\n")
    for x in range(100):
        print(generate_compliment(arr_of_adjectives, mode='plural'))
