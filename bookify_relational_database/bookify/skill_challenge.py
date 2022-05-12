from string import ascii_letters
from string import punctuation
from random import choices
from copy import copy
# result = choices(list(ascii_letters),k=8)
# print("".join(result))
class Password:
    """Class for Pasword Generator"""
    
    INPUT_UNIVERSE = {
        'numbers': list(range(10)),
        'letters':list(ascii_letters),
        'punctuation':list(punctuation)
    }

    DEFAULT_LEN = {
        'low':8,
        'mid':12,
        'high':16
    }


    def __init__(self,strength='mid',length=None):
        """ Constructor """
        self.strength = strength
        self.length = length
        self.generate()

    @classmethod
    def show_input_universe(cls):
        return cls.INPUT_UNIVERSE
    
    def generate(self):
        generator = copy(self.INPUT_UNIVERSE['letters'])
        print(generator)
        length = self.length or self.DEFAULT_LEN.get(self.strength)
        print(length)
        if self.strength == 'high':
            generator += self.INPUT_UNIVERSE['numbers'] + self.INPUT_UNIVERSE['punctuation']
        else:
            generator +=  self.INPUT_UNIVERSE['numbers']
        self.genrerated_password = map(str,choices(generator,k=self.length))



p = Password('low')
print(p.genrerated_password)
