# Compliment_Randomizer
Script generates random russian compliment(adjective) for girl/girls.


Requirements
------------

Import lib from standard library.



Typical usage
-------------
You can't make cool compliments? Here we go, now you can simply get random compliment using ths function! 
Here is a small example to whet your appetite (Python 3):

```python
"""Here is some code"""
print("Ты сегодня просто {}❤".format(generate_compliment(arr_of_adjectives, mode='single')))
# prints "Ты сегодня просто шикарная❤"
print("Спокойной ночи, мои {}❤".format(generate_compliment(arr_of_adjectives, mode='plural')))
# prints "Спокойной ночи, мои обоятельные❤"