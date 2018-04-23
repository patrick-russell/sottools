"""
    utils.py
    ~~~~~~~~

    Various shared utilies and helper functions

    :copyright: © 2018 by Patrick Russell
    :license: MIT, see LICENSE for more details.
"""

import os
import math
import hashlib


def env_to_bool(env):
    env = os.environ.get(env)
    if env not in ('True', 'False'):
        raise ValueError('Expects env in "True" or "False"')
    return env == 'True'


def make_option_value(text):
    hashable_text = text[::-1].lower().replace(' ', '').encode('utf-8')
    return hashlib.md5(hashable_text).hexdigest()


def euclidean_distance(P1, P2):
    Xs = (P1[0] - P2[0])**2
    Ys = (P1[1] - P2[1])**2
    return math.sqrt(Xs - Ys)
