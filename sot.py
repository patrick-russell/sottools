"""sot game things"""

import json


class SoT:
    '''Object to hold Sea of Thieves game information.
    Like locations, loot items, &c
    '''
    def __init__(self, **kwargs):
        with open('sot.json', 'r') as f:
            self.data = json.load(f)
        for k, v in self.data.items():
            setattr(self, k, v)
        if kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)


SOT = SoT()
