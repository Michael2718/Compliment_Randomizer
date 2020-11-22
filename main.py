import random


def is_hard_consonant(c):
    """
    Returns True if the russian letter c is hard consonant(according to the russian grammar).

    Parameters:
        c (str):The letter to be checked.
    Returns:
        bool:True if c is hard hard consonant or false if it is not.
    """
    hard_letters = ['п', 'б', 'ф', 'в', 'т', 'д', 'с', 'з', 'ц', 'м', 'н', 'р', 'л']
    return c in hard_letters


def generate_compliment(array, mode):
    """
    Returns the random compliment(adjective then) from an array and formats it according to mode.
    Formatting works only with russian adjectives so far.

    Parameters:
        array (list):The list of adjectives.
        mode (str):The adjective formatting mode, should equal 'single' or 'plural'.
    Returns:
        str:The random adjective from an array in the right form, specified by mode.
    """
    random_adjective = array[random.randrange(len(array))]
    if mode == 'single':
        return random_adjective
    elif mode == "plural":
        if is_hard_consonant(random_adjective[-3]) and random_adjective[-2] != 'я':
            return random_adjective[:-2] + 'ые'
        else:
            return random_adjective[:-2] + 'ие'


if __name__ == "__main__":
    file = open('adjectives.txt', mode='r', encoding='utf8').read()
    arr_of_adjectives = file.split("\n")
    print("Спокойной ночи, моя {}❤".format(generate_compliment(arr_of_adjectives, mode='single')))  # Usage example
