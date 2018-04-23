"""
    sotgame.py
    ~~~~~~~~

    sot game things.

    Shared object with locations, items, etc
    Pushing all the logic for loading that info into this module.
    We currently keep things in a file but can swap out to a database
    without changing the website.

    :copyright: © 2018 by Patrick Russell
    :license: MIT, see LICENSE for more details.
"""

import json


class SoT:
    """Object to hold Sea of Thieves game information.
    Like locations, loot items, &c
    """

    def __init__(self, **kwargs):
        with open('sot.json', 'r') as f:
            self.data = json.load(f)
        for k, v in self.data.items():
            setattr(self, k, v)

        if kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)


sot = SoT()
