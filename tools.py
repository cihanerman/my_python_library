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
