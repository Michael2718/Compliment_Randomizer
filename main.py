import random
file = open('adjectives.txt', mode='r', encoding='utf8').read()
arr_of_adjectives = file.split("\n")
random_adjective = arr_of_adjectives[random.randrange(0, len(arr_of_adjectives))]
print("Спокойной ночи, мои {}❤".format(random_adjective[:-2] + 'ые'))  # для множественного числа
print("Спокойной ночи, моя {}❤".format(random_adjective))
