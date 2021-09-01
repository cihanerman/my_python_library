# -*- coding: utf-8 -*-
# librays
import datetime
import random
import string


# class and functions


class Switcher(object):
    """Python switch case

        example:
            keys = ["a","b","c"]
            values = [1,2,3]
            switch = Switcher(keys, values)
            print(switch.get_case("a")) #=> 1
            print(switch.get_case("q")) #=> None
            switch = Switcher(keys, values, 'Not found')
            print(switch.get_case("q")) #=> Not found
    """

    def __init__(self, keys, values, default=None):
        self.switch = dict(zip(keys, values))
        self.default = default

    def get_case(self, key):
        return self.switch.get(key, self.default)


def switcher(keys: list, values: list, case, default=None):
    """ Python switch case function

        example:
            keys = ["a","b","c"]
            values = [1,2,3]
            print(switcher(keys, values, "a")) #=> 1
            print(switcher(keys, values, "q")) #=> None
            print(switcher(keys, values, "q", 'Not fount')) #=> Not fount
    """
    return dict(zip(keys, values)).get(case, default)


def safe_division(n, d):
    """Python safe division for ZeroDivisionError"""
    return n / d if d else 0


def converts_turkish_characters_to_english_characters(word: str) -> str:
    """ The function that converts Turkish characters to English characters

        Parameters:
            word: Related word
    """
    turkish_caracters = {
        ord(c): ord(t)
        for c, t in zip(u"şçıöüğŞÇİÜÖĞ", u"sciougSCIUOG")
    }
    return word.translate(turkish_caracters)


def random_string(length: int) -> str:
    """ Ramdom string creation function

        Parameters:
            length: Number of characters
    """
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choices(letters, k=length))


def diff_month(d1: datetime.datetime, d2: datetime.datetime) -> int:
    """ Calculates the difference in months between two dates """
    return abs((d1.year - d2.year) * 12 + d1.month - d2.month)


def check_string_case_insensitive(s1: str, s2: str) -> bool:
    """String equality check case insensitive

    Args:
        s1 (str): First string variable
        s2 (str): Second string variable

    Returns:
        bool: Equality status
    """

    return s1.lower() == s2.lower()


def multi_replace(string_: str, old_characters: str, new_characters=None) -> str:
    """Python multi replace function

    :param string_: The desired string to change
    :param old_characters: Characters requested to be changed
    :param new_characters:
    :return: new string
    :example:
        print(multi_replace('(+0546) 667 87 87', '()+ '))
        #=> 05466678787
    """
    trans_dict = dict(zip(old_characters, new_characters)) if new_characters else dict(
        zip(list(old_characters), [None] * len(old_characters)))
    return string_.translate(string_.maketrans(trans_dict))

def iscastlable(typ, value) -> bool:
    """Function that queries whether a cast can be done or not"""
    try:
        typ(value)
        return True
    except Exception as e:
        return False
    
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

"""add it to the corresponding function, it will suppress the name of the calling place
    import inspect
    print(inspect.stack()[1][3])
"""
