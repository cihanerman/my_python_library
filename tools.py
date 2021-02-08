class Switcher(object):
    """Python switch case
    
        example:
            keys = ["a","b","c"]
            values = [1,2,3]
            switch = Switcher(keys, values)
            print(switch.get_case("a")) #=> 1
            print(switch.get_case("q")) #=> None
    """
    def __init__(self, keys, values):
        self.switch = dict(zip(keys, values))
    
    def get_case(self, key):
        return self.switch.get(key, None)
