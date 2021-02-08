# -*- coding: utf-8 -*-
# librays
import random, string, datetime

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
    def __init__(self, keys, values, default= None):
        self.switch = dict(zip(keys, values))
        self.default = default
    
    def get_case(self, key):
        return self.switch.get(key, self.default)

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
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def diff_month(d1: datetime.datetime, d2: datetime.datetime) -> int:
    """ Calculates the difference in months between two dates """
    return abs((d1.year - d2.year) * 12 + d1.month - d2.month)
